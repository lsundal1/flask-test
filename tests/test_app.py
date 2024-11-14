import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app 
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json[0] == {
"author_id": 3,
"book_id": 1,
"is_fiction": True,
"price_in_pence": 809,
"quantity_in_stock": 550,
"release_date": "Sun, 12 Oct 1997 00:00:00 GMT",
"title": "The Hitchhiker's Guide to the Galaxy"
}
    
def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404