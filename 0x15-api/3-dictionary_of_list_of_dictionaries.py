#!/usr/bin/python3
"""Returns information about employee TODO list progress"""
import json
import requests
import sys


def users_all(id=None):
    url = 'https://jsonplaceholder.typicode.com/users'
    if id is not None:
        url += '/' + id
    r = requests.get(url)
    return r.json()


def todos_all(userId, done=None):
    url = 'https://jsonplaceholder.typicode.com/users/' + userId + '/todos'
    if done is not None:
        if done:
            url += '?completed=true'
        else:
            url += '?completed=false'
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    users = users_all()

    filename = 'todo_all_employees.json'

    data = {}
    for user in users:
        data[user['id']] = []
        todos = todos_all(str(user['id']))
        for todo in todos:
            data[user['id']].append({
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']})

    with open(filename, 'w+') as the_file:
        json.dump(data, the_file)
