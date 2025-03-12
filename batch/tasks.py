from time import sleep
from .models import BatchJob, BatchData
import threading  # Running tasks in the background

def process_batch(batch_id):
    batch = BatchJob.objects.get(id=batch_id)
    batch.status = 'processing'
    batch.save()

    # Simulating batch processing
    for item in BatchData.objects.filter(batch=batch):
        sleep(1)  # Simulating processing time
        item.processed = True
        item.save()

    batch.status = 'completed'
    batch.save()

def run_batch_process_async(batch_id):
    thread = threading.Thread(target=process_batch, args=(batch_id,))
    thread.start()
