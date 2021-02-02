import json
import pytest

from mock_functions import *


def test_yes_no_api_request(requests_mock):
    requests_mock.get(
        'https://yesno.wtf/api',
        text=json.dumps({
            'answer': 'yes',
        }),
        status_code=200
    )
    result = yes_no_api_request()
    assert result['data']['answer'] == 'yes'
    assert result['code'] == 200


@pytest.mark.parametrize('parameter_answer, parameter_code, expected_result', (
        ('yes', 200, True),
        ('yes', 404, False),
        ('no', 200, False),
))
def test_is_yes_answer(parameter_answer, parameter_code, expected_result, mocker):
    mocker.patch('mock_functions.yes_no_api_request', return_value={
        'data': {
            'answer': parameter_answer,
        },
        'code': parameter_code,
    })
    result = is_yes_answer()
    assert result == expected_result
