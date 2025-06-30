from celery import Celery
from ..tasks import reminder

celery_app = Celery(
    "recallify",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1"
)

celery_app.conf.update(
    task_routes = {
        "app.tasks.*": {"queue": "default"},
    },
    task_default_queue = "default"
)