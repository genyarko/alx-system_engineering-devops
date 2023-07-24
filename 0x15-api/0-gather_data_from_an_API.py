#!/usr/bin/python3
"""
Module: gather_data_from_an_API

Script to fetch TODO list progress for a given employee ID using REST API.

Usage:
    python3 gather_data_from_an_API.py <employee_id>
"""

import sys
import requests

def get_employee_todo_list_progress(employee_id):
    """
    Fetch and display the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    user_data = response_user.json()
    todos_data = response_todos.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
