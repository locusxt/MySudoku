# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def start_sudoku(request):
	return render_to_response('sudoku.html')