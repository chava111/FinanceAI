from scrapers.remoteok import scrape_remoteok


def run_all_scrapers(db):

    print("=" * 60)
    print("FinanceAI Scraper Engine")
    print("=" * 60)

    total_added = 0

    try:
        added = scrape_remoteok(db)

        print(f"RemoteOK : {added} new jobs")

        total_added += added

    except Exception as e:
        print(f"RemoteOK Error : {e}")

    print("-" * 60)
    print(f"Total Jobs Added : {total_added}")
    print("=" * 60)

    return total_added