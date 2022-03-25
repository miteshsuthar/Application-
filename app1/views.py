from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.


def xyz(request):
    return render(request, "index.html")


def signUp(request):
    email = request.GET['email']
    psw = request.GET['psw']
    cursor = connection.cursor()
    query = "insert into users (email,psw) values(%s,%s)"
    value = (email, psw)
    cursor.execute(query, value)
    print(cursor.rowcount)
    data = {"email": email, "psw": psw}
    return render(request, "first.html", data)
    # query = '''Select * from city where id=11'''
    # row = cursor.fetchone()
    # print(row)
    # query = "Select * from city where name ='"+email+"'"

