import pytest
from fetch_rt.app import app


@pytest.fixture(scope='module')
def testing_client():
	with app.test_client() as client:
		yield client


def test_successful_pyr_api(testing_client):
	rv = testing_client.get('/process_word?word=banana')
	assert b'PYRAMID FOUND'in rv.data


def test_failed_pyr_api(testing_client):
	rv_f = testing_client.get('/process_word?word=sad')
	assert b'NOT A PYRAMID' in rv_f.data


def test_bad_data_api(testing_client):
	rv_f = testing_client.get('/process_word?word=?!@')
	assert b'Unable to process' in rv_f.data


def test_no_data_api(testing_client):
	rv_f = testing_client.get('/process_word?word=')
	assert b'Unable to process' in rv_f.data
