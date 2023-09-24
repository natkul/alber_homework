import random

import pytest

from api_test import ApiTester
from utils.generate_user_data import get_id, get_phone, get_name, get_surname


def pytest_addoption(parser):
    parser.addoption("--ip", action="store", default="127.0.0.1", help="server IP address")
    parser.addoption("--port", action="store", default="4000", help="server Port")


@pytest.fixture(scope='session')
def tester(request):
    ip = request.config.getoption("--ip")
    port = request.config.getoption("--port")
    return ApiTester(ip, port)


@pytest.fixture
async def create_user(tester):
    phone = get_phone()
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'John',
        'surname': 'Doe',
        'phone': phone,
        'age': 30
    }
    response = await tester.send_request(request)
    assert response['status'] == 'success'
    return request


@pytest.fixture(scope='module')
async def prepare_data(tester):
    name = get_name()
    surname = get_surname()
    bodies = [
        {
            'id': get_id(),
            'method': 'add',
            'name': name,
            'surname': get_surname(),
            'phone': get_phone(),
            'age': random.randint(10, 99)
        },
        {
            'id': get_id(),
            'method': 'add',
            'name': name,
            'surname': get_surname(),
            'phone': get_phone(),
            'age': random.randint(10, 99)
        },
        {
            'id': get_id(),
            'method': 'add',
            'name': get_name(),
            'surname': surname,
            'phone': get_phone(),
            'age': random.randint(10, 99)
        },
        {
            'id': get_id(),
            'method': 'add',
            'name': get_name(),
            'surname': surname,
            'phone': get_phone(),
            'age': random.randint(10, 99)
        },
        {
            'id': get_id(),
            'method': 'add',
            'name': get_name(),
            'surname': surname,
            'phone': get_phone(),
            'age': random.randint(10, 99)
        }
    ]

    for body in bodies:
        response = await tester.send_request(body)
        assert response['status'] == 'success'

    return bodies
