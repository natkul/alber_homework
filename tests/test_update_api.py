import random

import pytest
from faker import Faker

from schemas.response_schemas import ADD, UPDATE
from utils.generate_user_data import get_id, get_phone
from utils.user import get_user
from utils.validator import is_valid


@pytest.mark.asyncio
async def test_update_user(tester, create_user):
    user = await create_user
    faker = Faker()
    new_name = faker.name()
    request = {
        'id': get_id(),
        'method': 'update',
        'name': new_name,
        'surname': user['surname'],
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)

    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'success', 'user was not updated'

    user_info = {
        'phone': user['phone'],
    }

    response = await get_user(tester, user_info)
    assert response['users'][0]['name'] == new_name
    assert response['users'][0]['surname'] == request['surname']
    assert response['users'][0]['phone'] == request['phone']
    assert response['users'][0]['age'] == request['age']


@pytest.mark.asyncio
async def test_update_surname(tester, create_user):
    user = await create_user
    faker = Faker()
    new_surname = faker.name()
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': new_surname,
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)

    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'success', 'user was not updated'

    user_info = {
        'phone': user['phone'],
    }

    response = await get_user(tester, user_info)
    assert response['users'][0]['name'] == request['name']
    assert response['users'][0]['surname'] == new_surname
    assert response['users'][0]['phone'] == request['phone']
    assert response['users'][0]['age'] == request['age']


@pytest.mark.asyncio
async def test_update_age(tester, create_user):
    user = await create_user
    age = random.randint(1, 99)
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': user['surname'],
        'phone': user['phone'],
        'age': age
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'success', 'user was not updated'

    user_info = {
        'phone': user['phone'],
    }

    response = await get_user(tester, user_info)
    assert response['users'][0]['name'] == request['name']
    assert response['users'][0]['surname'] == request['surname']
    assert response['users'][0]['phone'] == request['phone']
    assert response['users'][0]['age'] == age


@pytest.mark.parametrize('phone', [1, False, '123'])
@pytest.mark.asyncio
async def test_validate_update_phone(tester, create_user, phone):
    user = await create_user
    phone = get_phone()
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': user['surname'],
        'phone': phone,
        'age': user['age']
    }
    response = await tester.send_request(request)

    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', f'user was updated, {request}'


@pytest.mark.parametrize('name', [1, True])
@pytest.mark.asyncio
async def test_update_user(tester, create_user, name):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': name,
        'surname': user['surname'],
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)

    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'


@pytest.mark.parametrize('surname', [1, False])
@pytest.mark.asyncio
async def test_update_surname(tester, create_user, surname):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': surname,
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)

    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was not updated'


@pytest.mark.parametrize('age', ['1', 0, True])
@pytest.mark.asyncio
async def test_invalid_update_age(tester, create_user, age):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': user['surname'],
        'phone': user['phone'],
        'age': age
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'


@pytest.mark.asyncio
async def test_update_without_surname(tester, create_user):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'


@pytest.mark.asyncio
async def test_update_without_name(tester, create_user):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'surname': user['surname'],
        'phone': user['phone'],
        'age': user['age']
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'


@pytest.mark.asyncio
async def test_update_without_age(tester, create_user):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': user['surname'],
        'phone': user['phone']
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'


@pytest.mark.asyncio
async def test_update_without_phone(tester, create_user):
    user = await create_user
    request = {
        'id': get_id(),
        'method': 'update',
        'name': user['name'],
        'surname': user['surname'],
        'age': user['age']
    }
    response = await tester.send_request(request)
    assert is_valid(response, UPDATE) is True
    assert response['status'] == 'failure', 'user was updated'
