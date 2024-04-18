import os
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
    # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = sqlalchemy.create_engine(db_url, echo=True)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)