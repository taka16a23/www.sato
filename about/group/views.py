from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def groupview(request):
    r"""SUMMARY

    group(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'about/group/index.html', context, context_instance=RequestContext(request))
