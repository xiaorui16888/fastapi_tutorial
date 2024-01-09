# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 19:50
"""
from enum import Enum
from typing import List

from fastapi import FastAPI, Query, Path
from starlette import status

app = FastAPI()


# 路径操作及路径函数（参数）
@app.post("/parameter/", summary='我是路径参数', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
async def parameter(q: List[str] = Query(["test1", "test2"])):
    return {
        'message': q,
    }


# 路径参数
@app.get("/user/{user_id}/article/{article_id}")
async def callback(user_id: int, article_id: str):
    return {
        'user_id': user_id,
        'article_id': article_id
    }


# 带 / 的关键子路径参数
@app.get("/uls/{file_path}")
async def callback_file_path(file_path: str):
    return {
        'file_path': file_path
    }


# 把路径变量定义为Path类型，才能正常处理
@app.get("/uls/{file_path:path}")
async def callback_file_path_2(file_path: str):
    return {
        'file_path': file_path
    }


# 枚举预设路径参数值
class ModelName(str, Enum):
    name1 = "name1"
    name2 = "name2"
    name3 = "name3"


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.name1:
        return {"model_name": model_name, "message": "ok!"}
    if model_name.value == "name2":
        return {"model_name": model_name, "message": "name2 ok!"}
    return {"model_name": model_name, "message": "fail!"}


@app.get("/pay/{user_id}/article/{article_id}")
async def callback(user_id: int = Path(..., title="用户ID", description='用户ID信息', ge=10000),
                   article_id: str = Path(..., title="文章ID", description='用户所属文章ID信息', min_length=1,
                                          max_length=50)):
    return {
        'user_id': user_id,
        'article_id': article_id
    }


@app.get("/items/{item_id}")
async def callback(*, item_id: int = Path(..., ), q: str):
    return 'OK'


@app.get("/items/{item_id}")
async def callback(*, item_id: int = Path(..., ), q: str):
    return 'OK'


if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)
