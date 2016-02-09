from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def security_view(request):
    r"""SUMMARY

    security_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'security/index.html', context, context_instance=RequestContext(request))
