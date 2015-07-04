from django.conf.urls import patterns, url
from sudoku import views

urlpatterns = patterns('',
                        url(r'^$', views.start_sudoku, name='test'),
                        url(r'^ajax/add_game_log/$', views.add_game_log),
                        url(r'^history/$', views.show_history, name='history'),
                        url(r'^history/ajax/get_history/$', views.get_history),
                        url(r'^ajax/get_new_game/$', views.get_new_sudoku),
)