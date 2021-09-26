from django.shortcuts import render

# Create your views here.
BAD_NUMS = [2,3,4]
visits_main = []

def main(request):
    k = request.session.get('count_main', 1)
    request.session['count_main'] = k+1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'main.html', context={'count': k, 'after_k': after_k})
    else:
        pass

def profile(request):
    k = request.session.get('count_profile', 1)
    request.session['count_profile'] = k + 1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'profile.html', context={'count': k, 'after_k': after_k})
    else:
        pass

def news(request):
    k = request.session.get('count_news', 1)
    request.session['count_news'] = k + 1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'news.html', context={'count': k, 'after_k': after_k})
    else:
        pass
