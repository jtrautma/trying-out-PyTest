from urllib.request import urlopen
import json
import pytest

def test_gkv() :
    url = 'https://krankenkassen.check24.de/api/federal_state_from_zipcode/80636'
    rawResponse = urlopen(url).read()
    jsonRes = json.loads(rawResponse)
    expected_response = ["Bayern"]
    assert jsonRes == expected_response

# Execute test by runnning pytest test_CHECK24krankenkasse.py