from .models import Book
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_book_title_from_id(id):
    book_ref = Book.objects.get(id=id)
    return book_ref

def get_graph():
    # create a byte stream for image 
    buffer = BytesIO()
    # creates a plot with a bytesio object as a file-like object, Sets the formatting of image to png. 
    plt.savefig(buffer, format = 'png')
    # set cursor to the stream's begin
    buffer.seek(0)
    # get file contents
    image_png = buffer.getvalue()
    #encode our bytestream file 
    graph=base64.b64encode(image_png)
    # decode 
    graph = graph.decode('utf-8')
    # close the stream and free up mem
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    # AntiGrain Geometry
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,3))
    if chart_type == '#1':
        plt.bar(data['date_created'], data['quantity'])
    elif chart_type == "#2":
        # pie chart based upon price
        labels = kwargs.get('labels')
        plt.pie(data['quantity'], labels=labels)
    elif chart_type == "#3":
        # plot line chart based on data on x-axis and price on y-axis
        plt.plot(data['date_created'], data['price'])
    else:
        print('Unknown chart type entered')
    plt.tight_layout()

    chart = get_graph()
    return chart