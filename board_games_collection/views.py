from django.shortcuts import render
from django.http import HttpResponse
from board_games_collection.parsing.data_from_Internet import UserFromInternet


def index(request):
    # UserFromInternet('pych1971')
    return HttpResponse("Hello, world. You're at the polls index.")