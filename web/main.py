from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
app = FastAPI()

templates = Jinja2Templates(directory="/app")

@app.get("/")
async def start(request: Request):
    # client = MongoClient(host='db', port=27017, username='admin', password='root') 
    # client = MongoClient(host='db', port=27017) 
    client = MongoClient('mongodb://db:27017/')

    db = client["airport"]
    collection = db["plane"]
    collection.insert_one({
        "code":1,
        "name":"boeing",
        "country":"USA",
        "lastCheckUpDate":"02.04.2018"
    })

    data = list(collection.find())

    return templates.TemplateResponse("index.html", {"request": request, "data": data})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)