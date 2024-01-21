from typing import List, Optional, Set
from fastapi import FastAPI, Query, Path, Body, Header
from starlette import status
from enum import Enum

app = FastAPI()

"""
Header参数
1、下划线转换中划线，convert_underscores
"""


@app.get("/demo/header/")
async def read_items(user_agent: Optional[str] = Header(None, convert_underscores=True),
                     user_token: Optional[str] = Header(..., convert_underscores=False),
                     user_diy: Optional[str] = Header(None, convert_underscores=True)):
    return {"user_agent": user_agent, "user_token": user_token, "user_diy": user_diy}


"""
2、重命请求头参数
"""


@app.get("/headerList/")
async def read_headerList(x_token: List[str] = Header(None)):
    print(type(x_token))
    return {"X-Token values": x_token}


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)
