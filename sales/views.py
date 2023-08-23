from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')


# render understands to search for templates within the cwd 
# and the two levels under to the template html. 
def formatted_results(request):
    return render(request, 'sales/format_sales.html')