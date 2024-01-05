# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：sty_sub_app.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 17:01
"""

"""
主从应用挂载
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

sub_app = FastAPI(title="子应用", description="我是子应用的文档描述", version="0.0.1")


@sub_app.get("/index")
async def index():
    return JSONResponse({"index": "index"})
