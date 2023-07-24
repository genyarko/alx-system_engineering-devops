#!/usr/bin/python3

"""
Module: gather_data_from_an_API

Script to fetch TODO list progress for all employees using REST API and export data to JSON format.

Usage:
    python3 gather_data_from_an_API.py
"""

def get_employee_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    todos_response = requests.get(url + "todos", params={"userId": user_id})

    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch data for Employee ID: {user_id}")
        return []

    return todos_response.json()

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(url + "users")

    if users_response.status_code != 200:
        print("Error: Unable to fetch users' data from the API.")
        exit(1)

    users = users_response.json()

    all_employees_data = {}
    for user in users:
        employee_id = user.get("id")
        username = user.get("username")
        todos = get_employee_todos(employee_id)

        all_employees_data[employee_id] = {
            "username": username,
            "todos": [
                {
                    "task_id": todo.get("id"),
                    "title": todo.get("title"),
                    "completed": todo.get("completed")
                }
                for todo in todos
            ]
        }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees_data, jsonfile, indent=4)

    print("Data for all employees exported to todo_all_employees.json successfully.")
