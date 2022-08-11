from typing import List

from pydantic import BaseModel

class ProspectPage(BaseModel):
        org_id : int
        prospect_statement : str
        statement_type : str
        responses : List[str]
class RepsPage(BaseModel):
        org_id:int
        call_type : str
        question : str

class TranscriptionReq(BaseModel):
        call_id : int
        org_id: int
        user_type : str
        text : str
