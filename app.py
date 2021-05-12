from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)


# Configure DB
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)


   

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


@app.route('/projects/:id')
def project_id():
    return 'Projeto id'


@app.route('/new_project')
def new_project():
    return 'novo projeto'


@app.route('/alocation')
def alocation():
    return 'Alocação'
    






if __name__ == '__main__':
    app.run(debug=True)