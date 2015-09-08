from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

import datetime

from cloudCheck import models as m
from cloudCheck.forms import CloudForm

initial_comment = 'Comments (140 character limit)'

@login_required
def index(request):

    qs = m.Image.objects.exclude(is_cloudy__gte=1, lock=True)
    img = qs[0]
    form = CloudForm(initial= {'cloud_comments': initial_comment })
    
    # Lock image
    m.Image.objects.filter(id=img.id).update(lock=True)

    context = { 'images': img,
                'form' : form,
    }
 
    return render(request, 'cloudCheck/index.html', context)

@login_required
def cloud_submit(request, image_id):

    # Grab data from form
    form = CloudForm(request.POST)

    # Check if all fields are complete
    if form.is_valid():
        
        # Get data from submitted form
        cloudClass = int(form.cleaned_data.get('cloud_classification'))
        comments   = form.cleaned_data.get('cloud_comments')
        check_date = datetime.datetime.now()
        checked_by = request.user.username

        if (comments == initial_comment):
            comments = 'You didn\'t say anything!'
        
        m.Image.objects.filter(id=image_id).update(is_cloudy=cloudClass, 
                                                   cloud_comment=comments,
                                                   checked_by=checked_by,
                                                   checked_date=check_date, 
                                                   lock=False)

        return redirect('index')

    else:
        
        error_message = "No data submitted. Please try again!"

        return HttpResponse(error_message)
