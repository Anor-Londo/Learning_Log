from django.shortcuts import render

def index(reauest):
    """The home page for Learning Log"""
    return render(reauest, 'learning_logs/index.html')
