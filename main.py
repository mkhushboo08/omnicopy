from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Response
from typing import Any

# This create FastAPI Application 
app = FastAPI(root_path="/api/v1")

@app.get("/") # decorator
async def root():
  return{"message": "Hello World"}

# teporary database
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

# Get all campaigns
@app.get("/campaigns")
async def get_campaigns():
  return {"campaigns": data}

# Get one campaigns
@app.get("/campaigns/{id}") # {id}: path parameter
async def read_campaigns(id: int):
  for campaign in data:
    if campaign.get("campaign_id") == id:
      return {"campaigns": campaign}
  raise HTTPException(status_code=404) # 404: Not Found

# Create a campaign
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


# Update a campaign
@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):

  for index, compaign in enumerate(data):
    if compaign.get("campaign_id") == id:
      updated : Any = {
        "campaign_id" : id,
        "name" : body.get("name"),  #new name from request 
        "due_date" : body.get("due_date"), #new due date from request
        "created_at" : compaign.get("created_at")
      }
      data[index] = updated
      return {"compaign" : updated}
  raise HTTPException(status_code=404)

# Delete a campaign
@app.delete("/campaign/{id}")
async def update_compaign(id: int):
  for index, campaign in enumerate(data):
    if campaign.get("campaign_id") == id:
      data.pop(index)
      return Response(status_code=204)
  raise HTTPException(status_code=404)

  