from flask import Flask, request, jsonify, render_template, url_for, redirect
from models import *
from services import *         

app = Flask(__name__)    

# @app.route("/")                   
# def hello():                      
#     return "Hello World!"

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

@app.route('/projectAdd')
def project_add():
    return render_template('projectAdd.html')

@app.route("/projectAddPostReturn/<ID>/<projectName>")
def projectAddPostReturn(ID, projectName):
    return f"{projectName} is created successfully."

@app.route("/projectAddPost", methods=["POST"])
def projectAddPost():
    project = {
        "ID": request.form['ID'],
        "ProjectName": request.form['ProjectName'],
        "ProjectDescription": request.form['ProjectDescription'],
        "ProjectLead": request.form['ProjectLead'],
        "StartDate": request.form['StartDate']
    }
    returnObject = ProjectService().create(project)
    return redirect(url_for('projectAddPostReturn', ID=returnObject['ID'], projectName=returnObject['ProjectName']))

@app.route("/project", methods=["POST"])
def create_project():
    return jsonify(ProjectService().create(request.get_json()))

@app.route("/project", methods=["PUT"])
def update_project():
    return jsonify(ProjectService().update(request.get_json()))

@app.route("/project", methods=["DELETE"])
def delete_project():
    return jsonify(ProjectService().delete(request.get_json()))

@app.route("/project", methods=["GET"])
def view_project():
    return jsonify(ProjectService().select(request.get_json()))

@app.route("/projectAll", methods=["GET"])
def view_all_project():
    return jsonify(ProjectService().selectAll())


if __name__ == '__main__':
    ProjectSchema()
    print(ProjectModel().selectAll ())
    app.run(debug = True)