import pytest
from app import app

@pytest.fixture
def client():
  app.config['Testing'] = True
  with app.test_client() as client:
    yield client

def test_home(client):
  rv = client.get('/')
  assert rv.data == b'Welcome to New CI/CD Pipeline using Python! September 06, 2024'
