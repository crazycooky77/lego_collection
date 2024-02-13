from django.test import TestCase
from .forms import *


class TestUpdateUsername(TestCase):
    """
    Testing form for updating usernames
    """
    def setUp(self):
        """
        Create test user for test cases
        """
        self.user = CustomUser.objects.create_user(
            username='test_user_exists',
            password='t€$T951',
            email='test_user_exists@test.com',
            privacy='PRV'
        )

    def test_form_is_valid(self):
        """
        Check if overall change username form is valid
        """
        update_user_form = UpdateUsername({'username': 'test'})
        self.assertTrue(update_user_form.is_valid(),
                        msg='Failed: Valid username change form')

    def test_form_invalid(self):
        """
        Check if overall change username form is invalid
        """
        update_user_form = UpdateUsername({'username': ''})
        self.assertFalse(update_user_form.is_valid(),
                         msg='Failed: Invalid username change form')

    def test_user_exists(self):
        """
        See if the username already exists in the database
        """
        update_user_form = UpdateUsername({'username': 'test_user_exists'})
        self.assertFalse(update_user_form.is_valid(),
                         msg='Failed: Username exists check')


class TestUpdatePrivacy(TestCase):
    """
    Testing form for updating privacy settings in account
    """
    def test_form_is_valid(self):
        """
        Check if overall change privacy form is valid
        """
        update_privacy_form = UpdatePrivacy(
            {'privacy': 'PUB'})
        self.assertTrue(update_privacy_form.is_valid(),
                        msg='Failed: Valid privacy change form')

    def test_form_invalid(self):
        """
        Check if overall change privacy form is invalid
        """
        update_privacy_form = UpdatePrivacy({'privacy': ''})
        self.assertFalse(update_privacy_form.is_valid(),
                         msg='Failed: Invalid privacy change form')

    def test_form_invalid_choice(self):
        """
        Check if change privacy choice is invalid
        """
        update_privacy_form = UpdatePrivacy({'privacy': 'Public'})
        self.assertFalse(update_privacy_form.is_valid(),
                         msg='Failed: Invalid privacy change choice')


class TestDeleteAccount(TestCase):
    """
    Testing form for deleting accounts
    """
    def test_form_is_valid(self):
        """
        Check if overall delete account form is valid
        """
        delete_acc_form = DeleteAccount(
            {'delete': 1})
        self.assertTrue(delete_acc_form.is_valid(),
                        msg='Failed: Valid delete account form')

    def test_form_invalid(self):
        """
        Check if overall delete account form is invalid
        """
        delete_acc_form = DeleteAccount(
            {'delete': ''})
        self.assertFalse(delete_acc_form.is_valid(),
                         msg='Failed: Invalid delete account form')

    def test_form_invalid_bool(self):
        """
        Check if delete account boolean is invalid
        """
        delete_acc_form = DeleteAccount(
            {'delete': 0})
        self.assertFalse(delete_acc_form.is_valid(),
                         msg='Failed: Invalid delete account boolean')


class TestCreateCollection(TestCase):
    """
    Testing form for creating collections
    """
    def test_form_is_valid(self):
        """
        Check if overall create collection form is valid
        """
        create_col_form = CreateCollection(
            {'collection_name': 'test_collection'})
        self.assertTrue(create_col_form.is_valid(),
                        msg='Failed: Valid create collection form')

    def test_form_invalid(self):
        """
        Check if overall create collection form is invalid
        """
        create_col_form = CreateCollection(
            {'collection_name': ''})
        self.assertFalse(create_col_form.is_valid(),
                         msg='Failed: Invalid create collection form')


class TestEditCollection(TestCase):
    """
    Testing form for editing collections
    """
    def test_form_is_valid(self):
        """
        Check if overall edit collection form is valid
        """
        edit_col_form = EditCollection(
            {'collection_name': 'test_collection'})
        self.assertTrue(edit_col_form.is_valid(),
                        msg='Failed: Valid edit collection form')

    def test_form_invalid(self):
        """
        Check if overall edit collection form is invalid
        """
        edit_col_form = EditCollection(
            {'collection_name': ''})
        self.assertFalse(edit_col_form.is_valid(),
                         msg='Failed: Invalid edit collection form')


