from django.test import TestCase
from posts.models import Post, Tag
from users.models import CustomUser, UserProfile, Group
from django.urls import reverse

class PostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')
        CustomUser.objects.create(login='123456', password='123456', group_id=1)
        UserProfile.objects.create(user_id=1, name='123456')
        Post.objects.create(author_id=1, title='test', body='body')
        Tag.objects.create(text='tag_text')

    def test_url_exists_at_desired_location_if_notlogin(self):
        resp = self.client.get('/posts/create', follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_url_accessible_by_name_if_notlogin(self):
        create_post = self.client.get(reverse('create_post'), follow=True)
        pos_page = self.client.get(reverse('post', kwargs={'pk': 1}))
        update_post = self.client.get(reverse('update_post', kwargs={'pk': 1}))
        delete_post = self.client.get(reverse('delete_post', kwargs={'pk': 1}))
        tag_page = self.client.get(reverse('tag', kwargs={'pk': 1}))
        self.assertEqual(create_post.status_code, 200)
        self.assertEqual(pos_page.status_code, 200)
        self.assertEqual(update_post.status_code, 302)
        self.assertEqual(delete_post.status_code, 302)
        self.assertEqual(tag_page.status_code, 200)

    def test_correct_template_if_notlogin(self):
        create_post = self.client.get(reverse('create_post'), follow=True)
        post_page = self.client.get(reverse('post', kwargs={'pk': 1}))
        update_post = self.client.get(reverse('update_post', kwargs={'pk': 1}))
        delete_post = self.client.get(reverse('delete_post', kwargs={'pk': 1}))
        tag_page = self.client.get(reverse('tag', kwargs={'pk': 1}))
        self.assertTemplateUsed(create_post, 'users/login.html')
        self.assertTemplateUsed(post_page, 'posts/post.html')
        self.assertTemplateNotUsed(update_post)
        self.assertTemplateNotUsed(delete_post)
        self.assertTemplateUsed(tag_page, 'posts/tag.html')
