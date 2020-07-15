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

    def create(self, ID, ProjectName, ProjectDescription, ProjectLead, StartDate):

        print(ID)
        
        result = self.conn.execute(f"INSERT INTO Project (ID, ProjectName,ProjectDescription,ProjectLead,StartDate) \
        VALUES ({ID}, '{ProjectName}', '{ProjectDescription}', '{ProjectLead}','{StartDate}' )")

        
        self.conn.commit()

        return result

    def update(self, ID, ProjectName, ProjectDescription, ProjectLead, StartDate):

        result = self.conn.execute(f"""UPDATE Project SET
            ProjectName = '{ProjectName}', 
            ProjectDescription = '{ProjectDescription}', 
            ProjectLead = '{ProjectLead}',
            StartDate = '{StartDate}'
            WHERE ID = {ID}""")

        self.conn.commit()
        
        return result

    def delete(self, ID):

        result = self.conn.execute(f"DELETE FROM Project WHERE ID = {ID}")

        self.conn.commit()

        return result

    def select(self):
        result = ""

        cursor = self.conn.execute(f"SELECT * FROM PROJECT")

        for row in cursor:
            result = result + "ID = " + str(row[0]) + "\n"
            result = result + "ProjectName = " + row[1] + "\n"
            result = result + "ProjectDescription = " + row[2] + "\n"
            result = result + "ProjectLead = " + row[3] + "\n"
            result = result + "Start Date = " + row[4] + "\n"
        
        return result