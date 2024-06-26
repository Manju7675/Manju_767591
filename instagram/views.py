from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def HomePage(request):
    # return HttpResponse("Hello World")
    # name="Django"
    # type="Framework"
    # context={
    #     'name':name,
    #     'type':type,
    #     'fruits':['mango','apple','banana']
    # }
    
    students=[{
    "name": "manju",
    "age":"22",
    "number":"7675910036",
    "marks":90
    },
{
    "name": "vijay",
    "age":"23",
    "number":"7675918036",
    "marks":30
},
{
    "name": "pavan",
    "age":"24",
    "number":"7675980036",
    "marks":10
},
{
    "name": "shiva",
    "age":"25",
    "number":"7685910036",
    "marks":78,


}

    ]

    return render(request,"home.html",{"students":students})

# def temp(request):
#     return render(request/'home.html')