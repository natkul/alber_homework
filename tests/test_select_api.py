import pytest

from schemas.response_schemas import SELECT
from utils.user import get_user
from utils.validator import is_valid


@pytest.mark.asyncio
async def test_select_by_name(tester, prepare_data):
    data = await prepare_data
    name = data[0]['name']
    user_info = {
        'name': name,
    }

    response = await get_user(tester, user_info)

    for user in response['users']:
        assert user['name'] == name

    assert is_valid(response, SELECT) is True
    assert response['status'] == 'success'


@pytest.mark.asyncio
async def test_select_by_surname(tester, prepare_data):
    data = await prepare_data
    surname = data[0]['surname']
    user_info = {
        'surname': surname,
    }

    response = await get_user(tester, user_info)

    for user in response['users']:
        assert user['surname'] == surname

    assert is_valid(response, SELECT) is True
    assert response['status'] == 'success'


@pytest.mark.asyncio
async def test_select_by_phone(tester, prepare_data):
    data = await prepare_data
    phone = data[0]['phone']
    user_info = {
        'phone': phone,
    }

    response = await get_user(tester, user_info)

    assert len(response['users']) == 1
    assert response['users'][0]['phone'] == phone
    assert is_valid(response, SELECT) is True
    assert response['status'] == 'success'
