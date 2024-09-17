from flask_login import UserMixin
import sqlite3

BANCO = 'database.db'
def obter_conexao():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn

# classe python - Modelo (acessa o banco)
class User(UserMixin):
    id : str
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    
    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE id=?'
        dados = conexao.execute(SELECT, (id,)).fetchone()
        user = User(dados['email'], dados['senha'])
        user.id = dados['id']
        return user

    @classmethod
    def get_by_email(cls, email):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE email=?'
        dados = conexao.execute(SELECT, (email,)).fetchone()
        if dados:    
            user = User(dados['email'], dados['senha'])
            user.id = dados['id']
            return user
        return None