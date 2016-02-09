from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def about_view(request):
    r"""SUMMARY

    about_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'about/index.html', context, context_instance=RequestContext(request))
