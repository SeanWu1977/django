####################### view.py ##########################

from django.views.generic import ListView, CreateView, DetailView
# Create your views here.

class PP(ListView):
    model = Publisher
    
    context_object_name = 'my_favorite_publishers' # 設定 多回傳一queryset的名字，內容同object_list
    
    queryset = Publisher.objects.all()[0:1] # 標準回傳值，預設是Publisher.objects.all() ，可覆寫此值

    # 如沒有指定，會在templates\<app name>\<model name>_<view type>.html
    # 本例為templates\<app name>\publisher_list.html
    template_name = 'dir\xxx.html' # 會在templates\dir\xxx.html
                   
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


    
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        # 此方法同上一個class用 變數 queryset 來覆寫回傳值 
        # 同時存在時，會以此方法內的回傳值為主，會呼略變數 queryset 
        #
        # self 會儲存傳進來的變數，字典
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        # 此處是直接傳字典，所以直接用 self.publisher
        context['publisher'] = self.publisher
        return context    
    

    
from django.views import View
class GreetingView(View):
    greeting = "Good Day"
    def get(self, request):
        return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
    greeting = "Morning to ya "
    
    # url dispatch代入的變數會在此方法引入
    def get(self, request, name): 
        return HttpResponse(self.greeting + name)
    
class aboutview(TemplateView):
    template_name="view/about.html"    
    
####################### url.py ##########################
# 說明：as_view()方法會依class的屬性產生資料，並導到預設的template.html

path('publishers/', sign_views.PP.as_view()), 

# 傳變數到List
path('books/<publisher>/', PublisherBookList.as_view()),


path('about/', TemplateView.as_view(template_name="view/about.html")),
path('about1/', sign_views.aboutview.as_view()),
re_path('hi/(\w+)/', sign_views.MorningGreetingView.as_view()),

# 補充：as_view()方法-->執行後會return self.dispatch(request, *args, **kwargs)
# dispatch 會依request的方式(get, post, ..), 用getattr()函數 呼叫對應的 function (def get() / def post() ...)

####################### template (位於\templates目錄下) ##########################
####################### 如沒指定，則位於\templates\<app name>\xxx.html ##########################
{% block content %}
    <h2>Publishers</h2>
    <ul>
        {% for publisher in my_favorite_publishers %}
            <li>{{ publisher.name }},{{ publisher.address }}</li>
        {% endfor %}
    </ul>


     <ul>
        {% for book in book_list %}
            <li>{{ book.title }}</li>
        {% endfor %}
    </ul>   
{% endblock %}
