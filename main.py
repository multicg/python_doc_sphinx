from http.client import HTTPException
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """
    루트 진입점 입니다.

    :rtype: dict
    """
    return {"message": "Hello, FastAPI + Poetry + Uvicorn + Sphinx!"}


@app.get("/add/{a}/{b}")
async def read_add(a: str, b: str):
    """
    입력받은 두 정수를 더하는 함수입니다.

    :param a: 첫 번째 정수
    :param b: 두 번째 정수
    :return: 두 정수와 두 정수의 합을 "message"라는 키로 반환합니다.
    :rtype: dict
    """
    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        raise HTTPException(status_code=400, detail="Both a and b must be integers")

    result = a_int + b_int
    message = f"{a_int} + {b_int} = {result}"
    return {"message": message}
