from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'usuarios'
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'senha': self.senha
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