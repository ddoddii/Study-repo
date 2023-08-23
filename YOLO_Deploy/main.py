from typing import Union

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn
import datetime

from prediction import read_imagefile, predict

app = FastAPI()


@app.get("/")
def hello_world(name:str):
    return f"Hello I'm {name}"

@app.post("/api/predict")
def predict_image(file: UploadFile = File(...)):
    # Read file 
    image = read_imagefile(file)
    
    prediction = predict(image)

    return prediction
    


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)