from django.shortcuts import render
from django.http import HttpResponse


def error(request):
    return HttpResponse('К сожалению произошла ошибка')


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    return HttpResponse(f'host: {host} <br> browser: {user_agent} <br> Path: {path} <br>')


def user(request, username, folder, post_id):
    return HttpResponse(f"Username: {username} <br> Folder: {folder} <br> Post ID: {post_id}")
