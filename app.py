from flask import Flask, render_template, request, jsonify, make_response
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, query, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.selectable import Select
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
import yaml
import json

app = Flask(__name__)


# Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:doninha20@localhost/mydb"
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

    funcionarios = db.relationship('Funcionario', backref='cargos')


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
    funcionarios_cargo_id = fields.Number(dump_only=True)   
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
    

@app.route('/projects', methods=['GET', 'POST'])
def projects(): 
    projetos = Projeto.query.all()
    projects_schema = ProjectSchema(many=True)
    projects = projects_schema.dump(projetos)
    
    return make_response(jsonify({'projects': projects}))
    


@app.route('/projects/<int:id>', methods=['GET'])
def project_id(id):
    projeto = Projeto.query.filter_by(id=id)
    project_schema = ProjectSchema(many=True)
    project_id = project_schema.dump(projeto)
    return make_response(jsonify({'project_id': project_id}))

    
@app.route('/projects/<int:id>', methods=['PUT'])
def edit_project(id):
    projeto = Projeto.query.filter_by(id=id)
    project_schema = ProjectSchema(many=True)
    project_id = project_schema.dump(projeto)

    try:
        if ('nome' in projeto):
            projeto.nome = request.form['nome']
        if ('custoPrevisto' in projeto):
            projeto.custoPrevisto = request.form['custoPrevisto']
        if ('custoPrevisto' in projeto):
            projeto.area = request.form['custoPrevisto']
        if ('descricao' in projeto):
            projeto.descricao = request.form['descricao']
        if ('otherCost' in projeto):
            projeto.otherCost = request.form['otherCost']
        if ('hardware' in projeto):
            projeto.hardware = request.form['hardware']
        if ('licenca' in projeto):
            projeto.licenca = request.form['licenca']
        if ('duracao' in projeto):
            projeto.duracao = request.form['duracao']
        if ('status' in projeto):
            projeto.status = request.form['status']
        if ('seatCharge' in projeto):
            projeto.seatCharge = request.form['seatCharge']
        if ('nomeEmpresa' in projeto):
            projeto.nomeEmpresa = request.form['nomeEmpresa']

        db.session.add(projeto)
        db.session.commit()

    except:
        return 'Não foi possível realizar a ação!'

    return make_response(jsonify({'project_id': project_id}))



@app.route('/new_project', methods=['GET', 'POST'])
def new_project():

    skills = Habilidade.query.all()
    skill = Habilidade.query.get(id)
    skill_schema = HabilidadeSchema(many=True)
    habilidades = skill_schema.dump(skills)
    habilidade = skill_schema.dump(skill)

    funcoes = Cargo.query.all()
    funcoes_schema = CargoSchema(many=True)
    fun = funcoes_schema.dump(funcoes)

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
        
    

    return make_response(jsonify({'skills': habilidades}, {'funcoes': fun}))




@app.route('/allocation')
def allocation():
    funcionarios = Funcionario.query.all()
    return render_template('allocation.html', funcionarios=funcionarios)

    






if __name__ == '__main__':
    app.run(debug=True)