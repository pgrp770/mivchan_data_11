from flask import Flask

from main_producer.app.routes.message_route import message_blueprint

app = Flask(__name__)
app.register_blueprint(message_blueprint, url_prefix="/api/email")

if __name__ == '__main__':
    app.run()
