#!/usr/bin/python3
"""Script to get todos for a user from API"""

try:
    import requests  # type: ignore
except Exception:
    # Minimal fallback using urllib if requests isn't installed
    import urllib.request
    import json

    class _Response:
        def __init__(self, data):
            self._data = data

        def json(self):
            return json.loads(self._data.decode('utf-8'))

    class requests:
        @staticmethod
        def get(url):
            with urllib.request.urlopen(url) as resp:
                data = resp.read()
            return _Response(data)

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: {} USER_ID".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)

    total_questions = 0
    completed = []
    for todo in response.json():

        if todo['userId'] == user_id:
            total_questions += 1

            if todo['completed']:
                completed.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), total_questions))
    print(printer)
    for q in completed:
        print("\t {}".format(q))


if __name__ == "__main__":
    main()
