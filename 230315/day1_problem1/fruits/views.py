from django.shortcuts import render

# Create your views here.
def fruit(request):
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]

    context = {
        'data' : fruit_list
    }

    return render(request, 'fruits/fruits.html', context)
