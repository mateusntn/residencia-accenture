from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import yaml

app = Flask(__name__)


# Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:doninha20@localhost/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)





@app.route('/')
def index(): 
    return 'index'

@app.route('/login')
def login():
    return 'Login'


@app.route('/register')
def register():
    return 'Register'

@app.route('/dashboard')
def dashboard():
    return 'Dashboard'
    

@app.route('/projects')
def projects():
    return 'Projetos'


@app.route('/projects/<int:id>')
def project_id(id):
    return 'Projeto id'


@app.route('/new_project', methods=['GET', 'POST'])
def new_project():
    
    return render_template ('/index.html')


@app.route('/alocation')
def alocation():
    return 'Alocação'
    






if __name__ == '__main__':
    app.run(debug=True)