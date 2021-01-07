from fastapi import FastAPI
from pymongo import MongoClient
import creds
import pandas as pd

client = MongoClient(creds.mongodb_uri, creds.port) #mongodb connection
db = client['emaily-prod'] #enter database name
col=db['fast-api'] #enter collection name

# load csv data into pandas dataframe and convert it to dictionary records
df=pd.read_csv("neet.csv")
df=df.to_dict('records')
# print(df)

app = FastAPI()

# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}

# endpoint to insert airtable data into mangoDB collection
@app.post("/insert")
def insert():
    for i in df:
        col.insert_one(i)
    return {"message":"successfully inserted airtable!"}

# endpoint to stop process and delete whatever has been inserted in database
@app.post("/stop")
def stop():
    c=0
    for i in col.find():
        col.delete_one(i)
        c+=1
    return {"message":"Application stopped at " + str(c) + " insertions/deletions."}

# endpoint to delete airtable data from mongoDB collection
@app.post("/delete")
def delete_csv():
    for item in col.find():
        if('ques' in item):
            col.delete_one(item)
    return {"message":"successfully deleted airtable!"}
