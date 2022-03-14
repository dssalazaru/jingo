from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewList
from .models import ToDoList, Item

# Create your views here.

'''
getList
getItem
addList
addItem
delList
delItem
'''

obj = ToDoList.objects

def index(response):
    lsts = obj.all()
    return render(response, 'tdlst/list.html', {'lsts':lsts})
    # elements = ''
    # for lst in lsts:
    #     elements += '<tr style="text-align:center;"><td style="padding: 0 3rem;">'+str(lst.id)+'</td><td style="padding: 0 3rem;">'+lst.name+'</td></tr>'
    # html = f'''
    # <center><h1>Listados</h1>
    # <h2>http://localhost:8000/sqlite/tdlst/[id]</h2>
    # <table>
    # <tr>
    # <th>ID</th><th>Task</tg>
    # </tr>
    # {elements}
    # </table></center>
    # '''
    # return HttpResponse(html)

def todo(response, idlist):
    try:
        lst = obj.get(id=idlist)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
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


        # if len(items) == 0: return HttpResponse('<center><h1>%s</h1><h2>No hay nada para mostrar</h2></center>' %(lst.name))
        # for item in items:
        #     elements += '<tr style="text-align:center;"><td style="padding: 0 3rem;">'+str(item.id)+'</td><td style="padding: 0 3rem;">'+item.text+'</td></tr>'
        # html = f'''
        # <center><h1>{lst.name}</h1>
        # <table>
        # <tr>
        # <th>ID</th><th>Task</tg>
        # </tr>
        # {elements}
        # </table></center>
        # '''

    
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
            return HttpResponseRedirect('/sqlite/tdlst/%i' %lst.id)
        items = lst.item_set.all()
    return render(response, 'tdlst/edit.html', {'lst':lst,'items':items})

    # try:
        # lst = obj.get(id=idlist)
        # item = obj.get(id=idlist).item_set.get(id=iditem)
    # except:
        # return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    # try:
        # itemText = item.text
        # item.delete()
    # except:
        # return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>Can\'t remove: %s</h2></center>' %(idlist))
    # return HttpResponse('<center><h1>%s</h1><h2 style="color:red">Item removed: </br>ID: %s</br>Task: %s</h2></center>' %(lst.name, iditem, itemText))



'''
def getItem(response, idlist, iditem): # OFF - Unnecesary
    try:
        lst = obj.get(id=idlist)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    try:
        item = lst.item_set.get(id=iditem)
        html = f"""
        <center><h1>{lst.name}</h1>
        <table>
        <tr>
        <th>ID</th><th>Task</tg>
        </tr>
        <tr style="text-align:center;">
        <td style="padding: 0 3rem;">{str(item.id)}</td><td style="padding: 0 3rem;">{item.text}</td>
        </tr>
        </table></center>
        """
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>No se encontro el Item de ID: %s</h2></center>' %(iditem))
    return HttpResponse(html)
'''

def addList(response, name):
    new = ToDoList(name=name)
    new.save()
    return HttpResponseRedirect('/sqlite/tdlst/%i' %new.id)

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
            return HttpResponseRedirect('/sqlite/tdlst/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'tdlst/create.html', {'form':form})

