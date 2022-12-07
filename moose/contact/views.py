from django.shortcuts import render
from .forms import ContactForm
from .models import Subscribe


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'form': form,
        'email': email,
    }

    return render(request, 'contact.html', context)
