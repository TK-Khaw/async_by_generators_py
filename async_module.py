import datetime

def sleep(delay):
    """
    Implements an async sleep.
    """
    init_time = datetime.datetime.now().timestamp()
    end_time = init_time + delay
    while datetime.datetime.now().timestamp() < end_time:
        yield False

class Task:
    """
    Basically a data struct that links the callee to the caller.
    """
    def __init__(self, callee):
        self._callee = callee
        self.caller = None
        self._result = None

    def get_next(self):
        if self._result:
            """
            Last iteration produced the result from the callee.
            Send it to the caller.
            """
            self._callee.send(self._result)
            self._result = None
        return next(self._callee)

    def set_result(self, value):
        self._result = value

class EventLoop:
    def __init__(self):
        self._runnable_tasks = []

    def create_task(self, gen):
        """
        Create task that is monitored by the event loop using 
        given generator, `gen`.
        Kinda akin to call_soon on asyncio EventLoop.
        """
        self._runnable_tasks.append(Task(gen))


    def run_until_complete(self):
        """
        The event loop.
        The event loop basically did a round-robin.
        Akin to trampoline dispatch.
        """
        while self._runnable_tasks:
            for task in self._runnable_tasks:
                try:
                    res = task.get_next()
                    if isinstance(res, Task): 
                        """
                        If res is Task instance, add it to the loop, 
                        remove its caller from the loop, since it is awaiting result.
                        """
                        res.caller = task
                        self._runnable_tasks.remove(task)
                        self._runnable_tasks.append(res)
                except StopIteration as exc:
                    """
                    If task has a caller, then we must return the value back to it 
                    for further processing.
                    The caller is then added back into the loop-monitored tasks.
                    Callee will be removed since execution is completed.
                    """
                    if task.caller:
                        task.caller.set_result(exc.value)
                        self._runnable_tasks.append(task.caller)
                    self._runnable_tasks.remove(task)
                
        

