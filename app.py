
from fastapi import FastAPI, Request, HTTPException
from schema import data_input
from ipynb.fs.full.main import predict_diabetes


app = FastAPI()

@app.post("/")
async def read_root(data: data_input):
    try:
        return predict_diabetes(data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness, data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)