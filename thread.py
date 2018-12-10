from flask import Flask
import flask_apscheduler 
from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'thread:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 2
        }
    ]

    SCHEDULER_API_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b))

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/mine', methods=['GET'])
    def mine():


    app.config.from_object(Config())

    scheduler = APScheduler()
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    app.run(host='0.0.0.0', port=4000)