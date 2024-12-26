from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHAMY_DATABASE_URL = 'sqlite:/// ./blog.db'
# SQLALCHAMY_DATABASE_URL = "mysql+pymysql://{db_username}:{db_password}@localhost:3306/{db_name}"

SQLALCHAMY_DATABASE_URL = "mysql+pymysql://root:Mysql#497@localhost:3306/fastapidb"

# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args= {'check_same_thread':False} )
engine = create_engine(SQLALCHAMY_DATABASE_URL, echo= True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()