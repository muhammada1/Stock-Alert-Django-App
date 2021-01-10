from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import WatchList, Stock
from .forms import CreateNewList


# Create your views here.

def home(response):
    return render(response, "templates/home.html", {})

def index(response, id):
    ls = WatchList.objects.get(id=id)

    if ls in response.user.watchlist.all():

        
        if response.method == "POST":
            if response.POST.get("save"):
                for stock in ls.stock_set.all():
                    if response.POST.get("c" + str(stock.id)) == "clicked":
                        stock.delete()
                    else:
                        stock.complete = False
                    
                    #item.save()
            
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                trget = response.POST.get("target")

                if len(txt) > 0:
                    ls.stock_set.create(text=txt, complete=False, target=trget)

                else:
                    print("invalid")


        return render(response, "list.html", {"ls":ls})
    return render(response, "templates/view.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = WatchList(name=n)
            t.save()
            response.user.watchlist.add(t)

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "templates/create.html", {"form":form})

def view(response):
    return render(response, "templates/view.html", {})