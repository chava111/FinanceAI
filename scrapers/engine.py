from scrapers.remoteok import scrape_remoteok


def run_all_scrapers(db):

    total = 0

    total += scrape_remoteok(db)

    return total