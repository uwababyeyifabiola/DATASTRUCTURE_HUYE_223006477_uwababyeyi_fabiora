# Remote Job Board: Stack for undoing job applications, queue for job postings, and list for  available job opportunities.
from collections import deque

class RemoteJobBoard:
    def __init__(self):
        # Stack to store applied jobs for undoing
        self.applied_jobs_stack = []
        
        # Queue to store job postings (FIFO)
        self.job_postings_queue = deque()
        
        # List to store all available job opportunities
        self.available_jobs = []
    
    # Add a job posting to the queue
    def post_job(self, job):
        self.job_postings_queue.append(job)
        self.available_jobs.append(job)
        print(f"New job posted: {job}")
    
    # Process job posting from the queue (job goes live)
    def process_job_posting(self):
        if self.job_postings_queue:
            job = self.job_postings_queue.popleft()
            print(f"Job '{job}' is now live.")
        else:
            print("No job postings to process.")
    
    # Apply for a job (moves from available jobs to applied stack)
    def apply_for_job(self, job):
        if job in self.available_jobs:
            self.available_jobs.remove(job)
            self.applied_jobs_stack.append(job)
            print(f"Applied for job: {job}")
        else:
            print(f"Job '{job}' is not available.")
    
    # Undo the last job application
    def undo_last_application(self):
        if self.applied_jobs_stack:
            job = self.applied_jobs_stack.pop()
            self.available_jobs.append(job)
            print(f"Undo application for job: {job}")
        else:
            print("No applications to undo.")
    
    # Display all available jobs
    def display_available_jobs(self):
        if self.available_jobs:
            print("Available jobs:")
            for job in self.available_jobs:
                print(f"- {job}")
        else:
            print("No available jobs at the moment.")
    
    # Display applied jobs
    def display_applied_jobs(self):
        if self.applied_jobs_stack:
            print("Jobs you have applied for:")
            for job in self.applied_jobs_stack:
                print(f"- {job}")
        else:
            print("You haven't applied for any jobs yet.")

# Example usage:

job_board = RemoteJobBoard()

# Posting jobs
job_board.post_job("Software Engineer")
job_board.post_job("Data Scientist")
job_board.post_job("DevOps Engineer")

# Process job postings (they go live)
job_board.process_job_posting()
job_board.process_job_posting()

# Display available jobs
job_board.display_available_jobs()

# Apply for a job
job_board.apply_for_job("Software Engineer")

# Display applied jobs
job_board.display_applied_jobs()

# Undo last application
job_board.undo_last_application()

# Display available jobs again
job_board.display_available_jobs()

# Process more job postings
job_board.process_job_posting()
