from django.contrib import admin
from .models import Check, Verification, Transaction
    # Verification, Check, Transaction
from apps.accounts.models import CustomUser
# admin.site.register(Verification)
# admin.site.register(Check)
# admin.site.register(Transaction)
# admin.register( Transaction, Verification)(admin.ModelAdmin)


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = [
#         'user',
#         'email',
#         'unique_id',
#                     ]


class CheckAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'balance',
        'debt',
                    ]


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'doc',
                    ]


class VerificationAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_of_birth',
        'sex',
        'passport1',
        'passport2',
                    ]


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Check, CheckAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Verification, VerificationAdmin)


class CheckInLine(admin.StackedInline):
    model = Check


class TransactionInLine(admin.StackedInline):
    model = Transaction


class VerificationInLine(admin.StackedInline):
    model = Verification


class CustomAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'unique_id',
    )


@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    inlines = [CheckInLine, TransactionInLine, VerificationInLine]





# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#                     'balance',
#                     'debt',
#                     ]
# admin.site.register(Check, ProfileAdmin)




# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         'last_name',
#         'firs_name',
#     ]
# admin.site.register(CustomUser,ProfileAdmin)


#
# from django.contrib import admin
#
# class ProfileInline(admin.StackedInline):
#     model = Check
#
# class ProfileAdmin(admin.ModelAdmin):
#     inlines = [
#         ProfileInline,
#     ]
#
# admin.site.register(CustomUser, ProfileAdmin)

