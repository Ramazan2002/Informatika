from django.shortcuts import render
# Create your views here.
BAD_NUMS = [2,3,4]
A = 0
B = 0
C = 0

def main(request):
    global A
    k = A + 1
    A += 1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'main.html', context={'count': k, 'after_k': after_k})
    else:
        pass

def profile(request):
    global B
    k = B + 1
    B += 1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'profile.html', context={'count': k, 'after_k': after_k})
    else:
        pass

def news(request):
    global C
    k = C + 1
    C += 1
    after_k = 'раз'
    if request.method == "GET":
        if k % 10 in BAD_NUMS and ((k < 100 and (k > 20 or k<10)) or (k > 100 and (k > 20 or k < 10))):
            after_k = 'раза'
        return render(request, 'news.html', context={'count': k, 'after_k': after_k})
    else:
        pass
