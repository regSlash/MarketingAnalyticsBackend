def get_instantly_data():
    return {
        "campaigns": [
            {"id": 1, "name": "Summer Sale", "open_rate": 0.25},
            {"id": 2, "name": "Winter Special", "open_rate": 0.32}
        ],
        "metrics": {
            "total_campaigns": 2,
            "average_open_rate": 0.285
        }
    }

def get_google_ads_data():
    return {
        "campaign_performance": [
            {"id": 101, "clicks": 150, "cost": 300, "conversions": 15},
            {"id": 102, "clicks": 200, "cost": 450, "conversions": 20}
        ],
        "cpc": 2.5,
        "roi": 1.8
    }

def get_meta_ads_data():
    return {
        "audience_insights": {
            "age_range": "18-35",
            "locations": ["USA", "Canada"]
        },
        "engagement": {
            "likes": 1200,
            "shares": 300,
            "comments": 150
        },
        "roi": 3.2
    }