from fastapi import FastAPI 
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str 

class IngestRequest(BaseModel):
    repo_url: str
    branch: str | None=None

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

@app.post("/ingest-preview")
def ingest_preview(request: IngestRequest) -> dict[str, str | None]:
    return {
        "repo_url": request.repo_url,
        "branch": request.branch,
    }