import pytest
from pytest_httpx import HTTPXMock
from python_pytest.api import get_data


def test_valid_response(httpx_mock: HTTPXMock):
    # Arrange
    httpx_mock.add_response(
        status_code=200,
        json={
            "firstName": "John",
            "lastName": "Smith",
        },
        url="http://example.com/api/data",
    )

    # Act
    data = get_data()

    # Assert
    assert data == {
        "firstName": "John",
        "lastName": "Smith",
    }


def test_return_none_for_400_status_code(httpx_mock: HTTPXMock):
    # Arrange
    httpx_mock.add_response(status_code=404, json={}, url="http://example.com/api/data")

    # Act
    data = get_data()

    # Assert
    assert data is None


def test_exception_raised_for_500_status_code(httpx_mock: HTTPXMock):
    # Arrange
    httpx_mock.add_response(
        status_code=500,
        json={"message": "Internal Server Error"},
        url="http://example.com/api/data",
    )

    # Act
    with pytest.raises(ValueError) as exc:
        get_data()

    # Assert
    assert str(exc.value) == "Something went wrong"
