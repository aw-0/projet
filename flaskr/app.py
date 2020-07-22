from flask import Flask, request, jsonify, render_template, url_for, redirect
from models import *
from services import *         

app = Flask(__name__)    

# @app.route("/")                   
# def hello():                      
#     return "Hello World!"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST'])
def login():
    user = request.form['nm']
    return redirect(url_for('success',name=user))

@app.route('/projectAdd')
def project_add():
    return render_template('projectAdd.html')

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