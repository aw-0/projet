from models import ProjectModel

class ProjectService:
    def __init__(self):
        self.model = ProjectModel()

    def create(self, params):
        return self.model.create(params["ID"],params["ProjectName"],params["ProjectDescription"],params["ProjectLead"],params["StartDate"])