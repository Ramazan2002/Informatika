from django.shortcuts import render, redirect
from .forms import SimpleTextForm
from .models import Record
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
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            size = form.cleaned_data['size']
            imt = round(weight/(height/100)**2, 2)


            if gender == 'm':
                obr = 'Mr'
            elif gender == 'f':
                obr = 'Ms'
            else:
                obr = 'Not a human'
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

            all_imt = Record.objects.values_list('imt', flat=True)
            coefficient = round((imt / (sum(all_imt)/len(all_imt)) - 1), 2) * 100
            coef_positive = coefficient >= 0
            coefficient = abs(coefficient)
            context = {'name': name, 'age': age, 'height': height, 'weight': weight, 'coef_p': coef_positive,
                       'imt': imt, 'description': description, 'size': size, 'coef': coefficient}

            new_record = Record(name=name, age=age, weight=weight, height=height,
                                gender=gender, size=size, obraschenie=obr, imt=imt)
            new_record.save()
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