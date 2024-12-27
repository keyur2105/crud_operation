from django.shortcuts import render, HttpResponse, redirect

data=[]
def data_input(request):
    return render(request, "input.html", {"values" : {}, "updateId": ""})

def data_view(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    id = request.GET.get('uid')
    if name and password:
        if id and int(id) >= 0:
            data[int(id)]['name'] = name
            data[int(id)]['password'] = password
        else:
            data.append({"id":(int(len(data)-1))+1, "name":name, 'password': password})
            print(data)
    context={ "data" : data }
    return render(request, "data.html", context)
                                                             
def deletedata(request):
    id = request.GET.get('del')
    if id:
        global data
        data = [x for x in data if str(x['id']) !=  str(id)]
        return redirect(f"/get")
    else:
        return render(request,"data.html")

def updatedata(request):
    id = request.GET.get('update')

    context= {
        'values' : data[int(id)],
        'updateId': int(id)
    }
    return render(request,"input.html", context)
    

          


  
 

    











