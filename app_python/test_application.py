import datetime
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
from freezegun import freeze_time
import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY

client = TestClient(app)


@freeze_time("2021-08-14 03:21:34", tz_offset=0)
def test_read_main():
    query_params = {
        'timezone': 'Europe/Moscow'
    }
    response = client.get("/", params=query_params)
    assert response.json()['time'] == '2021-08-14 06:21:34'  # Moscow is 3 hours ahead of GMT
    assert response.status_code == 200


@freeze_time("2021-08-14 03:21:34", tz_offset=0)
def test_invalid_input():
    query_params = {
        'timezone': 'Europe/Moscow_blabla'
    }
    response = client.get("/", params=query_params)
    assert response.status_code == 400
