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

def get_employee_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))
    todos_response = requests.get(url + "todos", params={"userId": user_id})

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()
    return user, todos

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user, todos = get_employee_todos(employee_id)
    username = user.get("username")

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["Task ID", "Employee ID", "Employee Name", "Completed", "Title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos:
            writer.writerow({
                "Task ID": todo.get("id"),
                "Employee ID": employee_id,
                "Employee Name": username,
                "Completed": todo.get("completed"),
                "Title": todo.get("title")
            })

    print(f"Data for Employee {username} exported to {employee_id}.csv successfully.")
