from django.shortcuts import resolve_url
from django.test import TestCase


class HomeViewGet(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(resolve_url("core:home"))

    def test_view_home_status(self):
        self.assertTrue(200, self.response.status_code)

    def test_view_home_template_used(self):
        self.assertTemplateUsed(self.response, "core/home.html")
