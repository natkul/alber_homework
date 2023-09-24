import random

from faker import Faker


def get_id():
    fake = Faker()
    return str(fake.uuid4())


def get_name():
    fake = Faker()
    return fake.first_name()


def get_surname():
    fake = Faker()
    return fake.last_name()


def get_phone():
    fake = Faker()
    return str(fake.phone_number())


def get_bool():
    return str(random.randint(0, 1))
