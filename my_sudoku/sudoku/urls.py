from django.conf.urls import patterns, url
from sudoku import views

urlpatterns = patterns('',
                        url(r'^$', views.start_sudoku, name='test'),
                        url(r'^ajax/add_game_log/$', views.add_game_log),
)