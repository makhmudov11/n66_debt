from core.database_settings import execute_query

users = """
           CREATE TABLE IF NOT EXISTS users
           (
               id SMALLSERIAL PRIMARY KEY,
               username VARCHAR(50) NOT NULL CHECK (LENGTH(username) >= 5),
               password VARCHAR(30) NOT NULL CHECK (LENGTH(password) >= 8)
           );
           """
debts = """

    CREATE TABLE IF NOT EXISTS debts (
    id SMALLSERIAL PRIMARY KEY,
    from_user SMALLINT,
    to_user SMALLINT,
    date TIMESTAMP,
    status BOOLEAN,
    FOREIGN KEY (from_user) REFERENCES users(id),
    FOREIGN KEY (to_user) REFERENCES users(id)
    );
    """

def initializing_tables():
    execute_query(query=users)
    execute_query(query=debts)
