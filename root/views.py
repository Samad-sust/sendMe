from django.shortcuts import render
from django.http import HttpResponse

from submission.forms import SubmissionForm
from .extra_functions import check_submission_validity
from submission.models import Submission, SessionToken
from academic.models import Course, Assignment
# Create your views here.

def home(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        try:
            submission_form = SubmissionForm(request.POST, request.FILES)
        except:
            return HttpResponse('Something went wrong')
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

            if not sub_file:
                # return HttpResponse('No file uploaded')
               return render(request, 'submission-failure.html', {'msg': submission_valid})
                
            if not submission_valid == True:
            #    return HttpResponse(submission_valid)
               return render(request, 'submission-failure.html', {'msg': submission_valid})

            new_submission = Submission.objects.create(
                submission_assignment = Assignment.objects.get(assignment_code = assignment_code),
                submission_course = Course.objects.get(course_code = course_code),
                submission_session_token = SessionToken.objects.get(sessionToken_token = session_token),
                submission_reg_no = reg_no,
                ip_address = request_ip,
                user_agent = user_agent,
                submission_file = sub_file
            )
            new_submission.save()
            return render(request, 'submission-success.html')

        # return warning messege upon failing the if submission_form.is_valid() valid test       
        else:
            return render(request, 'submission-failure.html', {'msg': 'Submission failed, '})
    else:
        submission_form = SubmissionForm()
        contexts = {
            'submission_form' : submission_form
        }

        return render(request, 'home.html', contexts)

def login(request):
    return render(request, 'login.html')