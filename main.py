from typing import Optional
import numpy as np
import uvicorn
from fastapi import FastAPI, Depends,Request
from fastapi.templating import  Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics.pairwise import cosine_similarity
from starlette.routing import Route
from pydantic import BaseModel
from sqlalchemy.orm import Session
# from source import embed
import models
import schemas
from database import engine, SessionLocal



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()
models.Base.metadata.create_all(engine)


# def get_most_matching_text(text,ids,known_phrases):
#
#     # Universal sentence encoder
#     embeddings = embed(known_phrases)
#     sentence_vec = embed([text])
#     sims = cosine_similarity(
#         sentence_vec,
#         embeddings)
#     idx = np.argmax(sims)
#     phrase_id = ids[idx]
#     score = round(sims[0][idx],3)
#     match=known_phrases[idx]
#     return phrase_id,match,score






@app.post("/addStatement")
def prospects_statement(statement : schemas.ProspectPage,db: Session = Depends(get_db)):
    print("here")
    s = models.ProspectStatement(org_id=statement.org_id,
                                   prospect_statement=statement.prospect_statement,statement_type = statement.statement_type)
    db.add(s)
    db.flush()
    for response in statement.responses:
        obj = models.ProspectResponse(statement_id=s.statement_id,response=response)
        db.add(obj)
    db.commit()
    return True

# @app.get("/matchResponse/")
# def get_mathing_response(org_id:int,text:str,db:Session=Depends(get_db)):
#     objections = db.query(models.ProspectStatement).filter(models.ProspectStatement.org_id == org_id).all()
#     ids = [row.statement_id for row in objections]
#     known_phrases = [row.prospect_statement for row in objections]
#     statement_id,match,score = get_most_matching_text(text,ids,known_phrases)
#     result = db.query(models.ProspectResponse).filter(models.ProspectResponse.statement_id==statement_id).all()
#     responses = [row.response for row in result]
#     return {"responses": responses}

@app.post("/addQuestion")
def reps_question(question : schemas.RepsPage,db: Session = Depends(get_db)):
    s = models.RepsQuestion(org_id=question.org_id,call_type=question.call_type,
                                   question=question.question,)
    db.add(s)
    db.commit()
    return True

# @app.get("/matchQuestion/")
# def get_mathing_question(org_id:int,text:str,db:Session=Depends(get_db)):
#     questions = db.query(models.RepsQuestion).filter(models.RepsQuestion.org_id == org_id).all()
#     ids = [row.question_id for row in questions]
#     known_phrases = [row.question for row in questions]
#     question_id, match, score = get_most_matching_text(text, ids, known_phrases)
#     return {"question_id": question_id}

@app.get("/allQuestions/{org_id}")
def get_all_question(org_id:int,db:Session=Depends(get_db)):
    questions = db.query(models.RepsQuestion).filter(models.RepsQuestion.org_id == org_id).all()
    return questions

@app.get('/')
def index():
    return {"Response": "Hello world"}
# @app.post("/transcription")
# def run_transcription(request: schemas.TranscriptionReq, db:Session=Depends(get_db)):
#     if request.user_type == "sales_rep":
#         questions  = get_mathing_question(request.org_id,request.text,db)
#         return questions
#     else :
#         responses= get_mathing_response(request.org_id, request.text, db)
#         return responses

if __name__ == '__main__':
    uvicorn.run(app)