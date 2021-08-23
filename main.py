import datetime

import pytz as pytz
import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def read_root(timezone: str):
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:

        raise HTTPException(status_code=400, detail="Wrong timezone")
    now = datetime.datetime.now(tz)

    timestr = now.strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content={"time": timestr})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
