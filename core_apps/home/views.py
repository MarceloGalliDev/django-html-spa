from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CorretoraForm


class CadastroCorretoraView(FormView):
    template_name = 'home/page_home.html'
    form_class = CorretoraForm
    success_url = reverse_lazy('cadastro_sucesso')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
