import jsonschema


def is_valid(response, schema):
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        return False
