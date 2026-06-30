import requests
from models import Job


URL = "https://remoteok.com/api"


def scrape_remoteok(db):

    added = 0

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(URL, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()

    except Exception as e:
        print(e)
        return 0

    for item in data:

        if not isinstance(item, dict):
            continue

        title = item.get("position", "")

        if title == "":
            continue

        keywords = [
            "finance",
            "account",
            "fp&a",
            "controller",
            "analyst",
            "bookkeeper",
            "audit",
            "treasury"
        ]

        if not any(k in title.lower() for k in keywords):
            continue

        url = item.get("url", "")

        exists = db.query(Job).filter(Job.url == url).first()

        if exists:
            continue

        job = Job(
            title=title,
            company=item.get("company", ""),
            location=item.get("location", "Remote"),
            salary=str(item.get("salary", "")),
            source="RemoteOK",
            job_type="Remote",
            experience="",
            tags=",".join(item.get("tags", [])),
            description=item.get("description", ""),
            url=url,
            posted=str(item.get("date", ""))
        )

        db.add(job)
        added += 1

    db.commit()

    return added