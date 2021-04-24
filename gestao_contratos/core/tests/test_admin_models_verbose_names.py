from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.test import TestCase


class AdminModelsTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username="tester")
        self.user.set_password("qwer1234")
        self.user.save()
        self.client.login(username='tester', password='qwer1234')

    def test_models_verbose_name(self):
        response = self.client.get(resolve_url('admin:index'))
        expected = ['Atletas</a>', ]
        for text in expected:
            with self.subTest():
                self.assertContains(response, text)
