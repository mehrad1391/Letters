import random
from django.shortcuts import render
from django.http import JsonResponse

LETTERS = list("اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی")

def get_letters(request):
    count = random.randint(5,9)
    letters = random.sample(LETTERS, count)
    
    return JsonResponse ({
        "letters": letters
    })