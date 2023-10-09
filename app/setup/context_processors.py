from setup.models import Setup


def setup(request):
    setup_object = Setup.objects.order_by('-id').first()
    return {
        'setup': setup_object,
    }
