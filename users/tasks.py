from main.celery import app
from .send_email import send_reset_email


@app.task
def reset_email_task(user_email, code):
    send_reset_email(user_email, code)

