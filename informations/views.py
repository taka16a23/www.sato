from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def informations_view(request):
    r"""SUMMARY

    informations_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'informations/index.html', context, context_instance=RequestContext(request))
