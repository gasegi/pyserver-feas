from sqlalchemy.orm import Session

from sql.staff import Staff
from sql.staff_job import StaffJob


def initializeTestData(db: Session):
    objects = [
        Staff(staff_id=1, staff_number='user1', staff_name='鈴木',
              password='raFF41zUzpYwU', admin_flag=1, delete_flag=0),
        StaffJob(staff_id=1, job_id=1)
    ]
    db.bulk_save_objects(objects)
