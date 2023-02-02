import django_filters
from .models import Submission, SessionToken


# class OrderFilter(django_filters.FilterSet):

#     user_id__id = django_filters.CharFilter(lookup_expr='iexact')
#     book_id__id = django_filters.CharFilter(lookup_expr='iexact')
#     user_id__email = django_filters.CharFilter(lookup_expr='iexact')
#     start_date = DateFilter(field_name='order_date', lookup_expr='gte')
#     end_date = DateFilter(field_name='order_date', lookup_expr='lte')

#     class Meta:
#         model = Order
#         fields = '__all__'
#         exclude = ['order_date', 'book_id', 'user_id']


class SubmissionFilter(django_filters.FilterSet):
    submission_reg_no = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Submission
        fields = ['submission_assignment', 'submission_course', 'submission_session_token', 'submission_date_time', 'submission_reg_no']



class TokenFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SessionToken
        fields = '__all__'