"""Correção educacional: consultas parametrizadas. Não é autenticação de produção."""
import sqlite3


def create_database():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE users (username TEXT, password TEXT)")
    con.execute("INSERT INTO users VALUES (?, ?)", ("aluno", "senha-ficticia"))
    return con


def authenticate(con, username, password):
    query = "SELECT username FROM users WHERE username = ? AND password = ?"
    return con.execute(query, (username, password)).fetchone() is not None


if __name__ == "__main__":
    db = create_database()
    print("Login de laboratorio corrigido (dados ficticios).")
    print(authenticate(db, input("Usuario: "), input("Senha: ")))
    db.close()
