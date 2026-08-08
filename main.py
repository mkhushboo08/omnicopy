from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Request, Response
from typing import Any
app = FastAPI(root_path="/api/v1")

@app.get("/")
async def root():
  return{"message": "Hello World"}

data : Any= [
  {
    "campaign_id" : 1,
    "name" : "Summer Launch",
    "due_date" : datetime.now(),
    "created_at" : datetime.now()
  },
  {
    "campaign_id" : 2,
    "name" : "Black Friday",
    "due_date" : datetime.now(),
    "created_at" : datetime.now()
  }
]

@app.get("/campaigns")
async def get_campaigns():
  return {"campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaigns(id: int):
  for campaign in data:
    if campaign.get("campaign_id") == id:
      return {"campaigns": campaign}
  raise HTTPException(status_code=404)

@app.post("/campaigns", status_code=201)
async def create_campaign(body: dict[str, Any]):
  new = {
    "campaign_id" : randint(100,200),
    "name" : body.get("name"),
    "due_date" : body.get("due_date"),
    "created_at" : datetime.now()
  }

  data.append(new)
  return {"campaign" : new }

@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):

  for index, comapaign in enumerate(data):
    if comapaign.get("compaign_id") == id:
      updated : Any = {
        "campaign_id" : id,
        "name" : body.get("name"),
        "due_date" : body.get("due_date"),
        "created_at" : comapaign.get("created_at")
      }
      data[index] = updated
      return {"compaign" : updated}
  raise HTTPException(status_code=404)


@app.delete("/campaign/{id}")
async def update_compaign(id: int):
  for index, campaign in enumerate(data):
    if campaign.get("campaign_id") == id:
      data.pop(index)
      return Response(status_code=204)
  raise HTTPException(status_code=404)