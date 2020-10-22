from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import TodoItem
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def signin(request):
    return HttpResponseRedirect("This is signin page")


def signup(request):

    return render(request, 'user/login_bkp.html')

def todoView(request):
    todo_items = TodoItem.objects.all().order_by("-added_date")
    constraints = {
        "todo_items": todo_items
    }
    return render(request, 'index.html', constraints)

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    
    TodoItem.objects.create(added_date=current_date, text=content)


    return HttpResponseRedirect('/todo')

@csrf_exempt
def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo')