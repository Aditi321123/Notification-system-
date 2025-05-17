in_app_notifications = {}

def save_notification(user_id, content):
    in_app_notifications.setdefault(user_id, []).append(content)

def get_user_notifications(user_id):
    return in_app_notifications.get(user_id, [])
