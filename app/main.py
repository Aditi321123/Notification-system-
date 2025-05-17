from fastapi import FastAPI, HTTPException
from app.schemas import NotificationRequest
from app.queue import send_to_queue
from app.db import get_user_notifications

app = FastAPI()

@app.post("/notifications")
def send_notification(notification: NotificationRequest):
    try:
        send_to_queue(notification.dict())
        return {"message": "Notification queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}/notifications")
def get_notifications(user_id: str):
    return get_user_notifications(user_id)
