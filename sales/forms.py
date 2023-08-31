from django import forms
from .models import Sale

# specify the 3 chart choices with a 
# human readable choice string and a corresponding number.
CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart')
)

qs = Sale.objects.all()
titles = [e.book.title for e in qs]
title_choices = ()
titles = set(titles)
for e in titles:
    title_choices = ((e,e),) + title_choices



class SalesSearchForm(forms.Form):
    book_title = forms.ChoiceField(choices=title_choices)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
