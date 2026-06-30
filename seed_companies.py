import csv
import os

from database import SessionLocal
from models import Company

DATA_FOLDER = "data"
CSV_FILE = os.path.join(DATA_FOLDER, "companies.csv")


def to_bool(value):
    return str(value).strip().upper() == "TRUE"


def seed_companies():

    if not os.path.exists(CSV_FILE):
        print(f"ERROR: {CSV_FILE} not found.")
        return

    db = SessionLocal()

    added = 0
    skipped = 0

    try:

        with open(CSV_FILE, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                company_name = row["company_name"].strip()

                exists = (
                    db.query(Company)
                    .filter(Company.company_name == company_name)
                    .first()
                )

                if exists:
                    skipped += 1
                    continue

                company = Company(

                    company_name=company_name,

                    ats=row["ats"].strip(),

                    career_url=row["career_url"].strip(),

                    remote=to_bool(row["remote"]),

                    india=to_bool(row["india"]),

                    finance=to_bool(row["finance"]),

                    active=True,

                    last_scan=""

                )

                db.add(company)

                added += 1

        db.commit()

        print()
        print("=" * 70)
        print("FinanceAI Company Seeder")
        print("=" * 70)
        print(f"Companies Added   : {added}")
        print(f"Companies Skipped : {skipped}")
        print("=" * 70)

    finally:

        db.close()


if __name__ == "__main__":
    seed_companies()