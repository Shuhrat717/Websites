from django.shortcuts import render

from apps.contact.forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.POST.get('email')
    context = {
        'form': form,
        'email': email,
    }

    return render(request, 'contact.html', context)
