from django.shortcuts import render_to_response

# Create your views here.
def lab_view(request):
    r"""SUMMARY

    lab_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response('lab/index.html', context)
