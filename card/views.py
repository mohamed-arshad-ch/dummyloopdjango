from django.shortcuts import render,HttpResponse
from .models import Mymembers

# Create your views here.
def index(request):
    obj1 = Mymembers()
    obj1.name = "Arshad"
    obj1.age = 19
    obj1.place = "Malappuram"
    obj1.imageadd = "https://mohamed-arshad-ch.github.io/Personal-Website/me.jpeg"


    obj2 = Mymembers()
    obj2.name = "Vyshnav"
    obj2.age = 20 
    obj2.place = "Vadakara"
    obj2.imageadd = "https://akkuvy.github.io/PersonalWebsite/da.png"

    obj3 = Mymembers()
    obj3.name = "Sharath"
    obj3.age = 26
    obj3.place = "Nilamboor"
    obj3.imageadd = "http://sarathrj10.tk/assets/images/sarath.jpg"


    new = [obj1,obj2,obj3]
   
    return render(request,'index.html',{'objk':new})
    #return HttpResponse("<h1>Hello</h1>")
