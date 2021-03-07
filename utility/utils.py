# coding:utf-8

from utility.constant import *
import subprocess
import time
import sys


def start_bot_cmd(bot_url, ip):
    if DOMAIN_BASENAME not in bot_url:
        return 420
    for danger_cmd in DANGER_CMDS:
        if danger_cmd in bot_url:
            return 422
    try:
        bot_url = bot_url.replace(GAME_HOMEPAGE_URL, 'localhost:%d' % GAME_PORT)
        if sys.platform == 'win32':
            prc = subprocess.Popen(['node', 'play-bot', '--bot=%s' % BOT_NAME, '%s' % bot_url], cwd=BOT_DIR, shell=True)
        else:
            prc = subprocess.Popen(['node play-bot --bot=%s %s' % (BOT_NAME, bot_url)], cwd=BOT_DIR, shell=True)
    except FileNotFoundError:
        return 421
    time.sleep(1)
    if subprocess.Popen.poll(prc) is None:
        return 0
    else:
        return 422
