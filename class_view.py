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

####################### url.py ##########################
# 說明：as_view()方法會依class的屬性產生資料，並導到預設的template.html

path('publishers/', sign_views.PP.as_view()),  

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
