# coding: utf-8
import os
from flask import Flask, request
from autopy.key import (
    toggle,
    K_CONTROL,
    K_F3,
    K_F1,
    K_F2, K_F4, K_F6)


app = Flask(__name__)
project_root = os.path.abspath(".")
template = open(os.path.join(project_root, "templates/index.html"), "r").read()


class MusicBox(object):
    @classmethod
    def _press_keys(cls, keys):
        map(lambda key: toggle(key, True), keys)
        map(lambda key: toggle(key, False), keys)

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

