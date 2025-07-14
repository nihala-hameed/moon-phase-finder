from django.shortcuts import render
from .forms import DateInputForm
import requests

def home(request):
    result = None
    form = DateInputForm()

    if request.method == 'POST':
        form = DateInputForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            year = date.year
            month = date.month
            day = date.day

            # Call the Moon API
            url = f"https://www.icalendar37.net/lunar/api/?lang=en&year={year}&month={month}&size=100&lightColor=white&shadeColor=black&texturize=true"
            response = requests.get(url)
            data = response.json()

            # Get the moon phase on that day
            result = data['phase'][str(day)]['svg']  # this returns image URL or SVG

    return render(request, 'home.html', {'form': form, 'result': result})