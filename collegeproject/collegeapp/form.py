from django import forms
from .models import Department, Order,Course

class OrderForm(forms.ModelForm):
    # Form fields for name, DOB, age, gender, phone number, email, address, department, courses, purpose, and materials
    class Meta:
        model=Order
        fields=['name','dob','age','gender','email','phone_number','purpose','department','course','pen','notebook']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset=Course.objects.none()

        if'department'in self.data:
            try:
                department_id=int(self.data.get('department'))
                self.fields['course'].queryset=Course.objects.filter(department_id=department_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset=self.instance.department.course_set.order_by('name')