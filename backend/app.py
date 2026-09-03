from fastapi import FastAPI, UploadFile, File
2
from fastapi.responses import FileResponse
3
 
4
app = FastAPI()
5
 
6
@app.get("/")
7
def home():
8
return {"status": "Dining Production Sheet App"}
9
 
10
@app.post("/generate")
11
async def generate(file: UploadFile = File(...)):
12
return {"message": f"Received {file.filename}"}
