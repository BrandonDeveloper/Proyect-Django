"""Post views."""
#Django

from django.http import HttpResponse
from datetime import datetime

posts=[{
    "name":"Shingeky no Kioyin",
    "user":"Eren",
    "timestamp":datetime.now().strftime("%b %d, %Y - %H:%M hrs"),
    "picture":"https://i.pinimg.com/474x/92/de/ca/92decad2906d73d9e3a2a4381161e15c.jpg",
},
{
    "name":"Demon Slayer",
    "user":"Tanjero",
    "timestamp":datetime.now().strftime("%b %d, %Y - %H:%M hrs"),
    "picture":"https://arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/R2B4MI4BBVBVTKWJRROU2DD4S4.jpg",
},
{
    "name":"Los prisioneros del cielo",
    "user":"Los 7 pecados capitales",
    "timestamp":datetime.now().strftime("%b %d, %Y - %H:%M hrs"),
    "picture":"https://i.pinimg.com/originals/d4/28/c9/d428c9bc7985c98b9ecb07b666ec58ec.jpg",
},
{
    "name":"Faded",
    "user":"Alan Walker",
    "timestamp": datetime.now().strftime("%b %d, %Y - %H:%M hrs"),
    "picture":"https://rfmsomnii.com/wp-content/uploads/2020/02/Optimized-AW_AVIATION_11-CLEAN-1024x727.jpg"
}]    


def list_posts(request):
    content=[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}" title="Hi" height="500" width="500"></figure>
        """.format(**post))
    return HttpResponse("<br>".join(content))