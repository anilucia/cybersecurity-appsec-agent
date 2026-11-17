"""EXEMPLO INSEGURO APENAS PARA ANÁLISE ESTÁTICA E LABORATÓRIO.
Banco em memória com dados fictícios. Nunca use em produção.
"""
import sqlite3


def create_database():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE users (username TEXT, password TEXT)")
    con.execute("INSERT INTO users VALUES (?, ?)", ("aluno", "senha-ficticia"))
    return con


def authenticate(con, username, password):
    query = (
        f"SELECT username FROM users WHERE username = '{username}' "
        f"AND password = '{password}'"
    )
    return con.execute(query).fetchone() is not None


if __name__ == "__main__":
    db = create_database()
    print("Login de laboratorio (dados ficticios).")
    print(authenticate(db, input("Usuario: "), input("Senha: ")))
    db.close()
