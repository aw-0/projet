import sqlite3

class ProjectSchema:
    def __init__(self):
        self.conn = sqlite3.connect('Project.db')
        self.createProjectTable()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def createProjectTable(self):

        self.conn.execute('''CREATE TABLE IF NOT EXISTS Project
        (ID INT     NOT NULL,
        ProjectName          TEXT    NOT NULL,
        ProjectDescription          TEXT    NOT NULL,
        ProjectLead          TEXT    NOT NULL,
        StartDate         TEXT       NOT NULL);''')

class ProjectModel:
    def __init__(self):
        self.conn = sqlite3.connect('Project.db')

    def create(self, params):

        ID = params["ID"]
        ProjectName = params["ProjectName"]
        ProjectDescription= params["ProjectDescription"]
        ProjectLead = params["ProjectLead"]
        StartDate = params["StartDate"]
        
        self.conn.execute(f"INSERT INTO Project (ID, ProjectName,ProjectDescription,ProjectLead,StartDate) \
        VALUES ({ID}, '{ProjectName}', '{ProjectDescription}', '{ProjectLead}','{StartDate}' )")

        
        self.conn.commit()

        return {
            "ID": ID,
            "ProjectName": ProjectName,
            "ProjectDescription": ProjectDescription,
            "ProjectLead": ProjectLead,
            "StartDate": StartDate
        }

    def update(self, params):

        ID = params["ID"]
        ProjectName = params["ProjectName"]
        ProjectDescription= params["ProjectDescription"]
        ProjectLead = params["ProjectLead"]
        StartDate = params["StartDate"]

        self.conn.execute(f"""UPDATE Project SET
            ProjectName = '{ProjectName}', 
            ProjectDescription = '{ProjectDescription}', 
            ProjectLead = '{ProjectLead}',
            StartDate = '{StartDate}'
            WHERE ID = {ID}""")

        self.conn.commit()
        
        return {
            "ID": ID,
            "ProjectName": ProjectName,
            "ProjectDescription": ProjectDescription,
            "ProjectLead": ProjectLead,
            "StartDate": StartDate
        }

    def delete(self, params):

        ID = params["ID"]

        self.conn.execute(f"DELETE FROM Project WHERE ID = {ID}")

        self.conn.commit()

        return {
            "status": 1
        }

    def selectAll(self):
        result = {}

        cursor = self.conn.execute(f"SELECT * FROM PROJECT")

        for row in cursor:
            result["ID"] = str(row[0])
            result["ProjectName"] = row[1]
            result["ProjectDescription"] = row[2]
            result["ProjectLead"] = row[3]
            result["StartDate"] = row[4]
        
        return result
    
    def select(self, params):
        ID = params["ID"]

        result = {}

        cursor = self.conn.execute(f"SELECT * FROM PROJECT WHERE ID = {ID}")

        for row in cursor:
            result["ID"] = str(row[0])
            result["ProjectName"] = row[1]
            result["ProjectDescription"] = row[2]
            result["ProjectLead"] = row[3]
            result["StartDate"] = row[4]
        
        return result