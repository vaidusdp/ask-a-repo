from fastapi import FastAPI 
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str 

app = FastAPI(
    title="Ask a Repo",
    description="A backend service to ingest and search GitHub repositories",
    version="1.0.0"
)

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="ask-a-repo"
    )