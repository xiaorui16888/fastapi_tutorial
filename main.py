import os.path
import pathlib

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI(title="学习FastAPI框架文档", description="以下是关于框架文档的介绍和描述", version="0.0.1")

templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")

app.mount("/static", staticfiles, name="static")


@app.get("/app/hello", tags=["app实例对象注册接口--示例"])
def app_hello():
    return {"Hello": "app api"}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    # uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
    # 自动获取模块名称，启动
    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(app=f"{app_model_name}:app", host="127.0.0.1", port=8000, reload=True)
