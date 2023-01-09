from django.shortcuts import render, get_object_or_404


def get_menu(request, pk=None):
    context = {}
    return render(request, 'main.html', context)
