from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    FullName: str
    Phone: List[str]
    Email: List[str]
    Birthdate: str

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]

@app.post("/api/v1/contact")
@app.get("/api/v1/contact")
@app.put("/api/v1/contact")
@app.delete("/api/v1/contact")
def handle_contact(contact: Optional[Contact] = None):
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        FullName="",
        Phone=[],
        Email=[],
        Birthdate=""
    )

@app.post("/api/v1/group")
@app.get("/api/v1/group")
@app.put("/api/v1/group")
@app.delete("/api/v1/group")
def handle_group(group: Optional[Group] = None):
    return Group(
        ID=0,
        Title="",
        Description="",
        Contacts=[]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=6080)
