from django.shortcuts import render, redirect
from django.views import View
from .models import Alumni
from .forms import AlumniForm

class AlumniListView(View):
    def get(self, request):
        alumni = Alumni.objects.all()
        return render(request, 'alumni_list.html', {'alumni': alumni})

def AlumniFilterView(request):
    if request.method == 'POST':
        sphere = request.POST.get('sphere')
        alumni = Alumni.objects.filter(sphere=sphere)
        return render(request, 'alumni_list.html', {'alumni': alumni})
    else:
        return render(request, 'alumni_filter.html')

class AlumniAddView(View):
    def get(self, request):
        form = AlumniForm()
        return render(request, 'alumni_add.html', {'form': form})

    def post(self, request):
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumni_list')
        return render(request, 'alumni_add.html', {'form': form})
