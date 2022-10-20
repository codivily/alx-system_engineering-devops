#!/usr/bin/python3
"""Returns information about employee TODO list progress"""
import requests
import sys


def users(id):
    r = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
    return r.json()


def todos(userId, done=None):
    url = 'https://jsonplaceholder.typicode.com/users/' + userId + '/todos'

    if done is not None:
        if done:
            url += '?completed=true'
        else:
            url += '?completed=false'
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0)

    userId = sys.argv[1]

    if not userId.isnumeric():
        sys.exit(0)

    user = users(userId)
    todos = todos(userId)
    completed_todos = [todo for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'],
        len(completed_todos),
        len(todos)))

    for todo in completed_todos:
        print('\t' + todo['title'])
