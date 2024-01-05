# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 17:41
"""
import configparser

from fastapi import FastAPI

config = configparser.ConfigParser()
config.read('conf.ini', encoding='utf-8')

app = FastAPI(debug=bool(config.get('fastapi_config', 'debug')),
              title=config.get('fastapi_config', 'title'),
              description=config.get('fastapi_config', 'description'),
              version=config.get('fastapi_config', 'version'), )


@app.get("/index")
def index():
    return "index"


if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True, port=3000)
