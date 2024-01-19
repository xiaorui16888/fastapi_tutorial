# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/18 14:42
"""
from typing import List, Optional, Set, Dict
from fastapi import FastAPI, Query, Path, Body
from pydantic.v1 import Field
from starlette import status
from enum import Enum

app = FastAPI()

from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    user_id: str
    token: str
    timestamp: str
    article_id: Optional[str] = None


"""
用pydantic模型申明请求体
"""


@app.post("/read_item/")
def read_item(item: Item):
    return {
        "user_id": item.user_id,
        "article_id": item.article_id
    }


"""
单值Request Body字段参数定义：长度，大小
"""


@app.post("/action/item")
def action_item(user_id: int = Body(..., gt=10),
                token: str = Body(...),
                article_id: str = Body(default=None)):
    return {
        "user_id": user_id,
        "article_id": article_id,
        "token": token
    }


class Itement(BaseModel):
    user_id: int = Body(..., gt=10, embed=True)
    token: str
    timestamp: str
    article_id: Optional[str] = None


@app.post("/action/body3")
def callbackbody(item: Itement = Body(default=None, embed=False)):
    return {
        'body': item
    }


# =================
class ItemUser(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


"""
多个request body参数
"""


@app.put("/items/")
async def update_item1111(item: ItemUser, user: User):
    results = {"item": item, "user": user}
    return results


"""
多个模型类和单个request body
"""


@app.put("/items/more")
async def update_item(item: Item, user: User, importance: int = Body(..., gt=0)
                      ):
    results = {"item": item, "user": user, "importance": importance}
    return results


"""
模型类嵌套声明
"""


class ItemUser2(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    user: User


@app.put("/items/body4")
async def update_item(item: ItemUser2, importance: int = Body(..., gt=0)
                      ):
    results = {"item": item, "user": item.user, "importance": importance}
    return results


"""
嵌套模型为List、Set类型
"""


class ItemUser3(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    user: User
    # 新增模型嵌套并设置为集合类型
    tags: Set[str] = []
    users: List[User] = None


@app.put("/items/body555")
async def update_item(item: ItemUser3, importance: int = Body(..., gt=0)):
    results = {"item": item, "user": item.user, "importance": importance}
    return results


"""
任意dict字典类型构成请求体
"""


@app.post("/items/body6")
async def body6(item: Dict[str, str]):
    results = {"item": item}
    return results


"""
模型中的field字段定义
"""


class FieldItem(BaseModel):
    name: Optional[str] = Field(default=None, title="字段标题", description="字段描述", max_length=5)
    token: Optional[float] = None


@app.post("/demo/field")
async def demo_field(name: FieldItem):
    results = {
        "name": name
    }
    return results


if __name__ == '__main__':
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)
