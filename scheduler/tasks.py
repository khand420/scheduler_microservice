


# jobs/tasks.py

from celery import shared_task
from .models import Job
from datetime import datetime
import time

@shared_task
def execute_job(job_id):
    job = Job.objects.get(id=job_id)
    job.last_run = datetime.now()
    job.save()
    # Here you would implement the actual job logic (e.g., sending an email)
    print(f"Executing job: {job.name}")



@shared_task
def schedule_job(job_id):
    try:
        job = Job.objects.get(id=job_id)
        # Simulate scheduling job logic here, for example:
        print(f"Scheduling job {job.name} to run as per the schedule {job.schedule}")
        # You can implement actual scheduling logic here based on your requirement
        # Example: time.sleep(10) to simulate a task taking 10 seconds to complete
        time.sleep(10)
        job.last_run = datetime.now()
        job.save()
    except Job.DoesNotExist:
        print(f"Job with id {job_id} does not exist.")



        
# @shared_task
# def schedule_job(job_id):
#     job = Job.objects.get(id=job_id)
#     # Pseudo code for scheduling - in practice, you might use something like Celery's periodic task system
#     if job.schedule == "every Monday at 10:00 AM":
#         while True:
#             current_time = datetime.now().strftime('%A %H:%M')
#             if current_time == "Monday 10:00":
#                 execute_job.delay(job_id)
#                 time.sleep(60)  # Sleep for a minute to avoid multiple triggers




# @shared_task
# def execute_job(job_id):
#     job = Job.objects.get(id=job_id)
#     # Dummy job logic (e.g., sending an email or processing data)
#     print(f"Executing job: {job.name}")
#     # Update last_run and next_run
#     job.last_run = timezone.now()
#     job.save()