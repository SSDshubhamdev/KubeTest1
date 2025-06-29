from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Azure Microservice!"

if __name__ == '__main__':
    # Runs the app on all interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)