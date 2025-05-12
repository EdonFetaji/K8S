from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Redis connection settings from environment variables
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route('/')
def index():
    try:
        count = r.incr('pageviews')
    except redis.exceptions.ConnectionError:
        count = "Unavailable (Redis connection failed)"
    return render_template('index.html', count=count)

if __name__ == '__main__':
    # Flask host/port settings from environment variables
    FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.environ.get("FLASK_PORT", 80))
    app.run(host=FLASK_HOST, port=FLASK_PORT)
