from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://msnuhvgdioxspt:2734aa13537f8d43ed5d2d100a83178b02a25d3052ad9113dc1c91fa0d28c405@ec2-3-225-110-188.compute-1.amazonaws.com:5432/dc0futgm0ntmaq"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

