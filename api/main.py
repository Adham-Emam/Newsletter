from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
# Path to the JSON file in the parent directory
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "news_scrapper", "data.json")


class Article(BaseModel):
    url: str
    title: str
    last_updated: str
    image_url: str
    body: str


@app.get("/data")
async def read_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                raw_data = file.read()
                data = json.loads(raw_data)  # Use json.loads to catch errors
                return data
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Error decoding JSON")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Server error: {e}")
    else:
        raise HTTPException(status_code=404, detail="Data file not found")


@app.get("/")
async def index():
    return {"message": "Welcome to the API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
