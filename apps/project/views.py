from django.shortcuts import render, HttpResponse, redirect, reverse,  get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.views.generic.edit import FormView, UpdateView
from django.conf import settings
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.base import View
# from .forms import AuthForm, RegisterForm, ProfileEditForm, UserEditForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Project
from .forms import ProjectEditForm, ProjectForm
from ..user.views import get_context
from ..user.views import Messages, ajax_messages
from django.template.defaultfilters import slugify



from django.views.generic.edit import FormView
from django.views.generic.list import ListView

class ProjectCreate(FormView):
    template_name = 'project_setup.html'
    form_class = ProjectForm
    success_url = '/'   #change

    def get_form_kwargs(self):
        kwargs = super(ProjectCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'pagename': 'Новый проект',
        })
        return context

    def form_valid(self, form):
        form.save(commit=False)
        return super(ProjectCreate, self).form_valid(form)

    def form_invalid(self, form):
        # Add action to invalid form phase
        print(form)
        print(form.error_messages)
        # messages.success(self.request, 'An error occured while processing the payment')
        # return self.render_to_response(self.get_context_data(form=form))


def project_create(request):
    m = Messages()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(request.user)
        else:
            print(form.errors)
    else:
        form = ProjectForm()

    return render(request, 'project_setup.html', {
        'form': form,
        'pagename': 'Новый проект',
    })


class ProjectListView(ListView):

    model = Project
    template_name = 'project_list.html'
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'pagename': 'Проекты',
        })
        return context


def project_view(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return '404'

    m = Messages()
    if request.method == 'POST':
        if request.user.is_authenticated and request.user == project.author:
            response_data = {}
            project_form = ProjectForm(request.POST, instance=project)
            if project_form.is_valid() and project_form.is_valid():
                project = project_form.save(request.user, commit=False)
                # response_data.update(project_form.cleaned_data)
                # response_data.update(project_form.cleaned_data)
                # m.add(request, 'success', 'Ваш профиль был успешно обновлен!')
                project.save()
                project_form.save_m2m()
                response_data.update({'messages': ajax_messages(request)})
            else:
                # m.add(request, 'error', 'Что-то пошло не так...')
                response_data.update({'messages': ajax_messages(request)})
            # return JsonResponse(response_data)
        else:
            raise Exception
    else:
        project_form = ProjectForm()
        print(project_form)

    return render(request, 'project_view.html', {
        'form': project_form,
        'user_id' : project.id,
        'project' : project,
    })
    #
    # if request.user.is_authenticated and request.user == project.author:
    #     # user is project owner
    #     return redirect(reverse('user_profile'), get_context(request, 'Профиль'))
    # else:
    #     # client tries to look smb profile
    #     except ObjectDoesNotExist:
    #         return HttpResponseNotFound

