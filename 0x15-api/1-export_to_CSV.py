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
    if not user:
        sys.exit(0)

    todos = todos(userId)

    filename = '{}.csv'.format(userId)

    with open(filename, 'a+') as the_file:
        line = '"{}","{}","{}","{}"\n'
        for todo in todos:
            the_file.write(line.format(
                userId,
                user['username'],
                todo['completed'],
                todo['title']))
