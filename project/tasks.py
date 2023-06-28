from celery import shared_task
from celery.contrib.abortable import AbortableTask

from time import sleep


@shared_task(bind=True, base=AbortableTask)
def start_action(self):
    
    for i in range(100):
        print(i)
        sleep(1)
        if self.is_aborted():
            return 'TASK STOPPED!'
    return 'DONE!'