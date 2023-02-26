# coding: utf-8
import os
from flask import Flask, request, jsonify
import autopy

from autopy.key import (
    toggle,
    Modifier,
    Code,
)

K_CONTROL = Modifier.CONTROL
K_F3 = Code.F3
K_F1 = Code.F1
K_F2 = Code.F2
K_F4 = Code.F4
K_F6 = Code.F6


app = Flask(__name__)
project_root = os.path.abspath(".")
template = open(os.path.join(project_root, "templates/index.html"), "r", encoding="utf-8").read()


class MusicBox(object):
    @classmethod
    def _press_keys(cls, keys):
        autopy.key.tap(
            keys[1],
            [keys[0]]
        )

    @classmethod
    def next_song(cls):
        cls._press_keys((K_CONTROL, K_F3))

    @classmethod
    def prev_song(cls):
        cls._press_keys((K_CONTROL, K_F1))

    @classmethod
    def pause_play(cls):
        cls._press_keys((K_CONTROL, K_F2))

    @classmethod
    def volume_up(cls):
        cls._press_keys((K_CONTROL, K_F6))

    @classmethod
    def volume_down(cls):
        cls._press_keys((K_CONTROL, K_F4))

    @classmethod
    def shutdown(cls):
        os.system("shutdown -s -t 5")


@app.route('/')
def hello_world():
    key_word = request.args.get("action")
    if key_word:
        getattr(MusicBox, key_word)()

    return template


# 移动端连接服务器校验
@app.route('/mobile_connect')
def mobile_connect():
    response = jsonify(code=200, message="Connected", platform="win", status=1, version="0.0.1")
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10010)

