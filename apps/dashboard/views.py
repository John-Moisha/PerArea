from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView, View, DetailView, FormView)
from apps.accounts.models import CustomUser
from apps.accounts.forms import SettingsForm
from core import settings
from .forms import CheckForm, VerificationForms, VerifAccountForms,VerificationFormsSet
from .models import Check, Transaction, Verification


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DashboardView(LoginRequiredMixin, TemplateView):
    # model = CustomUser
    template_name = 'dashboard/home.html'


class CheckView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/check.html'


class DepositsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/deposits.html'


class Replenish(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/replenish.html'


class TransactionsView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/transactions.html'
    model = Transaction

    def get_object(self):
        # context = get_object_or_404(Transaction, user_id=self.request.user.id)
        # context['doc'] = self.
        return get_object_or_404(Transaction, user_id=self.request.user.id)


class SettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/settings.html'
    form_class = SettingsForm
    success_url = reverse_lazy('dashboard:settings')

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.request.user.id)


# class VerifAccountFormView(FormView):
#     template_name = 'dashboard/verification.html'
#     form_class = VerifAccountForms
#     success_url = reverse_lazy('dashboard:verification')
#
#     def post(self, request, *args, **kwargs):
#         VerifAccount_form = self.form_class(request.POST)
#         Verification_form = VerificationForms()
#         if VerifAccount_form.is_valid():
#             VerifAccount_form.save()
#             return self.render_to_response(
#                 self.get_context_data(
#                     success=True,
#                 )
#             )
#         else:
#             return self.render_to_response(
#                 self.get_context_data(
#                     VerifAccount_form=VerifAccount_form,
#                 )
#             )


# class VerificationFormView(FormView):
#     template_name = 'dashboard/verification.html'
#     form_class = VerificationForms
#     success_url = reverse_lazy('dashboard:verification')
#
#     def post(self, request, *args, **kwargs):
#         Verification_form = self.form_class(request.POST)
#         VerifAccount_form = VerifAccountForms()
#         if Verification_form.is_valid():
#             Verification_form.save()
#             return self.render_to_response(
#                 self.get_context_data(
#                     success=True,
#                 )
#             )
#         else:
#             return self.render_to_response(
#                 self.get_context_data(
#                     Verification_form=Verification_form,
#                     VerifAccount_form=VerifAccount_form
#                 )
#             )


# class VerificationView(LoginRequiredMixin, UpdateView):
#     template_name = 'dashboard/verification.html'
#     # form_class = VerificationForms
#     success_url = reverse_lazy('dashboard:verification')
#
#     # def get_object(self, queryset=None):
#     #     return get_object_or_404(Verification, user_id=self.request.user.id)
#
#     def get(self, request, *args, **kwargs):
#         VerifAccount_form = VerifAccountForms(self.request.GET or None)
#         Verification_form = VerificationForms(self.request.GET or None)
#
#         context = self.get_context_data(user_id=self.request.user.id, **kwargs)
#         # get_object_or_404(Verification, user_id=self.request.user.id)
#
#         context['VA_f'] = VerifAccount_form
#         context['V_f'] = Verification_form
#         return self.render_to_response(context)


#
class VerificationView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/verification.html'
    form_class = VerificationForms
    success_url = reverse_lazy('dashboard:verification')

    def get_object(self, queryset=None):
        return get_object_or_404(Verification, user_id=self.request.user.id)


class VerificationInLine():
    model = Verification
    template_name = 'dashboard/verification.html'
    form_class = VerificationForms
    success_url = reverse_lazy('dashboard:verification')

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return reverse_lazy('dashboard:verification')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.product = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving. Useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.product = self.object
            image.save()


# class VerificationView2(LoginRequiredMixin, UpdateView):
#     model = CustomUser
#     template_name = 'dashboard/verification.html'
#     form_class = VerificationForms
#     success_url = reverse_lazy('dashboard:verification')
#
class VerificationView2(VerificationInLine, UpdateView):

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Verification, user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        ctx = super(VerificationView2, self).get_context_data(**kwargs)
        ctx['VerificationFormsSet'] = self.get_named_formsets()
        return get_object_or_404(ctx, user_id=self.request.user.id)

    def get_named_formsets(self):
        return {
            # 'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            # 'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
            'verif': VerificationFormsSet(self.request.POST or None,
                                          instance=get_object_or_404(Verification, user_id=self.request.user.id),
                                          prefix='verif')
            # 'v2erif': VerificationFormsSet(self.request.POST or None,
            #                               instance=get_object_or_404(CustomUser, pk=self.request.user.id),
            #                               prefix='verif')
            # get_object_or_404(Verification, user_id=self.request.user.id)
        }







