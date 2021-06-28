from django.shortcuts import render, redirect
from .forms import FileForm


def home(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = FileForm(request.POST, request.FILES)
            return render(request, 'myapp/home.html', {'form': form})
    form = FileForm()
    return render(request, 'myapp/home.html', {'form': form})
