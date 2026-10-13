from django.urls import path
from . import views

urlpatterns = [
    # سنضيف هنا مسارات الصفحات مع شرح الـ Views
    path('', views.index, name='index'),
    path('index2/<int:val1>/', views.index2, name='index2'),
    path('viewbook/<int:bookId>/', views.viewbook, name='viewbook'),
    path('<int:bookId>', views.viewbook),

]