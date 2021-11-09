from django.test import TestCase
from users.models import CustomUser, UserProfile, Group

class CustomUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')
        CustomUser.objects.create(login='123456', password='123456', group_id=1)

    def test_labels(self):
        user = CustomUser.objects.get(id=1)
        fields = user._meta.get_fields()
        self.assertEquals(fields[2].verbose_name, 'login')
        self.assertEquals(fields[3].verbose_name, 'group')
        self.assertEquals(fields[4].verbose_name, 'password')

    def test_max_length(self):
        user = CustomUser.objects.get(id=1)
        fields = user._meta.get_fields()
        login_max = fields[2].max_length
        password_max = fields[4].max_length
        self.assertEquals(login_max, 20)
        self.assertEquals(password_max, 100)

class UserProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')
        CustomUser.objects.create(login='123456', password='123456', group_id=1)
        UserProfile.objects.create(user_id=1, name='Test')

    def test_labels(self):
        profile = UserProfile.objects.get(user_id=1)
        fields = profile._meta.get_fields()
        self.assertEquals(fields[3].verbose_name, 'name')
        self.assertEquals(fields[4].verbose_name, 'email')

    def test_max_length(self):
        profile = UserProfile.objects.get(user_id=1)
        fields = profile._meta.get_fields()
        name_max = fields[3].max_length
        email_max = fields[4].max_length
        self.assertEquals(name_max, 30)
        self.assertEquals(email_max, 35)

class GroupModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='user', description='standard user')

    def test_labels(self):
        group = Group.objects.get(id=1)
        fields = group._meta.get_fields()
        self.assertEquals(fields[2].verbose_name, 'name')
        self.assertEquals(fields[3].verbose_name, 'description')

    def test_max_length(self):
        group = Group.objects.get(id=1)
        fields = group._meta.get_fields()
        name_max = fields[2].max_length
        description_max = fields[3].max_length
        self.assertEquals(name_max, 20)
        self.assertEquals(description_max, 50)
