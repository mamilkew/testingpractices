from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import User

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
            request = HttpRequest()
            response = home_page(request)
            html = response.content.decode('utf8')
            self.assertTrue(html.startswith('<html>'))
            self.assertIn('<title>To-Do lists</title>', html)
            self.assertTrue(html.endswith('</html>'))


class UserTestCase(TestCase):

    def setUp(self):
        self.author = User.objects.create(
          username='author@test.com',
          email='author@test.com',
          user_type=User.AUTHOR
        )
        self.publisher = User.objects.create(
          username='publisher@test.com',
          email='publisher@test.com',
          user_type=User.AUTHOR
        )

    def test_get_authors(self):
      self.assertEqual(User.get_authors(), 1)

    def test_can_write_books(self):
      self.assertTrue(self.author.can_write_books())
      self.assertFalse(self.publisher.can_write_books())
