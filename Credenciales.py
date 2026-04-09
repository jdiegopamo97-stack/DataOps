import sqlalchemy
from sqlalchemy import create_engine


def conexion_repo_final():
    SERVER = r'LAPTOP-9194SAIK'
    DATABASE = 'repo_final'
    DRIVER = 'ODBC+Driver+17+for+SQL+Server'
    connection_url = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
    con = create_engine(connection_url)

    return con
