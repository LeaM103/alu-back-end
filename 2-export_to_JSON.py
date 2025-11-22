#!/usr/bin/env python3
"""
Exports all tasks of a given employee ID to JSON format.
Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
# Get employee info
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

try:
    with urllib.request.urlopen(user_url) as resp:
        user_bytes = resp.read()
        user_text = user_bytes.decode('utf-8')
        user_data = json.loads(user_text)

    with urllib.request.urlopen(tasks_url) as resp:
        tasks_bytes = resp.read()
        tasks_text = tasks_bytes.decode('utf-8')
        tasks_data = json.loads(tasks_text)
except urllib.error.URLError as e:
    print(f"Error fetching data: {e}")
    sys.exit(1)

username = user_data.get("username")

# Prepare JSON structure
output_data = {
    employee_id: [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in tasks_data
    ]
}

# Write to JSON file named <USER_ID>.json
filename = f"{employee_id}.json"
with open(filename, 'w') as f:
    json.dump(output_data, f)

print(f"Data exported to {filename}")
