# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/9 16:48
"""
from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()

"""
参数选填，设置默认值
"""


@app.get("/query/")
async def callback(user_id: int, user_name: Optional[str] = None, user_token: str = 'token'):
    return {
        'user_id': user_id,
        'user_name': user_name,
        'user_token': user_token
    }


"""
bool类型参数的转换
"""


@app.get("/query/bool/")
async def callback(isbool: bool = False):
    return {
        'isbool': isbool
    }


"""
参数校验
"""


@app.get("/query/morequery")
async def callback(
        user_id: int = Query(..., ge=10, le=100),
        user_name: str = Query(None, min_length=1, max_length=50, pattern="^fixedquery$"),
        user_token: str = Query(default='token', min_length=1, max_length=50),
):
    return {
        'user_id': user_id,
        'user_name': user_name,
        'user_token': user_token
    }


"""
List类型多值查询参数
"""


@app.get("/query/list/")
async def query_list(q: List[str] = Query(["test1", "test2"])):
    return {
        'q': q
    }


if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)
