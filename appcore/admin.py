from django.contrib import admin
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from appcore.models import User, Profile, Post, Comment, Reaction, Survey, SurveyResponse, Notification, Group
from django import forms
from django.urls import path


class MyAdminSite(admin.AdminSite):
    site_header = 'SocialMedia Administration'

    def get_urls(self):
        return [path('stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        # Implementation for the custom stats view can be added here
        pass


admin_site = MyAdminSite(name='SocialMedia')


class ProfileForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['id', 'user__username']
    list_filter = ['user__username']
    form = ProfileForm

    def image_tag(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="150" height="150" />')
        return None

    image_tag.short_description = 'Avatar'


admin_site.register(User)
admin_site.register(Profile, ProfileAdmin)
admin_site.register(Post)
admin_site.register(Comment)
admin_site.register(Reaction)
admin_site.register(Survey)
admin_site.register(SurveyResponse)
admin_site.register(Notification)
admin_site.register(Group)
