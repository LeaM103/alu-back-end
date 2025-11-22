#!/usr/bin/env python3
import json
import urllib.request

# Get users
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

with urllib.request.urlopen(users_url) as u:
    users_response = json.load(u)
with urllib.request.urlopen(todos_url) as u:
    todos_response = json.load(u)

# Build dictionary
data = {}

for user in users_response:
    user_id = str(user["id"])
    username = user["username"]
    data[user_id] = []

    for todo in todos_response:
        if todo["userId"] == user["id"]:
            data[user_id].append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            })

# Write to JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(data, f)
