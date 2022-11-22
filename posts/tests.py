from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


CustomUser = get_user_model()

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = CustomUser.objects.create_user(
            username = 'testuser1',
            password = '123abc')
        testuser1.save()

        test_post = Post.objects.create(
            author = testuser1, title='Blog title', body='Body content ...')
        test_post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content ...')
        self.assertNotEqual(body, 'It shoudn\'t be here')
        

