from database import SessionLocal
from models import Company

# Import ATS plugins
# (We'll create these one by one.)
# from scrapers.greenhouse import scrape_greenhouse
# from scrapers.ashby import scrape_ashby
# from scrapers.lever import scrape_lever
# from scrapers.workable import scrape_workable

# Existing scraper
from scrapers.remoteok import scrape_remoteok


def run_all_scrapers(db):

    print("=" * 70)
    print("FinanceAI ATS Engine")
    print("=" * 70)

    total_jobs = 0

    # --------------------------------------------------
    # RemoteOK
    # --------------------------------------------------

    try:

        added = scrape_remoteok(db)

        print(f"[RemoteOK] {added} jobs imported")

        total_jobs += added

    except Exception as e:

        print(f"[RemoteOK] ERROR : {e}")

    # --------------------------------------------------
    # Company ATS Router
    # --------------------------------------------------

    companies = (
        db.query(Company)
        .filter(Company.active == True)
        .all()
    )

    print()
    print(f"Companies Loaded : {len(companies)}")
    print()

    ats_summary = {}

    for company in companies:

        ats = company.ats.strip()

        ats_summary.setdefault(ats, 0)
        ats_summary[ats] += 1

    print("Companies by ATS")
    print("-" * 70)

    for ats, count in sorted(ats_summary.items()):

        print(f"{ats:<20} {count}")

    print("-" * 70)

    #
    # ATS plugins will be called here
    #
    # Example:
    #
    # if ats == "Greenhouse":
    #     total_jobs += scrape_greenhouse(...)
    #

    print()
    print("=" * 70)
    print(f"TOTAL JOBS IMPORTED : {total_jobs}")
    print("=" * 70)

    return total_jobs