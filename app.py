from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Job
from scrapers.engine import run_all_scrapers

app = FastAPI(title="FinanceAI")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_dashboard_data():
    db: Session = SessionLocal()

    try:
        jobs = db.query(Job).all()

        total_jobs = len(jobs)

        remote_jobs = len([
            j for j in jobs
            if j.location and "remote" in j.location.lower()
        ])

        companies = len(set(
            j.company for j in jobs
            if j.company
        ))

        today_jobs = len([
            j for j in jobs
            if j.posted and "today" in str(j.posted).lower()
        ])

        return {
            "total_jobs": total_jobs,
            "remote_jobs": remote_jobs,
            "companies": companies,
            "today_jobs": today_jobs,
            "jobs": jobs
        }

    finally:
        db.close()


@app.get("/")
async def dashboard(request: Request):

    data = get_dashboard_data()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            **data
        }
    )


@app.get("/run-scrapers")
async def run_scrapers():

    db = SessionLocal()

    try:
        added = run_all_scrapers(db)
        print(f"Jobs Added : {added}")

    finally:
        db.close()

    return RedirectResponse(
        url="/",
        status_code=303
    )


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }