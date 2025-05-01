from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Document


class DocumentInline(admin.TabularInline):
    '''
    Inline-документы, показываются на странице пользователя
    '''
    model = Document
    extra = 0
    fields = ('title', 'file', 'description', 'created_at')
    readonly_fields = ('created_at',)


class UserAdmin(BaseUserAdmin):
    '''
    Админка пользователя
    '''
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    filter_horizontal = ()
    inlines = [DocumentInline]

    @admin.display(description='Documents')
    def document_count(self, obj):
        return obj.documents.count()


class DocumentAdmin(admin.ModelAdmin):
    '''
    Админка документа
    '''
    list_display = ('title', 'owner', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'owner__email')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)

