from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(250))
    company = Column(String(250))
    location = Column(String(250))

    salary = Column(String(100))

    source = Column(String(100))

    job_type = Column(String(100))

    experience = Column(String(100))

    tags = Column(String(500))

    description = Column(Text)

    url = Column(String(1000), unique=True)

    posted = Column(String(100))