from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Comment

class BlogPostCommentTests(TestCase):

    def setUp(self):
        self.post = BlogPost.objects.create(
            title="Test Post", 
            author="Test Author", 
            content="Test Content"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author="Commenter",
            text="Test Comment"
        )

    def test_create_blog_post(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'author': 'New Author',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(BlogPost.objects.count(), 2) 
        self.assertEqual(BlogPost.objects.last().title, 'New Post')

    def test_edit_blog_post(self):
        response = self.client.post(reverse('edit_post', args=[self.post.id]), {
            'title': 'Updated Title',
            'author': 'Test Author',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated Content')

    def test_delete_blog_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_add_comment(self):
        response = self.client.post(reverse('add_comment', args=[self.post.id]), {
            'author': 'New Commenter',
            'text': 'Another Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.last().text, 'Another Comment')
