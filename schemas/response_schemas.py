ADD = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'method': {
            'type': 'string',
            'const': 'add'
        },
        'status': {
            'type': 'string',
            'enum': ['success', 'failure']
        },
        'reason': {
            'type': 'string'
        }
    },
    'required': ['id', 'method', 'status'],
    'additionalProperties': False
}

DELETE = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'method': {
            'type': 'string',
            'const': 'delete'
        },
        'status': {
            'type': 'string',
            'enum': ['success', 'failure']
        },
        'reason': {
            'type': 'string'
        }
    },
    'required': ['id', 'method', 'status'],
    'additionalProperties': False
}

UPDATE = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'method': {
            'type': 'string',
            'const': 'update'
        },
        'status': {
            'type': 'string',
            'enum': ['success', 'failure']
        },
        'reason': {
            'type': 'string'
        }
    },
    'required': ['id', 'method', 'status'],
    'additionalProperties': False
}

SELECT = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'method': {'type': 'string', 'const': 'select'},
        'status': {'type': 'string', 'enum': ['success', 'failure']},
        'users': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'age': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'surname': {'type': 'string'}
                },
                'required': ['age', 'name', 'phone', 'surname'],
                'additionalProperties': False
            }
        }
    },
    'required': ['id', 'method', 'status', 'users'],
    'additionalProperties': False
}
