from django.shortcuts import render, redirect
from .forms import SimpleTextForm
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
    if request.method == 'POST':
        form = SimpleTextForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            age = request.POST['age']
            height = int(request.POST['height'])
            weight = int(request.POST['weight'])
            imt = weight/(height/100)**2
            if imt >= 40:
                description = 'Ожирение 3-й степени'
            elif 35 <= imt < 40:
                description = 'Ожирение 2-й степени'
            elif 30 <= imt < 35:
                description = 'Ожирение 1-й степени'
            elif 25 <= imt < 30:
                description = 'Избыточная масса тела (состояние, предшествующее ожирению)'
            elif 18.25 <= imt < 25:
                description = 'Норма'
            elif 16 <= imt < 18.25:
                description = 'Недостаточная масса тела (дефицит)'
            else:
                description = 'Выраженный дефицит массы тела'
            context = {'name': name, 'age': age, 'height': height,
                       'weight': weight, 'imt': round(imt, 2), 'description': description}

            return render(request, 'profile.html', context)
    else:
        form = SimpleTextForm()
    return render(request, 'profile.html', context={'form': form})

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