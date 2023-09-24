import pytest

from schemas.response_schemas import ADD
from utils.generate_user_data import get_id, get_phone
from utils.validator import is_valid


@pytest.mark.asyncio
async def test_add_user(tester):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'John',
        'surname': 'Doe',
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'success', 'user was not created'


@pytest.mark.asyncio
async def test_try_add_same_user(tester):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'John',
        'surname': 'Doe',
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'success', 'first user was not created'

    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'failure', 'second user was created with the same id'


@pytest.mark.parametrize('re_id', [1, True, ''])
@pytest.mark.asyncio
async def test_check_invalid_id(tester, re_id):
    request = {
        'id': re_id,
        'method': 'add',
        'name': 'John',
        'surname': 'Doe',
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True, f'response did not pass schema validate, response: {response}'
    assert response['status'] == 'failure', f'id can be not valid: {re_id}: {type(re_id)}'


@pytest.mark.parametrize('method', [1, True, '', 'abc'])
@pytest.mark.asyncio
async def test_check_invalid_method(tester, method):
    request = {
        'id': get_id(),
        'method': method,
        'name': 'John',
        'surname': 'Doe',
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert response['status'] == 'failure', f'method can be not valid: {method}: {type(method)}'
    assert 'id' in response, f'response does not contain "id", response: {response}'
    assert 'method' in response, f'response does not contain "method", response: {response}'
    assert len(response) == 3


# pytest-xdist has problems with run parametrize tests when use func instead of constants
@pytest.mark.parametrize('name', [1, True])
@pytest.mark.asyncio
async def test_check_invalid_name_type(tester, name):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': name,
        'surname': 'Doe',
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'failure', f'name can be as {name}: {type(name)}'


# pytest-xdist has problems with run parametrize tests when use func instead of constants
@pytest.mark.parametrize('surname', [1, False])
@pytest.mark.asyncio
async def test_check_invalid_surname_type(tester, surname):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'joe',
        'surname': surname,
        'phone': get_phone(),
        'age': 30
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'failure', f'surname can be as {surname}: {type(surname)}'


# pytest-xdist has problems with run parametrize tests when use func instead of constants
@pytest.mark.parametrize('phone', [1, False])
@pytest.mark.asyncio
async def test_check_invalid_phone_type(tester, phone):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'joe',
        'surname': 'bibick',
        'phone': phone,
        'age': 30
    }

    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'failure', f'phone can be as {phone}: {type(phone)}'


# pytest-xdist has problems with run parametrize tests when use func instead of constants
@pytest.mark.parametrize('age', ['1', 0, True])
@pytest.mark.asyncio
async def test_check_invalid_age_type(tester, age):
    request = {
        'id': get_id(),
        'method': 'add',
        'name': 'joe',
        'surname': 'bibick',
        'phone': get_phone(),
        'age': age
    }
    response = await tester.send_request(request)

    assert is_valid(response, ADD) is True
    assert response['status'] == 'failure', f'age can be as {age}: {type(age)}'
