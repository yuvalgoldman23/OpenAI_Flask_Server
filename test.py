import pytest
import requests

# The URL for the Flask server running from the Docker container
BASE_URL = 'http://localhost:5000'

@pytest.fixture(scope='module')
def flask_app():
    return BASE_URL

def test_endpoint(flask_app):
    """
    Test the /ask endpoint of the Flask app.
    """
    # Send some data to test the POST request and response
    data = {'question': 'Is it true that?'}
    
    response = requests.post(f'{flask_app}/ask', json=data)
    
    # Assert the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert the response contains an 'answer' field
    assert 'answer' in response.json()

if __name__ == '__main__':
    pytest.main()
