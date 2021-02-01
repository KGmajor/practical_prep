import json
from app import app


def test_ping():
    response = app.test_client().get('/ping')

    assert response.status_code == 200

def test_time_with_tz():
    response = app.test_client().get('/time?tz=America/Los+Angeles')

    assert response.status_code == 200

def test_time_with_bad_tz():
    response = app.test_client().get('time?aaaa')

    assert response.status_code == 404
    assert b"Could not process timezone" in response.data

def test_time_with_no_tz():
    response = app.test_client().get('/time')

    assert response.status_code == 200
    assert b"Local time" in response.data