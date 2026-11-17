
import sqlite3


def create_database():
    connection = sqlite3.connect(":memory:")

    connection.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        [
            ("admin", "admin123"),
            ("developer", "dev123"),
            ("guest", "guest123"),
        ]
    )

    connection.commit()
    return connection


def authenticate(connection, username, password):
    # Consulta construída com dados externos.
    query = (
        f"SELECT id, username FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    cursor = connection.execute(query)
    return cursor.fetchone()


def main():
    connection = create_database()

    try:
        username = input("Usuário: ")
        password = input("Senha: ")

        user = authenticate(connection, username, password)

        if user:
            print(f"Autenticado: {user[1]}")
        else:
            print("Credenciais inválidas.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()
