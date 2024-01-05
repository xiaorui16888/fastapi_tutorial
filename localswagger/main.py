# -*- coding: UTF-8 -*-
"""
@Project ：fastapi_tutorial 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2024/1/5 17:25
"""

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
import pathlib

app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory=f"{pathlib.Path.cwd()}/static"), name="static")


@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        # swagger_js_url="/static/swagger-ui-bundle.js",
        # swagger_css_url="/static/swagger-ui.css",
        swagger_js_url="https://lib.baomitu.com/swagger-ui/5.10.5/swagger-ui-bundle.js",
        swagger_css_url="https://lib.baomitu.com/swagger-ui/5.10.5/swagger-ui.css",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png"
    )


@app.get("/index")
def index():
    return "index"


if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True, port=3000)
