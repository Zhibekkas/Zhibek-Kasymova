from django.shortcuts import render
# Create your views here.


def calculate(request):

    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        result = 0
        num1 = int(request.POST.get('num'))
        num2 = int(request.POST.get('num1'))
        action = request.POST.get('options')
        if action == '+':
            result = num1 + num2
        elif action == '-':
            result = num1 - num2
        elif action == '*':
            result = num1 * num2
        elif action == '/':
            result = num1/num2
        context = {
            'number1': request.POST.get('num'),
            'number2': request.POST.get('num1'),
            'option': request.POST.get('options'),
            'result': result
        }
        print(context)
        return render(request, 'index.html', context)





