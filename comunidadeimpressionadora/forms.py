from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro email ou faça login para continuar.')

    def validate_username(self, username):
        username = Usuario.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('Nome de Usuário já cadastrado. Cadastre-se com outro nome de usuário.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    curso_python = BooleanField('Python')
    curso_htmlcss = BooleanField('HTML & CSS')
    curso_sql = BooleanField('SQL')
    curso_javascript = BooleanField('JavaScript')
    curso_vba = BooleanField('VBA')
    curso_excel = BooleanField('Excel')
    curso_powerbi = BooleanField('Power BI')
    curso_powerpoint = BooleanField('PowerPoint')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        # Verificar se o usuário mudou de email
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail.')

    def validate_username(self, username):
        # Verificar se o usuário mudou de nome de usuário
        if current_user.username != username.data:
            username = Usuario.query.filter_by(username=username.data).first()
            if username:
                raise ValidationError('Já existe um usuário com esse nome. Cadastre-se com outro nome de usuário.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
