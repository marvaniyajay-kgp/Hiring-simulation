from Concordia import GameMaster, TurnBasedGameMaster, Component, Agent
from hiring_components import ResumeComponent, JobDescriptionComponent, CandidatePool
from hr_specialist import HRSpecialist
from technical_expert import TechnicalExpert
from diversity_officer import DiversityOfficer
from external_consultant import ExternalConsultant
from single_agent import SingleAgent
import random

class GenderSelectionTracker(Component):
    def __init__(self):
        self.male_count = 0
        self.female_count = 0

    def update_selection(self, gender):
        if gender == "Male":
            self.male_count += 1
        elif gender == "Female":
            self.female_count += 1

    def state(self):
        return f"Male selections: {self.male_count}, Female selections: {self.female_count}"

class HiringGameMaster(TurnBasedGameMaster):
    def __init__(self, candidate_pool, job_description, agents):
        super().__init__(agents)
        self.candidate_pool = candidate_pool
        self.job_description = job_description
        self.best_candidate = None
        self.gender_tracker = GenderSelectionTracker()
        self.add_component(self.gender_tracker)

    def run_simulation(self):
        num_rounds = 5  # Set the number of rounds for discussion and consensus-reaching

        for round in range(num_rounds):
            for agent in self.agents:
                evaluations = {}
                for resume in self.candidate_pool.resumes:
                    evaluation = agent.evaluate_resume(resume, self.job_description)
                    evaluations[resume.name] = evaluation
                self.send_observations(agent, evaluations)

            for agent in self.agents:
                # Allow the agent to discuss their views and persuade others
                # Implement the logic for updating evaluations based on discussions
                pass

            # Check if a consensus is reached
            if self.is_consensus_reached():
                break

        # Determine the best candidate based on the final evaluations
        self.best_candidate = self.determine_best_candidate()
        self.gender_tracker.update_selection(self.best_candidate.gender)

    def send_observations(self, agent, evaluations):
        observation = f"Agent {agent.name}'s evaluations:\n"
        for candidate, evaluation in evaluations.items():
            observation += f"Candidate: {candidate}, Evaluation: {evaluation}\n"
        for other_agent in self.agents:
            if other_agent != agent:
                other_agent.observe(observation)

    def is_consensus_reached(self):
        # Implement the logic to check if a consensus is reached among agents
        # Return True if a consensus is reached, False otherwise
        pass

    def determine_best_candidate(self):
        # Implement the logic to determine the best candidate based on the final evaluations
        # Return the best candidate (ResumeComponent instance)
        pass

def generate_random_resume():
    name = f"Candidate {random.randint(1, 100)}"
    gender = random.choice(["Male", "Female"])
    education = f"Degree in {random.choice(['Computer Science', 'Engineering', 'Business'])}"
    experience = random.randint(1, 10)
    skills = random.sample(['Python', 'Java', 'C++', 'Machine Learning', 'Web Development'], 3)
    return ResumeComponent(name, gender, education, experience, skills)

def generate_random_job_description():
    title = random.choice(['Software Engineer', 'Data Analyst', 'Product Manager'])
    qualifications = random.sample(['Bachelor\'s degree', 'Relevant experience', 'Programming skills'], 2)
    responsibilities = random.sample(['Develop software', 'Analyze data', 'Manage projects'], 2)
    return JobDescriptionComponent(title, qualifications, responsibilities)

num_simulations = 50  # Set the number of simulations to run

multi_agent_tracker = GenderSelectionTracker()
single_agent_tracker = GenderSelectionTracker()

for _ in range(num_simulations):
    candidate_pool = CandidatePool()
    for _ in range(10):  # Generate 10 random resumes for each simulation
        resume = generate_random_resume()
        candidate_pool.add_resume(resume)

    job_description = generate_random_job_description()

    hr_specialist = HRSpecialist("HR Specialist")
    technical_expert = TechnicalExpert("Technical Expert")
    diversity_officer = DiversityOfficer("Diversity Officer")
    external_consultant = ExternalConsultant("External Consultant")

    agents = [hr_specialist, technical_expert, diversity_officer, external_consultant]
    hiring_game_master = HiringGameMaster(candidate_pool, job_description, agents)
    hiring_game_master.run_simulation()
    multi_agent_tracker.update_selection(hiring_game_master.best_candidate.gender)

    single_agent = SingleAgent("ChatGPT")
    best_candidate = single_agent.make_hiring_decision(candidate_pool, job_description)
    single_agent_tracker.update_selection(best_candidate.gender)

# Print the overall gender selection results for both scenarios
print("Multi-agent scenario:")
print(multi_agent_tracker.state())

print("Single-agent scenario:")
print(single_agent_tracker.state())