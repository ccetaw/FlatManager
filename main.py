from Tenant import Tenant
from Task import Task

"""
Main functionalities:
    Database:
    1. Store information of the tenants
    2. Store regulations of the flat
    3. Store regular tasks

    Callbacks:
    1. Start of the day:
        - Check status of all tenants, check if their tasks are done.
            - If their tasks are on the due date, remind them to do it
        - Assign regular tasks to tenants in an evenly distributed way regarding their availability
        - Greetings to tenants
        - Show today's task list
    2. User call:
        1) Delay the task (because of the trash bin is not full and it's not necessary to do it now, etc.)
        2) Register a regular task (require administer)
        3) Register an occasional task
        4) Mark a task as done. Occasional tasks will be deleted, regular tasks will be regenerated
        5) Output help information
    3. On message:
        1) 
    

"""