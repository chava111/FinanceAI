from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Job

from scrapers.engine import run_all_scrapers

app = FastAPI(title="FinanceAI")


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "FinanceAI Started Successfully"
    }


@app.get("/jobs")
def jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    return {
        "count": len(jobs),
        "jobs": jobs
    }


@app.get("/scrape")
def scrape(db: Session = Depends(get_db)):

    added = run_all_scrapers(db)

    return {
        "jobs_added": added
    }