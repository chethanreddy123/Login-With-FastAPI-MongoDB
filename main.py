from pymongo.mongo_client import MongoClient


client = MongoClient("mongodb+srv://chethanreddy2002:12345@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority")
Data = client['Test']
myData = Data['Test']

from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/create_account")
async def getInformation(info : Request):
    req_info = await info.json()

    UserName = req_info['UserName']
    Password = req_info['Password']
    Email = req_info['Email']

    myData.insert_one({
        "UserName" : UserName,
        "Password" : Password,
        "Email" : Email
    })


    return {
        "status" : "SUCCESS"
    }

@app.post("/check_account")
async def getInformation(info : Request):
    req_info = await info.json()
    UserName = req_info['UserName']
    PassWord = req_info['Password']

    if UserName == None:
        return {"Status" : "false"}
    if PassWord == None:
        return {"Status" : "false"}
    
    myquery = { "UserName" : UserName}
    status = myData.find_one(myquery)
    if status == None:
        return {"Status" : "false"}
    
    if status['Password'] == PassWord:
        return {"Status" : "true"}
    else:
        return {"Status" : "false"}