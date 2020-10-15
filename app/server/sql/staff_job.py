from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base


class StaffJob(Base):
    __tablename__ = "staff_job"

    staff_id = Column("staff_id", Integer, primary_key=True, index=True)
    job_id = Column("job_id", Integer, index=True)
