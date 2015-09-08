from cloudCheck import models as m

def run(verbose=True):

    m.Image.objects.all().update(lock=False)
