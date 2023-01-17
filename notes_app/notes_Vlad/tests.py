from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from .models import NoteModel, Category
from .views import SearchNotesView, NotesVlad


class NotesVladTest(TestCase):
    '''Тест для представления NotesVlad.
     Метод test_notes_vlad_view проверяет, что представление возвращает код состояния 200,
     и что ответ содержит текст 'Test Note' и 'Test Category'.'''

    def setUp(self):
        self.category1 = Category.objects.create(title='Category 1')
        self.category2 = Category.objects.create(title='Category 2')
        self.note1 = NoteModel.objects.create(content='Note 1', category=self.category1)
        self.note2 = NoteModel.objects.create(content='Note 2', category=self.category1)
        self.note3 = NoteModel.objects.create(content='Note 3', category=self.category2)

    def test_get_context_data(self):
        response = self.client.get(reverse('NotesVlad'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 3)

        response = self.client.get(reverse('NotesVlad'), {'category': 'Category 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 2)
        self.assertEqual(response.context['notes'][0], self.note2)
        self.assertEqual(response.context['notes'][1], self.note1)

        response = self.client.get(reverse('NotesVlad'), {'category': 'Category 2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 1)
        self.assertEqual(response.context['notes'][0], self.note3)

        response = self.client.get(reverse('NotesVlad'), {'category': 'Все'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 3)


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
