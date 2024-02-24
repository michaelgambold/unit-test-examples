from python_pytest import api


def handler():
    data = api.get_data()
    return data
