from flask import Flask, render_template, request, jsonify, make_response
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, query, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.selectable import Select
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from flask_cors import CORS
import yaml
import json

app = Flask(__name__)
CORS(app)

# Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:7890@localhost/alokar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_CURSORCLASS'] = "DictCursor"

db = SQLAlchemy(app)


projetos_habilidades = db.Table('projetos_habilidades',
    db.Column('projetos.id', db.Integer, db.ForeignKey('projetos.id')),
    db.Column('habilidades.id', db.Integer, db.ForeignKey('habilidades.id'))
)

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
    
    projetos_habilidades = db.relationship('Habilidade', secondary='projetos_habilidades', lazy='dynamic')
    funcionarios = db.relationship("Funcionario", secondary="funcionarios_projetos")

class ProjectSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Projeto
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    custoPrevisto = fields.Number(required=True)
    area = fields.String(required=True)
    descricao = fields.String(required=True)
    otherCost = fields.Number(required=True)
    hardware = fields.Number(required=True)
    licenca = fields.Number(required=True)
    duracao = fields.String(required=True)
    status = fields.String(required=True)
    seatCharge = fields.Number(required=True)
    nomeEmpresa = fields.String(required=True)

class Habilidade(db.Model):
    __tablename__ = "habilidades" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)

    funcionarios = db.relationship("Funcionario", secondary="funcionarios_habilidades")

class HabilidadeSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Habilidade
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    

class Cargo(db.Model):
    __tablename__ = "cargos" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)

    


class CargoSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Cargo
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)


class Funcionario(db.Model):
    __tablename__ = "funcionarios" 
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(100), nullable=False, index=True)
    custoHora = db.Column(db.Numeric, nullable=False)
    quantProjetos = db.Column(db.Integer, nullable=False)
    disponibilidade = db.Column(db.String(45), nullable=False)
    custoHora_overtime = db.Column(db.String(45), nullable=True)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)

    habilidades = db.relationship("Habilidade", secondary="funcionarios_habilidades")
    projetos = db.relationship("Projeto", secondary="funcionarios_projetos")
    usuarios = db.relationship("Usuario", back_populates="funcionarios")
    cargo = db.relationship('Cargo', backref='funcionarios')

class FuncionarioSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Funcionario
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nomeCompleto = fields.String(required=True)
    custoHora = fields.Number(required=True)    
    quantProjetos = fields.Number(required=True)
    disponibilidade = fields.String(required=True)
    custoHora_overtime = fields.String(required=True)
    cargo_id = fields.Number(required=True)
    cargo = fields.String(required=True)
    

class Usuario(db.Model):
    __tablename__ = "usuarios" 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, index=True)
    email = db.Column(db.String(45), nullable=True, index=True)
    senha = db.Column(db.String(250), nullable=True)
    funcionarios_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'))
    funcionarios_cargo_id = db.Column(db.Integer, nullable=False)

    funcionarios = db.relationship("Funcionario", back_populates="usuarios")

class UsuarioSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Usuario
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    email = fields.String(required=True)    
    senha = fields.String(required=True)
    funcionarios_id = fields.Number(required=True)
    funcionarios_cargo_id = fields.Number(required=True)
    

class Funcionario_habilidade(db.Model):
    __tablename__ = "funcionarios_habilidades" 
    funcionarios_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), primary_key=True)
    habilidades_id = db.Column(db.Integer, db.ForeignKey('habilidades.id'), primary_key=True)
    tempoExperiencia = db.Column(db.String(45), nullable=False)
    
    habilidades = db.relationship("Habilidade", backref=backref("funcionarios_habilidades", cascade="all, delete-orphan"))
    funcionarios = db.relationship("Funcionario", backref=backref("funcionarios_habilidades", cascade="all, delete-orphan"))

class Funcionario_habilidadeSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Funcionario_habilidade
        sqla_session = db.session
    funcionarios_id = fields.Number(dump_only=True)
    habilidades_id = fields.Number(dump_only=True)   
    tempoExperiencia= fields.String(required=True)

