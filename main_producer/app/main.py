from flask import Flask

from main_producer.app.routes.message_route import message_blueprint
from main_producer.app.routes.suspicions_route import suspicions_blueprint

app = Flask(__name__)
app.register_blueprint(message_blueprint, url_prefix="/api/email")
app.register_blueprint(suspicions_blueprint, url_prefix="/api/suspicions")

if __name__ == '__main__':
    app.run()
