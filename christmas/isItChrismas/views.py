from django.shortcuts import render
from datetime import datetime 



# Create your views here.
def index(request):
    today = datetime.now()
    year = today.year
    christmas = datetime(year, 12, 25)

    daysLeft = christmas-today
    return render(request, "christmas/index.html", {
        "christmas":today.day==25 and today.month==12,
        "daysLeft":daysLeft.days
    })
