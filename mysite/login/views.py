from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
url = "http://localhost:3000"
r = requests.Session()


def login(request):
    statusCode = ""
    if request.method == "POST":
        login_data = request.POST.dict()
        number = login_data.get("username")
        password = login_data.get("pass")
        res = r.post(url + "/login/admin", data={"contact": number, "password": password})
        statusCode += str(res.status_code)
        if res.status_code == 200:
            # Setting the header for the entire session
            request.session['x-auth'] = res.headers['x-auth']
            r.headers.update({"x-auth": res.headers['x-auth']})
            print("header " + str(res.headers['x-auth']))
            # new_response = r.get(url + "/admin/getAllUsers")
            # statusCode += str(new_response.status_code)
            print(statusCode)
        return render(request, 'login/admin panel/add-menu.html')
    return render(request, 'login/index.html')


def add_item(request):
    if 'x-auth' not in request.session:
        return  render(request, 'login/index.html')
    if request.method == "POST":
        item_data = request.POST.dict()
        item_name = item_data.get("item_name")
        desc = item_data.get("description")
        min = item_data.get("minimum")
        max = item_data.get("maximum")
        expiry = item_data.get("expiry")
        weight = item_data.get("weight")
        type = item_data.get("type_data")
        print({"item": item_name, "description": desc,
                                           "min_count": min, "max_count": max,
                                           "expiry": expiry, "weight": weight, "type": type})
        res = r.post(url + "/gobag/admin", data={"name": item_name, "description": desc,
                                           "min_count": min, "max_count": max,
                                           "expiry": expiry, "weight": weight, "type": type})
        if res.status_code == 200:
            print(res.text)
            return render(request, 'login/admin panel/add-menu.html', {"message": item_name + " Saved Successfully!"})
        else:
            print(str(res.status_code)+ " "+ res.text)
            return render(request, 'login/admin panel/add-menu.html', {"message": item_name + " Doesn't Saved!"})
    return render(request, 'login/admin panel/add-menu.html')



# Logout Page
def logout(request):
    if 'x-auth' not in request.session:
        return  render(request, 'login/index.html')
    res = r.get(url + "/logout")
    print(str(res.status_code))
    if res.status_code ==200:
        del request.session['x-auth']
        return render(request, 'login/index.html')