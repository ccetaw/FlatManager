
from datetime import date

class Task():
    def __init__(self, args) -> None:
        self.start_date = args['start_date']
        self.due_date = args['due_date']
        self.name = args['name']
        self.time = args['time'] # mins
        self.done = args['done']
        self.instruction = args['instruction']
        self.is_regular = True

    def status(self) -> dict:
        pass

    @classmethod
    def regular(cls):
        return cls()

    @classmethod
    def occasional(cls):
        pass
    