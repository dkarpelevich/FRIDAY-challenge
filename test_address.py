import json


def test_address(input_json='addresses.json'):
    with open(input_json, 'r', encoding='utf-8') as infile:
        assert_result = json.load(infile)
    assert assert_result['addresses'][0]['street'] == 'Winterallee'
    assert assert_result['addresses'][0]['housenumber'] == '3'
    assert assert_result['addresses'][1]['street'] == 'Musterstr.'
    assert assert_result['addresses'][1]['housenumber'] == '45'
    assert assert_result['addresses'][2]['street'] == 'Blaufeldweg'
    assert assert_result['addresses'][2]['housenumber'] == '123B'
    assert assert_result['addresses'][3]['street'] == 'Am Bächle'
    assert assert_result['addresses'][3]['housenumber'] == '23'
    assert assert_result['addresses'][4]['street'] == 'Auf der Vogelwiese'
    assert assert_result['addresses'][4]['housenumber'] == '23 b'
    assert assert_result['addresses'][5]['street'] == 'rue de la revolution'
    assert assert_result['addresses'][5]['housenumber'] == '4'
    assert assert_result['addresses'][6]['street'] == 'Calle 39'
    assert assert_result['addresses'][6]['housenumber'] == 'No 1540'


