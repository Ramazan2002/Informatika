from django.test import TestCase
from django.utils.timezone import now
from posts.forms import CreateFullPostForm, CreateCommentForm

class CreateFullPostFormTest(TestCase):

    def test_labels(self):
        form = CreateFullPostForm()
        self.assertTrue(form.fields['title'].label == 'Title')
        self.assertTrue(form.fields['body'].label == 'Body')
        self.assertTrue(form.fields['images'].label == 'Images')
        self.assertTrue(form.fields['tags'].label == 'Tags')

    def test_date(self):
        date = now()
        data = {'date_publication': date, 'title': '123', 'body': '123456'}
        form = CreateFullPostForm(data=data)
        self.assertTrue(form.is_valid())

class CreateCommentFormTest(TestCase):

    def test_labels(self):
        form = CreateCommentForm()
        self.assertTrue(form.fields['text'].label == 'Comment')