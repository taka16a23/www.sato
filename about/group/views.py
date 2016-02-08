from django.shortcuts import render

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
    return render(request, 'about/group/index.html', context)
