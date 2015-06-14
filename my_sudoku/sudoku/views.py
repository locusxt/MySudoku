# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from sudoku.models import GameLog
import datetime

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

def show_history(request):
	return render_to_response('history.html')

def get_history(request):
	logs = GameLog.objects.order_by("-date")
	log_list = []
	num = 10
	if len(logs) < 10:
		num = len(logs)
	for i in range(num):
		d = {}
		d['id'] = logs[i].id
		d['question'] = logs[i].question
		d['player'] = logs[i].player
		d['time'] = logs[i].cost_time
		d['level'] = logs[i].level
		d['date'] = logs[i].date.strftime("%Y-%m-%d")
		log_list.append(d)
	response_data = {'logs' : log_list}
	return HttpResponse(json.dumps(response_data), content_type="application/json")




























