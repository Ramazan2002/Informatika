from django import forms
from .models import Post, Comment
from django.utils.translation import ugettext_lazy as _

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class CreateFullPostForm(CreatePostForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta(CreatePostForm.Meta):
        fields = CreatePostForm.Meta.fields + ['images',]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': _('Comment')}
