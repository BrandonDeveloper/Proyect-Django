#Platzigram views 
from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now= datetime.now().strftime("%b %d, %Y - %H:%M hrs")
    return HttpResponse("Ohhh hi! Current server time {now}".format(now=now))

def sorted(request):
    numbers = [int(i) for i in request.GET["numbers"].split(",")]
    sorted_ints= sorted(numbers)
    data={
        "status":"Ok",
        "numbers":sorted_ints,
        "message":"Hi my name is Brandon and format json."
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
    )

def say_hi(request ,name,age):
    if age<12:
        message="Zorry {} no puedes pasar a platzigram".format(name)
    else:
        message="Hello {} welcome to platzigram".format(name) 
    return HttpResponse(message)      
