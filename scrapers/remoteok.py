import requests
import html

from models import Job

URL = "https://remoteok.com/api"


def scrape_remoteok(db):

    total_added = 0

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(
            URL,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        jobs = response.json()

    except Exception as e:
        print(f"RemoteOK Request Error : {e}")
        return 0

    keywords = [
        "finance",
        "account",
        "accountant",
        "fp&a",
        "financial",
        "controller",
        "audit",
        "bookkeeper",
        "treasury",
        "payroll",
        "tax"
    ]

    for item in jobs:

        if not isinstance(item, dict):
            continue

        title = html.unescape(
            str(item.get("position", "")).strip()
        )

        if title == "":
            continue

        if not any(word in title.lower() for word in keywords):
            continue

        url = item.get("url", "")

        if url == "":
            continue

        exists = db.query(Job).filter(Job.url == url).first()

        if exists:
            continue

        job = Job(

            title=title,

            company=html.unescape(
                str(item.get("company", ""))
            ),

            location=html.unescape(
                str(item.get("location", "Remote"))
            ),

            salary=str(item.get("salary", "")),

            source="RemoteOK",

            job_type="Remote",

            experience="",

            tags=",".join(item.get("tags", [])),

            description=html.unescape(
                str(item.get("description", ""))
            ),

            url=url,

            posted=str(item.get("date", ""))

        )

        db.add(job)

        total_added += 1

    db.commit()

    return total_added