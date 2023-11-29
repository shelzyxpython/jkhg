from django.shortcuts import render
from django.http import HttpResponse


def index(request, name, age):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'host: {host} <br> browser: {user_agent} <br> Path: {path} <br>'
                        f'user: {name}, age: {age}',
                        headers={'SecretC0de': ' 12345678'})



