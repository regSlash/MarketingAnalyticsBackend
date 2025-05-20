from pydantic import BaseModel

class AnalyticsRequest(BaseModel):
    start_date: str
    end_date: str
    metrics: list[str]
    campaign_ids: list[int] = []