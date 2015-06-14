# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from sudoku.models import GameLog

# Create your views here.
def start_sudoku(request):
	return render_to_response('sudoku.html')

@csrf_exempt
def add_game_log(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	game_log = GameLog(
		question=d['question'],
	 	level=d['level'], 
	 	player=d['player'], 
	 	cost_time=d['time']
	 );
	game_log.save();
	return HttpResponse("OK")