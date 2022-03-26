from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewList
from .models import ToDoList, Item

# Create your views here.

obj = ToDoList.objects

def index(response):
    lsts = obj.all()
    return render(response, 'tdlst/list.html', {'lsts':lsts})

def todo(response, idlist):
    lst = obj.get(id=idlist)
   
    if lst in response.user.todolist.all():
        try:
            items = lst.item_set.all()
            
            if response.method == 'POST':
                print(response.POST)
                if response.POST.get('save'):
                    for item in items:
                        item.complete = True if response.POST.get('c'+str(item.id)) == 'clicked' else False
                        item.save()
                elif response.POST.get('newItem'):
                    txt = response.POST.get('new')
                    if len(txt) > 2:
                        lst.item_set.create(text=txt.strip(), complete=False)
                    else: print('invalid')
                elif response.POST.get('edit'):
                    return HttpResponseRedirect('%i/edit' %lst.id)
                    
                    # edit = False if edit else True
                    # print(edit)
        except Exception as e:
            return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>Error en la tabla:</h2>%s</center>' %(e))
        return render(response, 'tdlst/todo.html', {'lst': lst,'items':items})
    return render(response, 'tdlst/view.html', {})
    
def edit(response, idlist):
    lst = obj.get(id=idlist)
    items = lst.item_set.all()
    if response.method == 'POST':
        print(response.POST)
        if response.POST.get('save'):
            for item in items:
                item.complete = True if response.POST.get('c'+str(item.id)) == 'clicked' else False
                item.save()
        elif response.POST.get('newItem'):
            txt = response.POST.get('new')
            if len(txt) > 2:
                lst.item_set.create(text=txt.strip(), complete=False)
            else: print('invalid')
        elif response.POST.get('rem'):
            for item in items:
                if str(item.id) == response.POST['rem']: item.delete()
        elif response.POST.get('edit'):
            return HttpResponseRedirect('/tdlst/%i' %lst.id)
        elif response.POST.get('del'):
            lst.delete()
            return HttpResponseRedirect('/tdlst')
        items = lst.item_set.all()
    return render(response, 'tdlst/edit.html', {'lst':lst,'items':items})

def addItem(response, idlist, text):
    try:
        lst = obj.get(id=idlist)
        item = lst.item_set.create(text=text.strip(), complete=False)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    return HttpResponse('<center><h2>New item created on %s</h2>%s</center>' %(lst.name, item.text))

def delList(response, idlist):
    try:
        lst = obj.get(id=idlist)
        item = lst.name
        lst.delete()
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    return HttpResponse('<center><h2 style="color:red">List removed: %s</h2></center>' %(item))

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
            return HttpResponseRedirect('/tdlst/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'tdlst/create.html', {'form':form})

def view(response):
    print(response.path)
    return render(response, 'tdlst/view.html', {})