# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 19:04
"""
from functools import lru_cache
from typing import Optional

from fastapi import FastAPI
from pydantic.v1 import validator, BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    title: str
    description: str
    version: str

    class Config:  # 可以不用定义
        env_file = ".env"
        env_file_encoding = 'utf-8'

    @validator("version", pre=True)
    def version_len_check(cls, v: str) -> Optional[str]:
        if v and len(v) == 0:
            return None
        return v


@lru_cache()  # 配置读取加上缓存
def get_settings():
    return Settings()


settings = Settings()
print(settings.debug)
print(settings.title)
print(settings.description)
print(settings.version)

# settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    description=settings.description,
    version=settings.version,
)

if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1')
