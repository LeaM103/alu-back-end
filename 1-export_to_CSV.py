#!/usr/bin/python3
"""
Exports data for a given employee ID to CSV format.
"""

import csv
import sys
import urllib.request
import urllib.error
import json


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Base URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    # Fetch user info
    try:
        with urllib.request.urlopen(user_url) as resp:
            user = json.load(resp)
    except urllib.error.URLError as e:
        print(f"Error fetching user: {e}")
        sys.exit(1)
    username = user.get("username")

    # Fetch tasks
    try:
        with urllib.request.urlopen(todos_url) as resp:
            todos = json.load(resp)
    except urllib.error.URLError as e:
        print(f"Error fetching todos: {e}")
        sys.exit(1)

    # CSV file name
    filename = f"{employee_id}.csv"

    # Write to CSV
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
