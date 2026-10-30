from django.shortcuts import render
import re

def login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not re.match(r'^[a-zA-Z0-9]+$', username):
            message = "Invalid Username"

        elif not re.match(r'^[a-zA-Z0-9@#$]+$', password):
            message = "Invalid Password"

        else:
            message = "Login Successful"

    return render(request, 'login.html', {'message': message})