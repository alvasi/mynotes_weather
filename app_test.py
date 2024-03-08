import pytest
from app import app
from unittest.mock import patch
import json


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("requests.get")
def test_current_weather_success(mock_get, client):
    """Test the /current_weather endpoint for a successful mocked response."""
    # Mocking the API response
    mock_response = {"current": {"temperature": 20, "weather_descriptions": ["Sunny"]}}
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = mock_response

    city = "London"
    response = client.get(f"/current_weather?city={city}")
    data = response.get_json()

    # Asserts
    assert response.status_code == 200
    assert data["temperature"] == 20
    assert data["weather_description"] == "Sunny"
