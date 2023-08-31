from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_book_title_from_id, get_chart

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    df = None
    chart = None

    # upon submission ....
    if request.method == 'POST':
        
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        qs = Sale.objects.filter(book__title=book_title)
        # qs = Sale.objects.all()
        if qs:
            df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, df, labels = df['date_created'].values)
            df['book_id'] = df['book_id'].apply(get_book_title_from_id)
            df = df.rename(columns={'book_id':'book_title'})
            df = df.to_html()
        else:
            df = 'search found no matches.'
    
    # context binds form data to template variable. 
    context = {
        'form' : form,
        'df': df,
        'chart' : chart
    }

    return render(request, 'sales/records.html', context)

