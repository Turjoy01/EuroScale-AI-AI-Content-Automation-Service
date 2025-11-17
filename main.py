from fastapi import FastAPI
from routers import content

app = FastAPI(
    title="AI Content Automation Service",
    description="Generate sales scripts, promo content, descriptions, summaries + 25+ EU languages",
    version="1.0.0"
)

app.include_router(content.router)

@app.get("/")
async def root():
    return {"message": "AI Content Service is running! Go to /docs"}