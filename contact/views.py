from django.shortcuts import render, HttpResponse


def contact_page(request):
    # return HttpResponse("This is the Bridges Contact Page")
    context = {'title': 'bridges', 'purpose': 'to help students'}
    return render(request, 'contact.html', context)