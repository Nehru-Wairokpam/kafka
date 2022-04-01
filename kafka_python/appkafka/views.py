# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
import pickle #pickle converts data into byte array
# def kafka_funtion(request):
  
#   producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
#   producer.send('djangoTopic', b'test')
#   return HttpResponse(200)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def kafka_funtion(request):
    if request.method == 'POST':
        data= request.body
        print(data)
        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
       
        producer.send('djangoTopic', data)
        return HttpResponse("Successfuly Published")
    else:
        return HttpResponse("GET Method Not Allow")