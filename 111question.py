# question: Home Renovation Manager: Stack for undoing project changes, queue for  processing renovation tasks, and list to manage ongoing projects.

from collections import deque

class HomeRenovationManager:
    def __init__(self):
        # Stack to track project changes for undo functionality
        self.project_changes_stack = []
        
        # Queue to store renovation tasks (FIFO)
        self.renovation_tasks_queue = deque()
        
        # List to manage ongoing projects
        self.ongoing_projects = []

    # Add a project to the ongoing projects list
    def add_project(self, project):
        self.ongoing_projects.append(project)
        print(f"Project added: {project}")
    
    # Display ongoing projects
    def display_projects(self):
        if self.ongoing_projects:
            print("Ongoing projects:")
            for project in self.ongoing_projects:
                print(f"- {project}")
        else:
            print("No ongoing projects at the moment.")
    
    # Make changes to a project and track changes in stack
    def make_change(self, project, change):
        if project in self.ongoing_projects:
            self.project_changes_stack.append((project, change))
            print(f"Change made to project '{project}': {change}")
        else:
            print(f"Project '{project}' not found.")
    
    # Undo the last project change
    def undo_last_change(self):
        if self.project_changes_stack:
            project, change = self.project_changes_stack.pop()
            print(f"Undid change to project '{project}': {change}")
        else:
            print("No changes to undo.")
    
    # Add renovation task to the queue
    def add_task(self, task):
        self.renovation_tasks_queue.append(task)
        print(f"Task added: {task}")
    
    # Process the next renovation task in the queue
    def process_task(self):
        if self.renovation_tasks_queue:
            task = self.renovation_tasks_queue.popleft()
            print(f"Processing task: {task}")
        else:
            print("No tasks to process.")
    
    # Display pending tasks in the queue
    def display_pending_tasks(self):
        if self.renovation_tasks_queue:
            print("Pending renovation tasks:")
            for task in self.renovation_tasks_queue:
                print(f"- {task}")
        else:
            print("No pending tasks at the moment.")

# Example usage:

manager = HomeRenovationManager()

# Adding projects
manager.add_project("Kitchen Remodel")
manager.add_project("Bathroom Renovation")

# Displaying ongoing projects
manager.display_projects()

# Making changes to a project
manager.make_change("Kitchen Remodel", "Installed new cabinets")
manager.make_change("Bathroom Renovation", "Replaced tiles")

# Undoing last change
manager.undo_last_change()

# Adding renovation tasks to the queue
manager.add_task("Paint the walls")
manager.add_task("Install new lighting")
manager.add_task("Finish flooring")

# Displaying pending tasks
manager.display_pending_tasks()

# Processing renovation tasks
manager.process_task()
manager.process_task()

# Display pending tasks after processing some
manager.display_pending_tasks()
