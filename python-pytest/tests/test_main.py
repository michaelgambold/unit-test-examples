import pytest
from pytest_mock import MockerFixture

from python_pytest.main import handler
from python_pytest import api


def test_handler_success(mocker: MockerFixture):
    # Arrange
    mocked_get_data = mocker.patch.object(
        api,
        "get_data",
        return_value={"firstName": "John", "lastName": "Smith"},
    )

    # Act
    result = handler()

    # Assert
    assert result == {
        "firstName": "John",
        "lastName": "Smith",
    }
    mocked_get_data.assert_called_once_with()


def test_handler_returns_none(mocker: MockerFixture):
    # Arrange
    mocked_get_data = mocker.patch.object(
        api,
        "get_data",
        return_value=None,
    )

    # Act
    result = api.get_data()

    # Assert
    assert result == None
    mocked_get_data.assert_called_once_with()


def test_exception_is_not_caught(mocker: MockerFixture):
    # Arrange
    mocked_get_data = mocker.patch.object(
        api,
        "get_data",
        side_effect=ValueError("Some Random Error"),
    )

    # Act
    with pytest.raises(ValueError) as exc:
        api.get_data()

    # Assert
    assert str(exc.value) == "Some Random Error"
    mocked_get_data.assert_called_once_with()
