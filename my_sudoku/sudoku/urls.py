from django.conf.urls import patterns, url
from sudoku import views

urlpatterns = patterns('',
                        url(r'^test/$', views.start_sudoku, name='test'),
)