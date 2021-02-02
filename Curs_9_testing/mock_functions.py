import json
import requests
import pytest


def yes_no_api_request():
    request = requests.get('https://yesno.wtf/api')
    return {
        'data': json.loads(request.text),
        'code': request.status_code,
    }


def is_yes_answer():
    request_data = yes_no_api_request()
    answer = request_data['data']['answer']
    code = request_data['code']
    return answer == 'yes' and code == 200
