from django import forms
from .models import Post, Comment, Tag
from django.utils.translation import ugettext_lazy as _

class CreatePostForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Post
        fields = ['title', 'body']

class CreateFullPostForm(CreatePostForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects)

    class Meta(CreatePostForm.Meta):
        fields = CreatePostForm.Meta.fields + ['images', 'tags']

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['images'].widget.attrs['class'] = 'form-control-file'

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': _('Comment')}
