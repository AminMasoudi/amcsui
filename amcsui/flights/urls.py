from django.urls import path
from . import views
app_name = 'flights'

urlpatterns = [
        path("",views.index,name="flights"),
        path("bookaflight/", views.book, name="bookAflight"),
]
