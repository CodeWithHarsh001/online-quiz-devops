
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Online Quiz System" in response.data


def test_quiz_page():
    client = app.test_client()
    response = client.get("/quiz")

    assert response.status_code == 200
    assert b"What does HTML stand for?" in response.data


def test_quiz_submission():
    client = app.test_client()

    response = client.post("/quiz", data={
        "question_0": "Hyper Text Markup Language",
        "question_1": "Python",
        "question_2": "Containerization",
        "question_3": "GitHub Actions",
        "question_4": "git clone"
    })

    assert response.status_code == 200
    assert b"5 / 5" in response.data
