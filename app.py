from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import yaml

app = Flask(__name__)


# Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:doninha20@localhost/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Projeto(db.Model):
    __tablename__ = "projetos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)
    custoPrevisto = db.Column(db.Float, nullable=True)
    area = db.Column(db.String(45), nullable=True, index=True)
    descricao = db.Column(db.String(500), nullable=True, index=True)
    otherCost = db.Column(db.Float, nullable=True, index=True)
    hardware = db.Column(db.Float, nullable=True, index=True)
    licenca = db.Column(db.Float, nullable=True, index=True)
    duracao = db.Column(db.String(45), nullable=True, index=True)
    status = db.Column(db.String(45), nullable=True, index=True)
    seatCharge = db.Column(db.Float, nullable=True, index=True)
    nomeEmpresa = db.Column(db.String(45), nullable=True, index=True)


class Habilidade(db.Model):
    __tablename__ = "funcionarios" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=True, index=True)




def __str__(self):
    return self.name



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
    if request.method == 'POST':
        projetos = Projeto()
        projetos.nome = request.form['nome']
        projetos.custoPrevisto = request.form['custoPrevisto']
        projetos.area = request.form['area']
        projetos.descricao = request.form['descricao']
        projetos.otherCost = request.form['otherCost']
        projetos.hardware = request.form['hardware']
        projetos.licenca = request.form['licenca']
        projetos.duracao = request.form['duracao']
        projetos.status = request.form['status']
        projetos.seatCharge = request.form['seatCharge']
        projetos.nomeEmpresa = request.form['nomeEmpresa']

        db.session.add(projetos)
        db.session.commit()

        return redirect('/projects')
    return render_template ('/index.html')


@app.route('/alocation')
def alocation():
    return 'Alocação'
    






if __name__ == '__main__':
    app.run(debug=True)