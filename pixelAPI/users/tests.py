from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
class Test(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test123',
            email='test@ggg.com',
            first_name='test',
            last_name='test2',
            date_birthday='1992-09-04',
            usernumber='+321122311',
            password='porca123'
        )
        self.assertEqual(user.username, 'test123')
        self.assertEqual(user.email, 'test@ggg.com')
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'test2')
        self.assertEqual(user.date_birthday, '1992-09-04')
        self.assertEqual(user.usernumber, '+321122311')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='Upertest123',
            email='Upertest@ggg.com',
            first_name='Upertest',
            last_name='Upertest2',
            date_birthday='1992-09-04',
            usernumber='+32112231',
            password='porcaTroia'
        )
        self.assertEqual(user.username, 'Upertest123')
        self.assertEqual(user.email, 'Upertest@ggg.com')
        self.assertEqual(user.first_name, 'Upertest')
        self.assertEqual(user.last_name, 'Upertest2')
        self.assertEqual(user.date_birthday, '1992-09-04')
        self.assertEqual(user.usernumber, '+32112231')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_admin)