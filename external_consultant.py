from Concordia import Agent, Component

class ExternalConsultantIdentity(Component):
    def __init__(self, name):
        self.name = name
        self.role = "External Consultant"
        self.expertise = "Unbiased evaluation and overall fit"

    def state(self):
        return f"Name: {self.name}\nRole: {self.role}\nExpertise: {self.expertise}"

class ExternalConsultantEvaluationComponent(Component):
    def __init__(self):
        self.criteria = ["Overall qualifications", "Fit for the role"]

    def evaluate_resume(self, resume, job_description):
        # Implement the evaluation logic based on the External Consultant's criteria
        # Return a score or assessment
        pass

    def state(self):
        return f"External Consultant evaluation criteria: {', '.join(self.criteria)}"

class ExternalConsultant(Agent):
    def __init__(self, name):
        super().__init__()
        self.identity = ExternalConsultantIdentity(name)
        self.evaluation_component = ExternalConsultantEvaluationComponent()
        self.add_component(self.identity)
        self.add_component(self.evaluation_component)