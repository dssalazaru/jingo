from django.shortcuts import render
from django.http import HttpResponse
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
    elements = ''
    lsts = obj.all()
    for lst in lsts:
        elements += '<tr style="text-align:center;"><td style="padding: 0 3rem;">'+str(lst.id)+'</td><td style="padding: 0 3rem;">'+lst.name+'</td></tr>'
    html = f'''
    <center><h1>Listados</h1>
    <h2>http://localhost:8000/sqlite/tdlst/[id]</h2>
    <table>
    <tr>
    <th>ID</th><th>Task</tg>
    </tr>
    {elements}
    </table></center>
    '''
    return HttpResponse(html)

def getList(response, idlist):
    elements = ''
    try:
        lst = obj.get(id=idlist)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    try:
        items = lst.item_set.all()
        if len(items) == 0: return HttpResponse('<center><h1>%s</h1><h2>No hay nada para mostrar</h2></center>' %(lst.name))
        for item in items:
            elements += '<tr style="text-align:center;"><td style="padding: 0 3rem;">'+str(item.id)+'</td><td style="padding: 0 3rem;">'+item.text+'</td></tr>'
        html = f'''
        <center><h1>{lst.name}</h1>
        <table>
        <tr>
        <th>ID</th><th>Task</tg>
        </tr>
        {elements}
        </table></center>
        '''
    except Exception as e:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>Error en la tabla:</h2>%s</center>' %(e))
    return HttpResponse(html)

def getItem(response, idlist, iditem):
    try:
        lst = obj.get(id=idlist)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    try:
        item = lst.item_set.get(id=iditem)
        html = f'''
        <center><h1>{lst.name}</h1>
        <table>
        <tr>
        <th>ID</th><th>Task</tg>
        </tr>
        <tr style="text-align:center;">
        <td style="padding: 0 3rem;">{str(item.id)}</td><td style="padding: 0 3rem;">{item.text}</td>
        </tr>
        </table></center>
        '''
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>No se encontro el Item de ID: %s</h2></center>' %(iditem))
    return HttpResponse(html)

def addList(response, name):
    new = ToDoList(name=name)
    new.save()
    td = obj.get(name=name)
    return HttpResponse('<center><h2>New list created:</h2> %s</center>' %(td.name))

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
    
def delItem(response, idlist, iditem):
    try:
        lst = obj.get(id=idlist)
        item = obj.get(id=idlist).item_set.get(id=iditem)
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>La lista no existe con ID: %s</h2></center>' %(idlist))
    try:
        itemText = item.text
        item.delete()
    except:
        return HttpResponse('<center><h1 style="color:red">ERROR</h1><h2>Can\'t remove: %s</h2></center>' %(idlist))
    return HttpResponse('<center><h1>%s</h1><h2 style="color:red">Item removed: </br>ID: %s</br>Task: %s</h2></center>' %(lst.name, iditem, itemText))
