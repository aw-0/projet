from flask import Flask, request, jsonify, render_template, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from models import *
from services import *         

app = Flask(__name__, static_folder='static') 

templateLoader = FileSystemLoader("/Users/andrew/Desktop/Coding/CoderSchool/Projet-main/flaskr/templates")
env = Environment(loader=templateLoader)

@app.route("/example1")
def example1():
    return render_template('example1.html')

@app.route('/example1PostReturn/<name>')
def example1PostReturn(name):
    return f'Welcome {name}!'

@app.route('/example1Post', methods=['POST'])
def example1Post():
    user = request.form['nm']
    return redirect(url_for('example1PostReturn',name=user))

@app.route("/home")
def home():
    template = env.get_template('home.html')
    return template.render(userContext="Andrew")

@app.route("/projectAdd", methods=["GET"])
def projectAdd():
    template = env.get_template('projectAdd.html')
    return template.render(userContext="Andrew")

# @app.route("/projectAddPostReturn/<ID>/<projectName>")
# def projectAddPostReturn(ID, projectName):
#     tm = Template("{{ projectName }} is created successfully.")
#     return tm.render(projectName=projectName)

@app.route("/projectAdd", methods=["POST"])
def projectAddPost():
    project = {
        "ProjectName": request.form['ProjectName'],
        "ProjectDescription": request.form['ProjectDescription'],
        "ProjectLead": request.form['ProjectLead'],
        "StartDate": request.form['StartDate']
    }
    ProjectService().create(project)
    return redirect(url_for('projectList'))
    #return redirect(url_for('projectAddPostReturn', ID=returnObject['ID'], projectName=returnObject['ProjectName']))

@app.route("/projectEdit", methods=['GET'])
def projectEdit():
    projectID = request.args.get('id')
    project = ProjectService().select({
        "ID": projectID
    })
    template = env.get_template('projectEdit.html')
    return template.render(project=project)

@app.route("/projectEdit", methods=["POST"])
def projectEditPost():
    project = {}

    project["ID"]=request.form['id']
    project["ProjectName"]= request.form['projectName']
    project["ProjectDescription"]= request.form['projectDescription']
    project["ProjectLead"]= request.form['projectLead']
    project["StartDate"]= request.form['startDate']

    ProjectService().update(project)
    return redirect(url_for('projectList'))

@app.route("/projectDelete", methods=["GET"])
def delete_project():
    projectID = request.args.get('id')
    ProjectService().delete({
        "ID": projectID
    })
    return redirect(url_for('projectList'))
    #return jsonify(ProjectService().delete(request.get_json()))

@app.route("/projectList")
def projectList():
    projectList = ProjectService().selectAll()
    template = env.get_template('projectList.html')
    return template.render(userContext="Andrew", projectList=projectList)

@app.route("/project", methods=["POST"])
def create_project():
    return jsonify(ProjectService().create(request.get_json()))

@app.route("/project", methods=["GET"])
def view_project():
    return jsonify(ProjectService().select(request.get_json()))

@app.route("/projectAll", methods=["GET"])
def view_all_project():
    return jsonify(ProjectService().selectAll())


if __name__ == '__main__':
    ProjectSchema().createProjectTable()
    print(ProjectModel().generateNewID())#ProjectModel().selectAll ())
    app.run(debug = True)