class Funcionario_projeto(db.Model):
    __tablename__ = "funcionarios_projetos" 
    funcionarios_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), primary_key=True)
    projetos_id = db.Column(db.Integer, db.ForeignKey('projetos.id'), primary_key=True)
    overtime = db.Column(db.Integer, nullable=True)
    funcao = db.Column(db.String(45), nullable=True)
    
    projetos = db.relationship("Projeto", backref=backref("funcionarios_projetos", cascade="all, delete-orphan"))
    funcionarios = db.relationship("Funcionario", backref=backref("funcionarios_projetos", cascade="all, delete-orphan"))

class Funcionario_projetoSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Funcionario_projeto
        sqla_session = db.session
    funcionarios_id = fields.Number(dump_only=True)
    projetos_id = fields.Number(dump_only=True)   
    overtime = fields.Number(required=True)
    funcao = fields.String(required=True)

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
    

@app.route('/projects', methods=['GET'])
def projects(): 
    projetos = Projeto.query.all()
    projects_schema = ProjectSchema(many=True)
    projects = projects_schema.dump(projetos)
    
    return make_response(jsonify(projects))
    


@app.route('/projects/<int:id>', methods=['GET'])
def project_id(id):
    projeto = Projeto.query.filter_by(id=id)
    project_schema = ProjectSchema(many=True)
    project_id = project_schema.dump(projeto)
    
    return make_response(jsonify(project_id))

    
@app.route('/projects/<int:id>', methods=['PUT'])
def edit_project(id):
    projetos = Projeto()
    nome = request.json['nome']
    custoPrevisto = request.json['custoPrevisto']
    area = request.json['area']
    descricao = request.json['descricao']
    otherCost = request.json['otherCost']
    hardware = request.json['hardware']
    licenca = request.json['licenca']
    duracao = request.json['duracao']
    status = request.json['status']
    seatCharge = request.json['seatCharge']
    nomeEmpresa = request.json['nomeEmpresa']
    projeto = Projeto.query.get(id)

    if not projeto:
        return jsonify({'message':'nao existe'}), 404

    try:
        
        projeto.nome = nome
        projeto.custoPrevisto = custoPrevisto
        projeto.area = area
        projeto.descricao = descricao
        projeto.otherCost = otherCost
        projeto.hardware = hardware
        projeto.licenca = licenca
        projeto.duracao = duracao
        projeto.status = status
        projeto.seatCharge = seatCharge
        projeto.nomeEmpresa = nomeEmpresa
        db.session.commit()
        return jsonify({'message:':'Deu bom!'}), 201

    except:
        return 'Não foi possível realizar a ação!'

    



@app.route('/new_project', methods=['POST'])
def new_project():

    if request.method == 'POST':
        projetos = Projeto()
        projetos.nome = request.json['nome']
        projetos.custoPrevisto = request.json['custoPrevisto']
        projetos.area = request.json['area']
        projetos.descricao = request.json['descricao']
        projetos.otherCost = request.json['otherCost']
        projetos.hardware = request.json['hardware']
        projetos.licenca = request.json['licenca']
        projetos.duracao = request.json['duracao']
        projetos.status = request.json['status']
        projetos.seatCharge = request.json['seatCharge']
        projetos.nomeEmpresa = request.json['nomeEmpresa']
        
        db.session.add(projetos)
        db.session.commit()


    return make_response(jsonify({'message:':'Deu bom!'}))


        
    

    

@app.route('/employees')
def allocation():
    funcionarios = Funcionario.query.join(Cargo, Cargo.id == Funcionario.cargo_id)
    funcionarios_schema = FuncionarioSchema(many=True)
    employees = funcionarios_schema.dump(funcionarios)
    

    return make_response(jsonify(employees))

@app.route('/fh')
def fh(): 
    funcionario_habilidade = Funcionario_habilidade.query.all()
    f_h_schema = Funcionario_habilidadeSchema(many=True)
    fh = f_h_schema = f_h_schema.dump(funcionario_habilidade)

    return make_response(jsonify(fh))


@app.route('/allocation/<int:id>')
def employee_id(id):    
    funcionario = Funcionario.query.filter_by(id=id)
    funcionario_schema = FuncionarioSchema(many=True)
    employee = funcionario_schema.dump(funcionario)

    return make_response(jsonify(employee))

@app.route('/skills')
def skills():
    skills = Habilidade.query.all()
    skills_schema = HabilidadeSchema(many=True)
    habilidades = skills_schema.dump(skills)

    return make_response(jsonify(habilidades))


if __name__ == '__main__':
    app.run(debug=True)