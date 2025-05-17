from app.db import save_notification

def send_inapp(data):
    save_notification(data['user_id'], data['content'])
    print(f"In-app notification stored for user {data['user_id']}")
