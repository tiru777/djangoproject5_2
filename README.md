```commandline
CRUD
------------------
Function based views
    - Create
    - update
    - delete
    - retrive or get

Authentication
------------------
views.py
    class EmployeeSignup(generic.CreateView):
        form_class = UserCreationForm
        template_name = "signup.html"
        success_url = reverse_lazy('home')
urls.py
    - create one signup page for this view
template
    - signup.html page create with form
    - registration directory create
        - login.html page create with defult form
urls.py
    - from django.urls import path,include
    - path('accounts/',include('django.contrib.auth.urls'),name='login')
settings.py
    - LOGIN_REDIRECT_URL = "home"
    - LOGOUT_REDIRECT_URL = "home"

Templates
    - base.html or whatever templates
        - make one condition if user is authenticated or not
            -   {% if user.is_authenticated %}
                    <h1>Welcome you have successfully logged</h1>
                  {% else %}
                    <h1>Please login or Signup</h1>
                  {% endif %}

```