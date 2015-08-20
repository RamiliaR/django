from django.forms import ModelForm
from congratulation.models import Customer, Details

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'mobile']
    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        fields = ['text', 'location', 'date', 'comment']
    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)