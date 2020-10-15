
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
