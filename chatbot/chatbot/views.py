from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    context = {}

    return render(request, "chathome.html", context)

def keyboard(request):
    return JsonResponse({
        'type': 'text',

    })

def message(request):

    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == "테스트"
        return JsonResponse({
            "version": "v2",
            "userId": "Usss47b00b58c90f8e47428af8b7bddcda3d",
            "timestamp": 1664169457884,
            "bubbles": [
                {
                    "type": "text",
                    "data": {
                                "description": "Chatbot Answer",
                                "url": "https://ncloud.com", # optional: URL
            "urlAlias": "https://ncloud.com" #optional: URL
            },
            "information": [
                {
                    "key": "chatType",
                    "value": "TEXT"
                },
                {
                    "key": "chatType",
                    "value": "TEXT"
                },
                {
                    "key": "score",
                    "value": "1.0"
                },
                {
                    "key": "scenarioName",
                    "value": "Conversation Name"
                },
                {
                    "key": "endOfBubble",
                    "value": "endOfBubble"
                },
                {
                    "key": "matchingType",
                    "value": "exactMatch"
                },
                {
                    "key": "domainCode",
                    "value": "Domain Code"
                }
            ],
            "context": []
            }
            ],
            "scenario": {
                            "name": "Conversation Name",
                            "chatUtteranceSetId": 4929383, # Conversation ID
            "intent": []
            },
            "entities": [],
            "keywords": [],
            "conversation": {
                                "scenarioName": "Conversation Name",
                                "chatUtteranceSetId": 4929383, # Conversation ID
            "types": []
            },
            "normalizer": "null",
            "event": "send"
        })


