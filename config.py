import os
from dotenv import load_dotenv

load_dotenv()

# ----------------------------------------------------
# APPLICATION
# ----------------------------------------------------

APP_NAME = "FinanceAI"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///financeod.db"
)

# ----------------------------------------------------
# CHROME
# ----------------------------------------------------

CHROME_EXECUTABLE = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

CHROME_USER_DATA = r"C:\Users\veeru\AppData\Local\Google\Chrome\User Data"

CHROME_PROFILE = "Default"

HEADLESS = False

# ----------------------------------------------------
# JOB SEARCH
# ----------------------------------------------------

SEARCH_KEYWORDS = [

    "Finance Manager",

    "Senior Accountant",

    "Financial Analyst",

    "FP&A",

    "Accounting Manager",

    "General Ledger",

    "Record to Report",

    "Accounts Payable",

    "Accounts Receivable",

    "Finance Business Partner"

]

LOCATION = "Remote"

MAX_PAGES = 10

WAIT_TIME = 2

# ----------------------------------------------------
# EXPORT
# ----------------------------------------------------

EXPORT_FOLDER = "exports"