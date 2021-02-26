# coding:utf-8

from flask import Flask, render_template, request
from utility.utils import start_bot_cmd
from utility.constant import *


app = Flask(__name__)


# TODO
def homepage():
    return 0


@app.route('/')
@app.route('/ready/')
def ready():
    data = {'error_code': 0}
    return render_template('ready.html', **data)


@app.route('/start_bot/', methods=['POST'])
def start_bot():
    ip = request.remote_addr
    bot_url = request.form['bot_url']
    ret = start_bot_cmd(bot_url, ip)
    if ret == 0:
        return 'success'
    else:
        data = {'error_code': ret}
        return render_template('ready.html', **data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=BOT_PORT)