class TestCreateSet(TestCase):
    """
    Testing form for creating sets
    """
    def setUp(self):
        """
        Create test set for test cases
        """
        self.user = LegoSet.objects.create(
            set_number=98765, set_name='Test Set Exists')

    def test_form_is_valid(self):
        """
        Check if overall create set form is valid
        """
        create_set_form = CreateSet(
            {'set_number': 12345, 'set_name': 'Test Set'})
        self.assertTrue(create_set_form.is_valid(),
                        msg='Failed: Valid create set form')

    def test_form_invalid(self):
        """
        Check if overall create set form is invalid
        """
        create_set_form = CreateSet(
            {'set_number': '', 'set_name': ''})
        self.assertFalse(create_set_form.is_valid(),
                         msg='Failed: Invalid create set form')

    def test_form_invalid_nr(self):
        """
        Check if create set (set number) is invalid
        """
        create_set_form = CreateSet(
            {'set_number': '', 'set_name': 'Test Set'})
        self.assertFalse(create_set_form.is_valid(),
                         msg='Failed: Invalid create set (set number) form')

    def test_form_invalid_name(self):
        """
        Check if create set (set name) is invalid
        """
        create_set_form = CreateSet(
            {'set_number': 12345, 'set_name': ''})
        self.assertFalse(create_set_form.is_valid(),
                         msg='Failed: Invalid create set (set name) form')

    def test_set_exists(self):
        """
        See if the set number already exists in the database
        """
        create_set_form = CreateSet({'set_number': 98765,
                                     'set_name': 'Test Set Exists'})
        self.assertFalse(create_set_form.is_valid(),
                         msg='Failed: Set exists check')


class TestAddSet(TestCase):
    """
    Testing form for adding sets to collections
    """
    def setUp(self):
        """
        Create test set for test cases
        """
        LegoSet.objects.create(set_number=12345, set_name='Test Set')

    def test_form_is_valid(self):
        """
        Check if overall add set form is valid
        """
        add_set_form = AddSet({'set': LegoSet.objects.get(set_number=12345),
                               'build_status': 'NEW'})
        self.assertTrue(add_set_form.is_valid(),
                        msg='Failed: Valid add set form')

    def test_form_invalid(self):
        """
        Check if overall add set form is invalid
        """
        add_set_form = AddSet({'set': '',
                               'build_status': ''})
        self.assertFalse(add_set_form.is_valid(),
                         msg='Failed: Invalid add set form')

    def test_form_invalid_set(self):
        """
        Check if add set (set) form is invalid
        """
        add_set_form = AddSet({'set': '',
                               'build_status': 'STORED'})
        self.assertFalse(add_set_form.is_valid(),
                         msg='Failed: Invalid add set (set) form')

    def test_form_invalid_status(self):
        """
        Check if add set (build status) form is invalid
        """
        add_set_form = AddSet({'set': LegoSet.objects.get(set_number=12345),
                               'build_status': ''})
        self.assertFalse(add_set_form.is_valid(),
                         msg='Failed: Invalid add set (build status) form')

    def test_form_invalid_choice(self):
        """
        Check if add set (build status choice) form is invalid
        """
        add_set_form = AddSet({'set': LegoSet.objects.get(set_number=12345),
                               'build_status': 'Built'})
        self.assertFalse(
            add_set_form.is_valid(),
            msg='Failed: Invalid add set (build status choice) form')


class TestUpdateCol(TestCase):
    """
    Testing form for updating sets in collections
    """
    def test_form_is_valid(self):
        """
        Check if overall collection set update form is valid
        """
        update_col_form = UpdateCol({'build_status': 'NEW'})
        self.assertTrue(update_col_form.is_valid(),
                        msg='Failed: Valid update collection sets form')

    def test_form_invalid(self):
        """
        Check if overall collection set update form is invalid
        """
        update_col_form = UpdateCol({'build_status': ''})
        self.assertFalse(update_col_form.is_valid(),
                         msg='Failed: Invalid update collection sets form')

    def test_form_invalid_status(self):
        """
        Check if collection set update (build status choice) form is invalid
        """
        update_col_form = UpdateCol({'build_status': 'Built'})
        self.assertFalse(
            update_col_form.is_valid(),
            msg='Failed: Invalid update sets (build status choice) form')
