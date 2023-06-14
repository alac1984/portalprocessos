from fastapi import FastAPI
from application.main import app


def test_app():
    assert isinstance(app, FastAPI)
