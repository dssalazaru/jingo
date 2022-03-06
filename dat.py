'''

CREATE NEW PROJECT: django-admin startproject [name]

RUN SERVER: python manage.py runserver [5500] <- opcional port (default 8000)
CREATE NEW APP: python manage.py startapp [name] (example main)
SIMULATE UPDATE APP: python manage.py makemigrations main
UPDATE APP: python manage.py migrate

- in main dir, edit views.py and import: from django.http import HttpResponse
- in django project, django dir, edit settings.py and add in: INSTALLED_APPS = [ '[name].apps.[Name]Config', ]

=== Console test, DB

from main.models import Item, ToDoList 
t = ToDoList(name='ToDo DSSU')  
t.save()
ToDoList.objects.all()
    <QuerySet [<ToDoList: ToDo DSSU>]>
ToDoList.objects.get(id=1) 
    <ToDoList: ToDo DSSU>
ToDoList.objects.get(name='ToDo DSSU')
    <ToDoList: ToDo DSSU>
t.item_set.all()
    <QuerySet []>
t.item_set.create(text='Go to Sleep', complete=False)
    <Item: Go to Sleep>
t.item_set.all()
    <QuerySet [<Item: Go to Sleep>]>
    
t = ToDoList.objects
t.all()
t.filter(name__startswith="aaa")
t.filter(id=1)
item = t.get(id=1)
item.delete()
===
















'''