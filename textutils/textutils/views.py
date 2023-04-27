from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
    #return HttpResponse('''<h1>Youtube</h1> <a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django code with Harry</a>''')

#def about(request):
    #with open("test.txt", "r") as f:
        #contents = f.read()
    #return HttpResponse(contents)

def index(request):
    #sending variables in templates using params
    #params = {"name": " Prashant", "place" : "Noida"}
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline','off')
    charcount = request.POST.get('charcount','off')
    extraspace = request.POST.get('extraspace','off')
    # print(removepunc)
    # print(djtext)
    #check if checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text':analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (newline == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'total characters', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (extraspace == 'on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (removepunc != "on" and newline != "on" and extraspace != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

# def removepunc(request):
#     #get the text
#     djtext= request.GET.get('text','default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("Remove Punc")
#
# def capfirst(request):
#     return HttpResponse('''<a href='/'> back </a>''')
#
# def spaceremove(request):
#     return HttpResponse("space remover")
# def newlineremove(request):
#     return HttpResponse("New line remover")
#
# def charcount(request):
#     return HttpResponse("character counter")