from django.shortcuts import resolve_url
from django.test import TestCase


class HomeViewGet(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(resolve_url('core:home'))

    def test_status(self):
        self.assertTrue(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/home.html')

    def test_link_login(self):
        self.assertContains(self.response, f'href="{resolve_url("core:login")}"')


class HomeViewPost(TestCase):
    pass
