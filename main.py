import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/excel-data")
def get_excel_data():
    df = pd.read_excel("users.xlsx")
    data = df.to_dict(orient="records")   # excel → JSON
    return {"data": data}
