from datetime import date
from Task import Task
import json
class Tenant():
    """
    Tenant class holds the basic information of the tenant.
    Attributes:
    _info: dict
        name: str
        room: str
        subtenant: bool
    
    is_available: bool
    tasklist: list of Task
    absent_from: None or datetime.date()
    absent_till: None or datetime.date()

    Methods:

    """
    def __init__(self, args) -> None:
        self._info = {
            'name': args['name'],
            'room': args['room'],
            'subtenant': args['subtenant']
        }
        self.total_work_time = args['total_work_time']
        self.is_available = args['is_available']
        self.tasklist = [Task(task_info) for task_info in args['tasklsit']]
        self.absent_from = date.fromisoformat(args['absent_from']) 
        self.absent_till = date.fromisoformat(args['absent_till'])
        
    def add_task(self, task: Task) -> bool:
        if self.is_available:
            self.tasklist.append(task)
            return True
        else:
            return False
    
    def finish_task(self, task_id: int) -> bool:
        for task in self.tasklist:
            if id(task) == task_id:
                task['done'] = True
                self.total_work_time += task['time']
    
    def temp_leave(self, end: date, start: date = date().today()) -> bool:
        if end >= start:
            self.absent_from = start
            self.absent_till = end
            self.is_available = False
            return True
        else:
            return False

    def status(self) -> dict:
        tenant_status = {
            **self._info,
            'total_work_time': self.total_work_time,
            'is_available': True if self.is_available else False,
            'tasklist': [task.status() for task in self.tasklist],
            'absent_from': self.absent_from.isoformat(),
            'absent_till': self.absent_till.isoformat()
        }
        return tenant_status

    def save(self) -> bool:
        json_dict = json.dumps(self.status())
        filename = self._info['room'] + self._info['name']
        with open(filename, 'w') as file:
            file.write(json_dict)

    def __del__(self):
        print(id(self), "deleted")
        


    