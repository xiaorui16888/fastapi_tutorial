# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：sty_mount_flask.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 17:13
"""

"""
flask应用
"""

from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/index")
def flask_main():
    return {"index": "我是flask app"}
