from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from .models import NoteModel, Category
from .views import SearchNotesView


class NotesVladTestCase(TestCase):
    '''Тест для представления NotesVlad.
     Метод test_notes_vlad_view проверяет, что представление возвращает код состояния 200,
     и что ответ содержит текст 'Test Note' и 'Test Category'.'''

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(title='Test Category')
        self.note = NoteModel.objects.create(content='Test Note', category=self.category)

    def test_notes_vlad_view(self):
        response = self.client.get(reverse('NotesVlad'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'Test Category')


class SearchNotesViewTest(TestCase):
    '''Тест для SearchNotesView.'''

    def setUp(self):
        self.factory = RequestFactory()
        self.note = NoteModel.objects.create(content='test content')

    def test_search_notes_view(self):
        request = self.factory.get('/search-notes/', {'q': 'test'})
        request.user = AnonymousUser()
        view = SearchNotesView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test content')
