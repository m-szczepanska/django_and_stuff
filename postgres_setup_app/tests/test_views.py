from django.test import TestCase, Client

from tests.fixtures import gen_author, gen_book


client = Client()
BASE_URL='//127.0.0.1:8000'


class TestViews(TestCase):
    def setUp(self):
        self.authors = [
            gen_author(name='Filip Springer'),
            gen_author(name='Jiro Taniguchi'),
        ]
        self.books = [
            gen_book(title='Wanna z kolumnadą', author=self.authors[0]),
            gen_book(title='Miedzianka', author=self.authors[0]),
            gen_book(title='Idący człowiek', author=self.authors[1]),
        ]

    def test_book_list(self):
        response = client.get(f'{BASE_URL}')
        for book in self.books:
            self.assertIn(book, response.context['object_list'])
        self.assertEqual(response.status_code, 200)


    def test_book_detail(self, pk=1):
        response = client.get(f'{BASE_URL}/book_detail/{pk}')
        response_author = response.context['object'].author
        expected_author = self.books[0].author

        self.assertEqual(expected_author, response_author)
        self.assertEqual(self.books[0].title, response.context['object'].title)
        self.assertEqual(response.status_code, 200)