import pytest
from Fetch import app


@pytest.fixture
def client():
	app = app.test_client()


def test_successful_pyr_api(client):
	rv = client.get('/pyramid-word?word=banana')
	assert b'PYRAMID FOUND' in rv.data


def test_failed_pyr_api(client):
	rv_f = client.get('/pyramid-word?word=sad')
	assert b'NOT A PYRAMID' in rv.data


def test_bad_data_api(client):
	rv_f = client.get('/pyramid-word?word=?!@')
	assert b'Unable to process' in rv.data


def test_no_data_api(client):
	rv_f = client.get('/pyramid-word?word=')
	assert 'Data passed incorrectly' in rv.data