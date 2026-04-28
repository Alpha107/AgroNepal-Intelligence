from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ml_pipeline import recommender

app = FastAPI(
    title="AgroNepal API",
    description="Backend API for AgroNepal Agricultural Intelligence Dashboard",
    version="1.0.0"
)

# Configure CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to the frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AgroNepal API", "status": "healthy"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/districts")
def get_districts():
    import os
    import json
    from fastapi import HTTPException
    
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'nepal_districts.geojson')
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="GeoJSON data not found")
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

@app.get("/api/insights/{district_name}")
def get_district_insights(district_name: str):
    return recommender.get_insights(district_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

