import logging
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .tasks import send_registration_email
from .forms import CorretoraForm

logger = logging.getLogger(__name__)


class CadastroCorretoraView(FormView):
    template_name = 'home/page_home.html'
    form_class = CorretoraForm

    def form_valid(self, form):
        form.save()

        context = {
            'nome_corretora': form.cleaned_data['nome_corretora'],
            'telefone': form.cleaned_data['telefone'],
            'email': form.cleaned_data['email'],
            'cnpj': form.cleaned_data['cnpj'],
            'pessoa_contato': form.cleaned_data['pessoa_contato'],
        }

        send_registration_email.delay(context)

        return JsonResponse({"success": True})

    def form_invalid(self, form):
        errors = {field: error[0] for field, error in form.errors.items()}
        return JsonResponse({"success": False, "errors": errors})

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
