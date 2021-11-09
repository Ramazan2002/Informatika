from django.test import TestCase
from posts.models import Post, Comment, Tag
from users.models import CustomUser, UserProfile, Group

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')
        CustomUser.objects.create(login='123456', password='123456', group_id=1)
        UserProfile.objects.create(user_id=1, name='123456')
        Post.objects.create(author_id=1, title='test title', body='body for test')

    def test_labels(self):
        post = Post.objects.get(id=1)
        fields = post._meta.get_fields()
        author_field_label = fields[4].verbose_name
        title_field_label = fields[5].verbose_name
        body_field_label = fields[6].verbose_name
        publication_date_field_label = fields[7].verbose_name
        self.assertEquals(author_field_label, 'author')
        self.assertEquals(title_field_label, 'title')
        self.assertEquals(body_field_label, 'body')
        self.assertEquals(publication_date_field_label, 'publication date')

    def test_max_length(self):
        post = Post.objects.get(id=1)
        fields = post._meta.get_fields()
        title_max = fields[5].max_length
        body_max = fields[6].max_length
        self.assertEquals(title_max, 100)
        self.assertEquals(body_max, 2500)

class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')
        CustomUser.objects.create(login='123456', password='123456', group_id=1)
        UserProfile.objects.create(user_id=1, name='123456')
        Post.objects.create(author_id=1, title='test title', body='body for test')
        Comment.objects.create(post_id=1, author_id=1, text='1234')

    def test_labels(self):
        comment = Comment.objects.get(id=1)
        fields = comment._meta.get_fields()
        self.assertEquals(fields[1].verbose_name, 'post')
        self.assertEquals(fields[2].verbose_name, 'author')
        self.assertEquals(fields[3].verbose_name, 'text')
        self.assertEquals(fields[4].verbose_name, 'publication date')

    def test_max_length(self):
        comment = Comment.objects.get(id=1)
        fields = comment._meta.get_fields()
        text_max = fields[3].max_length
        self.assertEquals(text_max, 100)

class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(text = '123456789')

    def test_labels(self):
        tag = Tag.objects.get(id=1)
        field_name = tag._meta.get_field('text').verbose_name
        self.assertEquals(field_name, 'text')

    def test_max_length(self):
        tag = Tag.objects.get(id=1)
        field_max = tag._meta.get_field('text').max_length
        self.assertEquals(field_max, 10)