from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class ProspectStatement(Base):
    __tablename__ = "prospect_statement"

    statement_id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer)
    prospect_statement = Column(String)
    statement_type = Column(String)

class ProspectResponse(Base):
    __tablename__ = "prospect_response"

    response_id = Column(Integer, primary_key=True, index=True)
    statement_id = Column(Integer,ForeignKey("prospect_statement.statement_id"))
    response = Column(String)

class RepsQuestion(Base):
    __tablename__ = 'reps_question'

    org_id = Column(Integer)
    question_id = Column(Integer, primary_key=True, index=True)
    call_type = Column(String)
    question = Column(String)
