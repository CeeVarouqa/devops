import datetime

import pytz as pytz
import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

filename = 'data/visits.data'


def get_counter():
    try:
        with open(filename, 'r') as file:
            c = int(file.readline())
    except (ValueError, FileNotFoundError):
        c = 0
    return c


def increment_counter():
    c = get_counter()
    with open(filename, 'w+') as file:
        file.write(str(c + 1))


@app.get("/")
async def read_root(timezone: str):
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:

        raise HTTPException(status_code=400, detail="Wrong timezone")
    now = datetime.datetime.now(tz)

    timestr = now.strftime("%Y-%m-%d %H:%M:%S")
    increment_counter()
    return JSONResponse(content={"time": timestr})


@app.get("/visits/")
async def visits():
    visits_count = get_counter()
    return JSONResponse(content={"counter": visits_count})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
