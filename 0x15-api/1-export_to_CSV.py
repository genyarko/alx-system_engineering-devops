#!/usr/bin/python3
"""
Module: gather_data_from_an_API
Script to fetch TODO list progress for a given employee ID using REST API and export data to CSV format.
Usage:
    python3 gather_data_from_an_API.py <employee_id>
"""

import sys
import requests
import csv

def get_employee_todo_list_progress(employee_id):
    """
    Fetch and display the TODO list progress for the given employee ID and export to CSV format.
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

    csv_file = f'{employee_id}.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_id = task['id']
            task_title = task['title']
            task_status = "COMPLETED" if task['completed'] else "INCOMPLETE"
            writer.writerow([task_id, employee_name, task_status, task_title])

    print(f"Employee {employee_name} data exported to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
