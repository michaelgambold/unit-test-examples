import httpx

BASE_URL = "http://example.com"


def get_data() -> dict | None:
    response = httpx.get(f"{BASE_URL}/api/data")

    if response.status_code == 404:
        return None
    elif response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        raise ValueError("Something went wrong")
