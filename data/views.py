from django.shortcuts import render, HttpResponse, redirect


def data_input(request):
    name = request.GET.get('name')
    password = request.GET.get('pw')
    # print("1",name, password)
    
    if name and password:
        return render(request, "data.html")
    else:
        return render(request, "input.html", {"error" : "Required all field"})

data=[]

def data_view(request):

    name = request.GET.get('name')
    password = request.GET.get('pw')
    # print("2",name, password)

    if name and password:
        data.append({"id":len(data)+1, "name":name, 'password': password})
        print(data)

    context={ "data":data }
    # print(context)
    return render(request, "data.html", context)
                                                    
def deletedata(request):
    id = request.GET.get('del')
    if id:
        global data
        data = [x for x in data if str(x['id']) != str(id)]
        return redirect(f"/get")
    else:
        return render(request,"data.html")

def updatedata(request):
    id = request.GET.get('update')
    print("id",id)

    if id:
        global data
        data_on_id = lambda n : str(n['id']) == str(id)  
        f_data = list(filter(data_on_id, data))
        print("data",list(f_data))

        context= {
            'f_data' : f_data[0]
            }
        return render(request,"input.html", context)
    else:
        return HttpResponse("id is not found")
    


  
 

    











