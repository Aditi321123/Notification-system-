# Notification-system-
A simple notification system built with FastAPI, RabbitMQ, and Python workers, supporting email, SMS, and in-app notifications, with retry logic and queue-based processing.

📌 Features
📬 API to send notifications (/notifications)
📥 Retrieve user-specific in-app notifications (/users/{id}/notifications)
✉️ Supports Email, SMS, and In-App types
🔁 RabbitMQ for queuing with retry mechanism
⚙️ Docker-ready setup

project Structure-
notification-system/
├── app/
│   ├── main.py                # FastAPI app & routes
│   ├── schemas.py             # Request models (Pydantic)
│   ├── queue.py               # RabbitMQ publishing logic
│   ├── db.py                  # In-memory in-app notification storage
│
├── workers/
│   ├── worker.py              # Consumer + retry logic
│   ├── email_handler.py       # Simulated email notification
│   ├── sms_handler.py         # Simulated SMS notification
│   └── inapp_handler.py       # In-app notification logic
│
├── requirements.txt           # Python dependencies
├── docker-compose.yml         # Containers for RabbitMQ and services
└── README.md

🛠️ Setup Instructions
🚧 Prerequisites
Python 3.9+

Docker & Docker Compose

🔧 Local Development
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/notification-system.git
cd notification-system
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run RabbitMQ with Docker

bash
Copy
Edit
docker-compose up
Start FastAPI app

bash
Copy
Edit
cd app
uvicorn main:app --reload
Start the worker

bash
Copy
Edit
cd ..
python -m workers.worker
🔁 API Endpoints
➕ Send Notification
POST /notifications

json
Copy
Edit
{
  "user_id": "user123",
  "type": "email",        // "email", "sms", or "inapp"
  "message": "Hello!"
}
📥 Get User Notifications
GET /users/{user_id}/notifications

Returns all in-app messages for the given user.

🧪 Example
bash
Copy
Edit
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id":"alice","type":"inapp","message":"Welcome Alice!"}'
Then:

bash
Copy
Edit
curl http://localhost:8000/users/alice/notifications


✅ Bonus Features Implemented
1)Queued processing with RabbitMQ
2)Retry logic (max 3 times) on failure

📊 Management Dashboard
RabbitMQ Management UI:
Visit http://localhost:15672
Username: guest, Password: guest

🧾 Assumptions
#Email/SMS are simulated with print statements (can be swapped with real APIs).
#In-app notifications are stored in-memory (no persistence).
#Retry logic requeues failed messages up to 3 times.
#This is a learning/demo project; production features like auth, DB storage, etc., are out of scope.

📦 Future Improvements
#Add persistent DB (PostgreSQL, Redis, etc.)
#Integrate real email/SMS gateways (SendGrid, Twilio)
#WebSocket support for in-app live notifications
#Authentication / user management

📄 License
MIT — free to use and modify.

