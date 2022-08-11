import json
import requests

def add_prospect_data():
    objections = json.load(open(r"C:\Users\aswan\Work\Datamoo\PhraseComparison\Docs\objections.json","r",encoding="utf-8"))
    answers = json.load(open(r"C:\Users\aswan\Work\Datamoo\PhraseComparison\Docs\answers.json","r",encoding="utf-8"))

    for key in objections.keys():
        client_id = 1 if int(key) <5 else 2
        payload = {
      "org_id":client_id,
      "prospect_statement": objections[key],
      "statement_type": "objection",
      "responses": answers[key],
    }
        requests.post(url="http://127.0.0.1:8000/addStatement",json=payload,)

def add_sales_rep_data():
    path = r"C:\Users\aswan\Work\Datamoo\PhraseComparison\Docs\questions.txt"
    with open(path,"r") as file:
        questions= file.read().splitlines()
        half = len(questions)//2
        for idx,question in enumerate(questions):
            client_id = 1 if idx < half else 2
            call_type = "discovery" if idx < ((client_id-1) * 10)+(half//2) else "follow_up"
            payload = {
                  "org_id": client_id,
                  "call_type": call_type,
                "question": question
                }
            requests.post(url="http://127.0.0.1:8000/addQuestion/", json=payload, )

if __name__ == "__main__":
    add_sales_rep_data()

