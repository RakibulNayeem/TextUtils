# I have created this file - Nayeem
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Us")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*~'''

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        djtext = analyzed
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        djtext = analyzed
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        djtext = analyzed
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please check at least one switch and try again!")

    return render(request, 'analyze.html', params)
