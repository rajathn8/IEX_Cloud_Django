from django.shortcuts import render , redirect
import requests
import json
from . models import Stock

from .forms import StockForm
from django.contrib import messages
# Create your views here.

# most important point of the app.

# request is a browser request --

def home(request):
    # this is making the home directry specified by the rajath
    import requests
    import json
    
    if request.method=='POST':

        ticker=request.POST['ticker']
        api_request= requests.get(f"https://sandbox.iexapis.com/stable/stock/{ticker}/quote?token=Tpk_6147abc064d64c0ab788c13bb623730a")

        try:
            api=json.loads(api_request.content)

        except Exception as e:
            api='Error...'
            print(e)
        return render(request,'home.html',{'api':api})

    else:
        return render(request,'home.html',{'ticker':"Enter a ticker "})

def about(request):

    return render(request,'about.html',{})

def home_second(request):

    api_request= requests.get("https://sandbox.iexapis.com/stable/stock/AAPL/quote?token=Tpk_6147abc064d64c0ab788c13bb623730a")

    try:
        api=json.loads(api_request.content)

    except Exception as e:
        api='Error...'
        print(e)

    return render(request,'home.html',{'api':api})


def add_stock(request):
    # using actual django form system
    
    import requests
    import json

    if request.method=='POST':

        form = StockForm(request.POST or none)

        if form.is_valid():

            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')

    else:
        
        ticker = Stock.objects.all()

        output=[]

        for ticker_item in ticker:

            ticker_item=str(ticker_item) # because database retrieve is an object 
            api_request= requests.get(f"https://sandbox.iexapis.com/stable/stock/{ticker_item}/quote?token=Tpk_6147abc064d64c0ab788c13bb623730a")

            try:
                api=json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api='Error...'
                print(e)

        return render(request,'add_stock.html',{'ticker':ticker, "output": output})

def delete(request,stock_id):
# calls the delete function -- takes the stock id --- deletes the entry and then returns the database'''
    item = Stock.objects.get(pk=stock_id)
    item.delete()

    messages.success(request, (" Stock has been deleted "))
    return redirect(delete_stock)

def delete_stock_add(request,stock_id):
# calls the delete function -- takes the stock id --- deletes the entry and then returns the database'''
    item = Stock.objects.get(pk=stock_id)
    item.delete()

    messages.success(request, (" Stock has been deleted "))
    return redirect(add_stock)

def delete_stock(request):

    ticker=Stock.objects.all()

    return render(request,'delete_stock.html',{"ticker":ticker})


'''
 what is the { } --- it allows us to send information to the HTML page.

things in your database are objects

'''
'''

pk_a96bbe08204a4c7fbc29332d2afdc7e3
connect the api - get- collect 

understand django forms.

redirects to a different page

'''