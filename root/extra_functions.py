from academic.models import Course, Assignment
from submission.models import SessionToken


def check_submission_validity(course_code, assignment_code, session_token):
    the_course = Course.objects.filter(course_code = course_code)
    the_assignment = Assignment.objects.filter(assignment_code = assignment_code)
    the_token = SessionToken.objects.filter(sessionToken_token = session_token)

    # check if the course exists
    if not the_course:
        return 'Course not found with the code, ' + course_code
    
    #check if the assignment exists
    if not the_assignment:
        return 'Assignment not found with the code, ' + assignment_code

    #check if the token exists and have validity
    if not the_token:
        return 'The token is not valid'
    else:
        token_expired = print(the_token.values()[0]['sessionToken_expired'])
        if token_expired:
            return 'The session token is already expired'

    return True