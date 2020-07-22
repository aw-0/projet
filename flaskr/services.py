from models import ProjectModel

class ProjectService:
    def __init__(self):
        self.model = ProjectModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, params):
        return self.model.update(params)

    def delete(self, params):
        return self.model.delete(params)

    def select(self, params):
        return self.model.select(params)
    
    def selectAll(self):
        return self.model.selectAll()
