import pytest
from nois_api.main import get_app
from pathlib import Path

base_url = "http://localhost:8000/files/"
TEST_FILES_PATH = Path(__file__).parent / "test_files"


def test_uploading_getting_and_deleting_file(client):
    """Test basic CRUD methods work for audio file."""
    test_file = TEST_FILES_PATH / "audiotest.mp3"
    with open(str(test_file.absolute()), "rb") as file:
        content = file.read()
    assert content is not None

    files = {"upload_file": content}
    response = client.post(base_url, files=files)
    assert response.status_code == 201
    response_json = response.json()
    filename = response_json["filename"]

    response = client.get(f"{base_url}{filename}")
    assert response.status_code == 200
    assert response.content == content

    response = client.delete(f"{base_url}{filename}")
    assert response.status_code == 204
