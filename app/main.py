from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from .mock_data import get_instantly_data, get_google_ads_data, get_meta_ads_data

app = FastAPI(title="Marketing Analytics API")

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

@app.get("/api/analytics")
@limiter.limit("10/minute")
async def get_analytics(request: Request):
    try:
        return {
            "instantly": get_instantly_data(),
            "google_ads": get_google_ads_data(),
            "meta_ads": get_meta_ads_data()
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching analytics: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)