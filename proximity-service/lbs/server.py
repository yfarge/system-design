from flask import Flask

server = Flask(__name__)


@server.route('/')
def message():
    return "Location Based Service"


if __name__ == '__main__':
    server.run()
