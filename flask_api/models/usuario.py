from email.policy import default

from flask import url_for
from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'usuarios'
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40), nullable=False, unique=True)
    senha = banco.Column(banco.String(40))
    email = banco.Column(banco.String(80), nullable=False, unique=True)
    ativado = banco.Column(banco.Boolean, default=False)

    def __init__(self, login, senha, email, ativado):
        self.login = login
        self.senha = senha
        self.email = email
        self.senha = ativado
        
    def send_confirmation_email(self):
        #http://127.0.0.1:5000 + #/confirmacao/{user_id}
        link = request.url_root[:-1] + url_for('userconfirm', user_id= self.user_id) 
        

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'senha': self.senha,
            'email': self.email,
            'ativado': self.ativado,
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return False        

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def remove_user(self):
        banco.session.delete(self)
        banco.session.commit()
    @classmethod
    def find_by_login(cls, login):
        user_login = cls.query.filter_by(login = login).first()
        if user_login: 
            return user_login
        return False

