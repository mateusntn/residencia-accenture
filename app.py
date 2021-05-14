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
    __tablename__ = "habilidades" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)


class Cargo(db.Model):
    __tablename__ = "cargos" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)


class Funcionario(db.Model):
    __tablename__ = "funcionarios" 
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(100), nullable=False, index=True)
    custoHora = db.Column(db.Decimal, nullable=False)
    quantProjetos = db.Column(db.Integer, nullable=False)
    disponibilidade = db.Column(db.String(45), nullable=False)
    custoHora_overtime = db.Column(db.String(45), nullable=True)
    cargo_id = db.Column(db.Integer, foreign_key=True, nullable=False)


class Usuario(db.Model):
    __tablename__ = "usuarios" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)
    email = db.Column(db.String(45), nullable=True, index=True)
    senha = db.Column(db.String(250), nullable=True)
    funcionarios_id = db.Column(db.Ineger, nullable=False)
    funcionarios_cargo_id = db.Column(db.Ineger, nullable=False)


class Funcionario_habilidade(db.Model):
    __tablename__ = "funcionarios_habilidades" 
    funcionarios_id = db.Column(db.Integer, foreign_key=True)
    habilidades_id = db.Column(db.Integer, foreign_key=True)
    tempoExperiencia = db.Column(db.Integer, nullable=False)


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