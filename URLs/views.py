from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import URLs
import string
from random import choice
# Create your views here.
def url_fetch_short(request): 
    obj = URLs.objects.get(id=1)
    content = {
        'url' : obj.url, 
        'short_url' : obj.short_url
    }
    print(content)
    return render(request, "short_url.html", content)

def home_view(request, *args, **kwargs):
    data = request.POST.get('url')
    new_url = ""
    content = {
        'url' : None
    }
    print(data)
    if data:
        short_id = generate_short_id(8)
        print(short_id)
        print(request.get_host()+short_id)
        new_url = request.get_host()+"/"+short_id
        try:
            ans = URLs.objects.get(url = data)
        except URLs.DoesNotExist:
            ans = False
        print(ans)
        if ans:
            content = {
                'url' : ans.short_url
            }
        else:
            URLs.objects.create(url=data,short_url=new_url)
            content = {
                'url' : new_url
            }
    
    print(content)
    return render(request, 'home.html', content)


def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

def redirect_url(request,text):
    print(request, text)
    ans = URLs.objects.get(short_url=request.get_host()+"/"+text)
    print(ans.url)
    if ans.url:
        link = "https://www.youtube.com/watch?v=r9kT-jm136Q&ab_channel=PrettyPrinted"
        return HttpResponseRedirect(ans.url)
    else:
        return render(request, 'home.html', None)