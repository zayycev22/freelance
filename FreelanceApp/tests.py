# import unittest
from django.test import TestCase
from FreelanceApp.forms import User


class FreelanceTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='root',
            email='test@mail.ru',
            password='toor',
        )
        user.save()
        user = User.objects.create_user(
            username='root1',
            email='test1@mail.ru',
            password='toor',
        )
        user.save()

    def test_num_users(self):
        """Проверяем общее кол-во пользователей в БД"""
        user = User.objects.all()
        self.assertEqual(user.count(), 2)


class UrlsTests(TestCase):
    def test_index(self):
        """Проверка доступности страницы по корневому урлу и правильности шаблона"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_page(self):
        """Проверка доступности страницы регистрации и правильности шаблона"""
        response = self.client.get('/registration')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_page2(self):
        """Проверка доступности страницы топ листа и правильности шаблона"""
        response = self.client.get('/top')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'top_list.html')

    def test_page3(self):
        """Проверка доступности страницы информации о пользователе и правильности шаблона"""
        response = self.client.get('/user/info')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_info.html')

    def test_bad_url(self):
        """Проверка отсутствия страницы"""
        response = self.client.get('/0897864asdSSA1312')
        self.assertEqual(response.status_code, 404)


class UserTests(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='root',
            email='test@mail.ru',
            password='toor',
        )
        user.save()

    def test_user_login(self):
        self.client.login(username='root', password='toor')
        self.assertIn('_auth_user_id', self.client.session)

    def test_user_logout(self):
        self.client.login(username='root', password='toor')
        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)
