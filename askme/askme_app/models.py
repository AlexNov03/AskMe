from django.db import models

QUESTIONS = [
    {
        'id' : i, 
        'title' : f'Question {i}', 
        'text' : f'Text {i}'
    }for i in range(20)
]

CORRECT_CARD_QUESTIONS = [
    {'id': i,
     'text' : 'Text for correct card question'} for i in range(10)
]
