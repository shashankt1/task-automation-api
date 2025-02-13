from celery import Celery
from flask import Flask
from app.models import db, Task
import time

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

app = Flask(__name__)
app.config.from_object('config.Config')
celery = make_celery(app)

@celery.task(bind=True)
def execute_task(self, task_id):
    task = Task.query.get(task_id)
    if task:
        task.status = "Processing"
        db.session.commit()
        time.sleep(10)
        task.status = "Completed"
        db.session.commit()
