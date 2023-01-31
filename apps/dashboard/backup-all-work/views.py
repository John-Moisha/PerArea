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
from .forms import CheckForm, VerificationForms, VerifAccountForms, CollectionTitleFormSet
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


class VerificationView2(LoginRequiredMixin, UpdateView):
    model = Verification
    template_name = 'dashboard/verification.html'
    # form_class = VerificationForm
    success_url = reverse_lazy('dashboard:verification')

    # def get_object(self, queryset=None):
    #     return get_object_or_404(CustomUser, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        data = super(VerificationView2, self).get_context_data(**kwargs)
        get_object_or_404(CustomUser, pk=self.request.user.id)
        if self.request.POST:
            data['first_name'] = CollectionTitleFormSet(self.request.POST)
            data['last_name'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['first_name'] = CollectionTitleFormSet()
            data['last_name'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(VerificationView2, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:collection_detail', kwargs={'pk': self.object.pk})


