from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render_to_response
from about.contact.forms import ContactForm
from django.template import RequestContext

def contactform(request):
    context = {}
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/about/contact/thankyou/')
    context['form'] = ContactForm()
    return render_to_response(
        'about/contact/index.html',
        context,
        context_instance=RequestContext(request))

def thankyou(request):
    r"""SUMMARY

    thankyou(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    return render_to_response('about/contact/thankyou.html', )
