from django.shortcuts import render, HttpResponse, redirect

data=[]

def data_input(request):
    name = request.GET.get('name')
    password = request.GET.get('pw')
    print("1",name, password)
    
    if name and password:
        # data.append({"id":len(data)+1, "name":name, 'password': password})
        # print(data)
        return redirect('get/')
    else:
        return render(request, "input.html", {"error" : "Required all field"})

def data_view(request):
    name = request.GET.get('name')
    password = request.GET.get('pw')
    print("2",name, password)

    context={ "data":data }
    print(context)
    return render(request, "data.html", context)
    
    # if name and password:

    #     context={
    #         "id":count+1,
    #         'name':name,
    #         'password':password
    #     }
    #     return render(request, 'data.html', context)
    # else:
    #     return redirect('/')

def deletedata(request):
    id = request.GET.get("del")
    del id

    return render(request, "data.html")






