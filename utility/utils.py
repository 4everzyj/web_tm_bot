# coding:utf-8

from utility.constant import *
import subprocess
import time


def start_bot_cmd(bot_url, ip):
    if DOMAIN_BASENAME not in bot_url:
        return 420
    try:
        prc = subprocess.Popen(['node', 'play-bot', '--bot=%s' % BOT_NAME, '%s' % bot_url], cwd=BOT_DIR, shell=True)
    except FileNotFoundError:
        return 421
    time.sleep(1)
    if subprocess.Popen.poll(prc) is None:
        return 0
    else:
        return 422
