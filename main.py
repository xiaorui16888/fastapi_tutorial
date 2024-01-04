import os.path
import pathlib

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI(title="学习FastAPI框架文档", description="以下是关于框架文档的介绍和描述", version="0.0.1",
              # debug=True,
              terms_of_service="https://terms.团队的官网网站/",
              deprecated=False,  # 标记API废弃
              contact={"name": "邮件接受者信息", "url": "https://xxx.cc", "email": "87920151@qq.com"},
              license_info={"name": "版权信息说明License v3.0", "url": "https://www.baidu.com"},
              openapi_tags=[
                  {"name": "接口分组", "description": "接口分组信息说明"}
              ],
              servers=[
                  {"url": "/", "description": "本地调试环境"},
                  {"url": "https://xx.xx.com", "description": "线上测试环境"},
                  {"url": "https://xx2.xx2.com", "description": "线上生产环境"}
              ],
              # docs_url=None,  # 关闭docs访问
              # redoc_url=None, # 关闭redoc访问
              # openapi_url=None, #文档全部关闭访问
              )

templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")

app.mount("/static", staticfiles, name="static")


@app.get("/app/hello", tags=["app实例对象注册接口--示例"])
def app_hello():
    return {"Hello": "app api"}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # 1 / 0
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    # uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
    # 自动获取模块名称，启动
    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(app=f"{app_model_name}:app", host="127.0.0.1", port=8000, reload=True)
