from django.test import TestCase
from main.models import Feedback
from datetime import datetime

class FeedbackModelTest(TestCase):
    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            name="Тестовый пользователь",
            email="test@example.com",
            message="Это тестовый отзыв",
            rating=4,
            created_at=datetime.now()
        )
        self.assertEqual(feedback.name, "Тестовый пользователь")
        self.assertEqual(feedback.rating, 4)
        self.assertTrue(str(feedback).startswith("Тестовый пользователь"))
