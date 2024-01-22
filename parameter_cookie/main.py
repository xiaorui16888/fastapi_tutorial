# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/22 11:00
"""

from typing import List, Optional, Set
from fastapi import FastAPI, Query, Path, Body, Header, Cookie
from starlette import status
from enum import Enum

from starlette.responses import Response

app = FastAPI()


@app.get("/set/cookie/")
def set_cookie(response: Response):
    response.set_cookie(key="username", value="xiaozhu")
    return "set_cookie ok"


@app.get("/get/cookie/")
def get_cookie(username: Optional[str] = Cookie(None)):
    return {"username": username}


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)
