from academic.models import Course, Assignment
from submission.models import SessionToken


def check_submission_validity(course_code, assignment_code, session_token):
    the_course = Course.objects.filter(course_code = course_code)
    the_assignment = Assignment.objects.filter(assignment_code = assignment_code)
    the_token = SessionToken.objects.filter(sessionToken_token = session_token)

    print(the_course, the_assignment, the_token)
    return True