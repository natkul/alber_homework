from utils.generate_user_data import get_id


async def get_user(tester, body):
    user = {
        'id': get_id(),
        'method': 'select'
    }
    user.update(body)

    return await tester.send_request(user)
