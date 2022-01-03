from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TodoItem

def homePageView(request):
    allTodoItems = TodoItem.objects.all()
    return render(request, 'homePage.html',
        {'allTodoItems': allTodoItems})

def addTodoView(request):
    # create a new todo item, save it, and redirect to 'homePage'
    newItem = TodoItem(content = request.POST['content'])
    newItem.save()
    return HttpResponseRedirect('/homePage/')

def deleteTodoView(request, todoId):
    #delete an existing todo item, and redirect to 'homePage'
    deletedItem = TodoItem.objects.get(id = todoId)
    deletedItem.delete()
    return HttpResponseRedirect('/homePage/')