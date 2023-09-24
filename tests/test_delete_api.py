import pytest

from schemas.response_schemas import DELETE
from utils.generate_user_data import get_id
from utils.validator import is_valid


@pytest.mark.asyncio
async def test_delete_user(tester, create_user):
    user = await create_user
    phone = user['phone']
    request = {
        'id': get_id(),
        'method': 'delete',
        'phone': phone,
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'success', 'user was not deleted'


@pytest.mark.asyncio
async def test_delete_same_user(tester, create_user):
    user = await create_user
    phone = user['phone']
    request = {
        'id': get_id(),
        'method': 'delete',
        'phone': phone,
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'success', 'user was not deleted'

    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'failure', 'second user was deleted with the same id'


@pytest.mark.asyncio
async def test_delete_user_without_phone(tester, create_user):
    request = {
        'id': get_id(),
        'method': 'delete'
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'failure', 'user was not deleted'


@pytest.mark.parametrize('re_id', [1, True, ''])
@pytest.mark.asyncio
async def test_check_invalid_id(tester, create_user, re_id):
    user = await create_user
    phone = user['phone']
    request = {
        'id': re_id,
        'method': 'delete',
        'phone': phone,
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True, f'response did not pass schema validate, response: {response}'
    assert response['status'] == 'failure', f'id can be not valid: {re_id}: {type(re_id)}'


@pytest.mark.parametrize('method', [1, True, '', 'abc'])
@pytest.mark.asyncio
async def test_check_invalid_method(tester, create_user, method):
    user = await create_user
    phone = user['phone']
    request = {
        'id': get_id(),
        'method': method,
        'phone': phone,
    }
    response = await tester.send_request(request)

    assert response['status'] == 'failure', f'method can be not valid: {method}: {type(method)}'
    assert 'id' in response, f'response does not contain "id", response: {response}'
    assert 'method' in response, f'response does not contain "method", response: {response}'
    assert len(response) == 3


@pytest.mark.parametrize('phone', [1, False])
@pytest.mark.asyncio
async def test_check_invalid_phone(tester, phone):
    request = {
        'id': get_id(),
        'method': 'delete',
        'phone': phone,
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'failure', f'phone can be as {phone}: {type(phone)}'


@pytest.mark.asyncio
async def test_check_delete_non_exist_phone(tester):
    phone = get_id()
    request = {
        'id': get_id(),
        'method': 'delete',
        'phone': get_id(),
    }
    response = await tester.send_request(request)

    assert is_valid(response, DELETE) is True
    assert response['status'] == 'failure', f'phone can be as {phone}: {type(phone)}'
