from flask import Flask, request, jsonify
from models import *
from services import *         

app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return "Hello World!"

@app.route("/project", methods=["POST"])
def create_project():
    return jsonify(ProjectService().create({
        "ID": 20,
        "ProjectName": "TestProject",
        "ProjectDescription": "TestProject",
        "ProjectLead": "Andrew",
        "StartDate": "Today"
    }))

if __name__ == '__main__':
    ProjectSchema()
    app.run(debug = True)