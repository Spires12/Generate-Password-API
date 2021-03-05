import pytest

import requests

url = 'http://127.0.0.1:5000' 


def test_generator_password():
  res = requests.get(url + '/generator/password')
  assert res.status_code == 200
