from django.test import TestCase

# Create your tests here.
from django.utils import timezone
import datetime
from django.urls import reverse
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """ 
        was_published-recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        """ 
        was_published-recently() returns False for questions whose pub_date is far in the past.
        """
        time = timezone.now()- datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

        time = timezone.now()- datetime.timedelta(days=1,seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)


    def test_was_published_recently_with_recent_question(self):
        """ 
        was_published-recently() returns False for questions whose pub_date is in the recent past.
        """
        time = timezone.now() - datetime.timedelta(days=0.5)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),True)

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),True)

def create_question(question_text,days):
    """
    Create a question with the given 'question_text' and published the 
    given number of 'days' offset to now (negative for questions published
    in the past, positive for questions that have yet to be pulbished)

    """