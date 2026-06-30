from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Job

app = FastAPI(title="FinanceAI")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def dashboard(request: Request):

    db: Session = SessionLocal()

    jobs = db.query(Job).all()

    total_jobs = len(jobs)

    remote_jobs = len(
        [j for j in jobs if j.location and "remote" in j.location.lower()]
    )

    companies = len(
        set(j.company for j in jobs if j.company)
    )

    today_jobs = len(
        [j for j in jobs if j.posted == "Today"]
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "total_jobs": total_jobs,
            "remote_jobs": remote_jobs,
            "companies": companies,
            "today_jobs": today_jobs,
            "jobs": jobs
        }
    )