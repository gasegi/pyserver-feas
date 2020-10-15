from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base


class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column("staff_id", Integer, primary_key=True,
                      index=True, nullable=False)
    staff_number = Column("staff_number", String(10), nullable=False)
    staff_name = Column("staff_name", String(64), unique=True, nullable=False)
    password = Column("password", String(255), nullable=False)
    admin_flag = Column("admin_flag", Boolean(1), nullable=False)
    delete_flag = Column("delete_flag", Boolean(1), nullable=False)


login_sql = """
SELECT 
    staff_number
  , staff_name
  , password
  , admin_flag 
FROM 
    staff
WHERE 
    staff.staff_number='{0}' 
AND 
    staff.delete_flag=0
"""

# , job_id

# LEFT JOIN
#     staff_job
# ON
#     staff.staff_id=staff_job.staff_id
