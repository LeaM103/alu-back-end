#!/usr/bin/python3
"""
Python script that returns information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is given
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = f"{base_url}/users/{employee_id}"
    user = requests.get(user_url).json()

    # Get the employee's todos
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos = requests.get(todos_url).json()

    # Extract name and count tasks
    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display results
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
