
# Create your views here.
"""def contact(request):
    ContactForm
    return render(request, "contact/contact.html")"""


from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # enviamos el correo y  redirecionamos
            email = EmailMessage(
                "Web personal - Nuevo mensaje",
                "DE {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                to=["raulabelleira@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect('/contact/?ok')
            except:
                # algo no fue bien 
                return redirect('/contact/?fail')
        
            

    return render(request, "contact/contact.html", {'form': contact_form})