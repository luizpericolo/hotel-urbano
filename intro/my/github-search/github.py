import requests

URLS = {
    "USER_API_URL": "https://api.github.com/users/{}"
}

def _fetch_user_data(username):
    url = URLS.get("USER_API_URL").format(username)

    response = requests.get(url)
    return response.json()


def avatar(username):
    user_data = _fetch_user_data(username)

    return user_data.get("avatar_url")


if __name__ == "__main__":
    user_data = avatar("luizpericolo")
    print("User data:")
    print(user_data)
