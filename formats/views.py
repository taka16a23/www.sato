from django.shortcuts import render
from django.shortcuts import render_to_response
from formats.models import SatoFormat, OtherFormat
from django.template import RequestContext


# Create your views here.
def formats(request):
    r"""SUMMARY

    formats(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    context['satoformats'] = SatoFormat.objects.filter(
        publish=True).order_by('sortid')
    context['otherformats'] = OtherFormat.objects.filter(
        publish=True).order_by('sortid')
    return render_to_response(
        'formats/index.html', context, context_instance=RequestContext(request))
