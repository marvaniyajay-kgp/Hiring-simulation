from Concordia import Component

class ResumeComponent(Component):
    def __init__(self, name, gender, education, experience, skills):
        self.name = name
        self.gender = gender
        self.education = education
        self.experience = experience
        self.skills = skills

    def state(self):
        return f"Name: {self.name}\nGender: {self.gender}\nEducation: {self.education}\nExperience: {self.experience}\nSkills: {', '.join(self.skills)}"

class JobDescriptionComponent(Component):
    def __init__(self, title, qualifications, responsibilities):
        self.title = title
        self.qualifications = qualifications
        self.responsibilities = responsibilities

    def state(self):
        return f"Title: {self.title}\nQualifications: {', '.join(self.qualifications)}\nResponsibilities: {', '.join(self.responsibilities)}"

class CandidatePool(Component):
    def __init__(self):
        self.resumes = []

    def add_resume(self, resume):
        self.resumes.append(resume)

    def state(self):
        return "\n\n".join([resume.state() for resume in self.resumes])