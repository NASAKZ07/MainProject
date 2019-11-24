from django.shortcuts import render

def signIn(request):
    return render(request, 'MyApp/signIn.html')
def signUp(request):
    return render(request, 'MyApp/signUp.html')