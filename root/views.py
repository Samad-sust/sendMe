from django.shortcuts import render
from django.http import HttpResponse

from submission.forms import SubmissionForm
from .extra_functions import check_submission_validity
# Create your views here.

def home(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        submission_form = SubmissionForm(request.POST, request.FILES)
        # check whether it's valid:
        print('Submission Received')
        # print(submission_form)
        if submission_form.is_valid():
            course_code = submission_form.cleaned_data['course_code']
            assignment_code = submission_form.cleaned_data['assignment_code']
            reg_no = submission_form.cleaned_data['reg_no']
            session_token = submission_form.cleaned_data['session_token']
            sub_file = submission_form.cleaned_data['assignment_file']
            request_ip = request.META.get('REMOTE_ADDR') #get the IP address of the users PC
            user_agent = request.headers['User-Agent'] # get the details about users' browser

            submission_valid = check_submission_validity(course_code, assignment_code, session_token)
            if submission_valid:
                print('submission is valid')

            return HttpResponse('thanks')
        else:
            # return HttpResponse('Form is not valid')
            pass
    else:
        submission_form = SubmissionForm()
        contexts = {
            'submission_form' : submission_form
        }

        return render(request, 'home.html', contexts)

