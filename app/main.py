from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from .mock_data import get_instantly_data, get_google_ads_data, get_meta_ads_data
from .schemas import AnalyticsRequest

app = FastAPI(title="Marketing Analytics API")
api_key_header = APIKeyHeader(name="X-API-Key")
limiter = Limiter(key_func=get_remote_address)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/api/analytics")
@limiter.limit("10/minute")
async def get_analytics(
    request: Request,
    params: AnalyticsRequest,
    api_key: str = Depends(api_key_header)
):
    if api_key != "secure-key-123":
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    try:
        # Агрегація даних з валідацією
        return {
            "instantly": get_instantly_data(params.start_date),
            "google_ads": get_google_ads_data(params.campaign_ids),
            "meta_ads": get_meta_ads_data(params.metrics)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)