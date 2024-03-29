import os.path
import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from sty_mount_flask import flask_app
# async def fastapi_index():
#     return JSONResponse({"index": "fastapi_index"})
#
#
# async def fastapi_about():
#     return JSONResponse({"about": "fastapi_about"})
#
#
# routers = [
#     APIRoute(path="/fastapi/index", endpoint=fastapi_index, methods=["GET", "POST"]),
#     APIRoute(path="/fastapi/about", endpoint=fastapi_about, methods=["GET", "POST"]),
# ]
from sty_route import sty_route_app
from sty_sub_app import sub_app


async def exception_not_found(request, exc):
    return JSONResponse({"code": exc.status_code, "error": "没有定义这个请求地址"},
                        status_code=exc.status_code)


exception_handlers = {
    404: exception_not_found
}

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
              exception_handlers=exception_handlers  # 定义异常捕捉处理器
              )

# app = FastAPI(routers=routers)  # 全局routers参数

templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")

app.mount("/static", staticfiles, name="static")

# 挂载子应用
app.mount(path="/sub_app", app=sub_app, name='sub_app')

# 挂载其他WSGI应用
app.mount(path="/flask_app", app=WSGIMiddleware(flask_app), name="flask_app")

# 路由注册方式
router_user = APIRouter(prefix="/user", tags=["用户模块"])
router_pay = APIRouter(prefix="/pay", tags=["支付模块"])


@router_user.get("/user/login")
def user_login():
    return {"ok": "登录成功"}


@router_pay.get("/pay/order")
def pay_order():
    return {"ok": "订单支付成功"}


# TODO:会有告警，想不通...UserWarning: Duplicate Operation ID user_info_user_user_user_info_post for function user_info at /Users/safety/PycharmProjects/fastapi_tutorial/main.py
#   warnings.warn(message, stacklevel=1)
@router_user.api_route("/user/user_info", methods=["POST", "GET"])  # 支持多个请求方法
def user_info():
    return {"ok": "查看用户信息"}


# 添加路由分组
app.include_router(router_pay)
app.include_router(router_user)

app.include_router(sty_route_app)


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
