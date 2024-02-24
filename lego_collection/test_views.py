from django.test import TestCase
from django.urls import reverse
from .models import LegoSet
from .views import *


class TestCreateUser(TestCase):
    """
    Testing create user functionality
    Testing overall sign-up page view
    """
    def test_signup(self):
        """
        Test sign-up page
        """
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!-- Page for users to create an account -->',
                      response.content,
                      msg='Failed: Valid sign-up page')

    def test_create_user(self):
        """
        Test CustomUser creation
        """
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'test_user',
                                     'email': 'test_user@test.com',
                                     'password1': 't€$T9511',
                                     'password2': 't€$T9511'},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully signed in as test_user.',
                      response.content,
                      msg='Failed: Valid create user')


class TestHomepage(TestCase):
    """
    Test view for homepage
    """
    def setUp(self):
        """
        Create test user for test cases
        """
        self.user = CustomUser.objects.create_user(
            username='test_homepage',
            password='t€$T951',
            email='test_homepage@test.com',
            privacy='PRV'
        )

    def test_home_view_logged_out(self):
        """
        Test homepage view when not logged in
        """
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'create an account</a> to save and view',
                      response.content,
                      msg='Failed: Valid homepage logged out view')

    def test_home_view_logged_in(self):
        """
        Test homepage view when logged in
        """
        self.client.login(username='test_homepage', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Happy collecting!', response.content,
                      msg='Failed: Valid homepage logged in view')

    def test_home_widget_logged_out(self):
        """
        Test homepage profile widget when not logged in
        """
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Forgot Login/Password',
                      response.content,
                      msg='Failed: Valid homepage widget logged out view')

    def test_home_widget_logged_in(self):
        """
        Test homepage profile widget when logged in
        """
        self.client.login(username='test_homepage', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sets owned', response.content,
                      msg='Failed: Valid homepage widget logged in view')


class TestSortFilter(TestCase):
    """
    Testing sorting and filtering
    """
    def setUp(self):
        """
        Create test sets for test cases
        Create test user for test cases
        Create test collection for test cases
        Add test sets to test collection for test cases
        """
        # Create test sets
        LegoSet.objects.create(set_number=12345,
                               set_name='Test Set Status')
        LegoSet.objects.create(set_number=11111,
                               set_name='Test Set Name')
        LegoSet.objects.create(set_number=0,
                               set_name='Test Set Number')
        LegoSet.objects.create(set_number=3500,
                               set_name='Test Set Pieces u500',
                               nr_of_pieces=400)
        LegoSet.objects.create(set_number=31000,
                               set_name='Test Set Pieces u1000',
                               nr_of_pieces=900)
        LegoSet.objects.create(set_number=30500,
                               set_name='Test Set Pieces o500',
                               nr_of_pieces=600)
        LegoSet.objects.create(set_number=301000,
                               set_name='Test Set Pieces o1000',
                               nr_of_pieces=1100)
        LegoSet.objects.create(set_number=302500,
                               set_name='Test Set Pieces o2500',
                               nr_of_pieces=2600)
        LegoSet.objects.create(set_number=305000,
                               set_name='Test Set Pieces o5000',
                               nr_of_pieces=6000)
        LegoSet.objects.create(set_number=44444,
                               set_name='Test Set Location')
        LegoSet.objects.create(set_number=55555,
                               set_name='Test Set Missing')
        LegoSet.objects.create(set_number=66666,
                               set_name='Test Set Favourited')

        # Create test user
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

        # Create collection and add sets
        Collection.objects.create(
            collection_name='Test Collection',
            collection_owner=CustomUser.objects.get(username='test_user'))
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='B',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='BN',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='EX',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='STORED',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='WL',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=11111),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=0),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=3500),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=31000),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=30500),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=301000),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=302500),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=305000),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=44444),
            build_status='NEW',
            set_location='Test',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=55555),
            build_status='NEW',
            missing_pieces='Test',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_user')),
            set=LegoSet.objects.get(set_number=66666),
            build_status='NEW',
            favourited=1)

    def test_sort_nr(self):
        """
        Test sorting for Set Number
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=nr')
        set_0 = str(response.content).find(
            '<td class="set-nr-col">0</td>')
        set_66666 = str(response.content).find(
            '<td class="set-nr-col">66666</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(set_0 < set_66666,
                        msg='Failed: Valid Set Number sorting')

    def test_rsort_nr(self):
        """
        Test reverse sorting for Set Number
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=nr')
        set_0 = str(response.content).find(
            '<td class="set-nr-col">0</td>')
        set_66666 = str(response.content).find(
            '<td class="set-nr-col">66666</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(set_0 < set_66666,
                         msg='Failed: Valid Set Number reverse sorting')

    def test_sort_name(self):
        """
        Test sorting for Set Name
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=name')
        set_fave = str(response.content).find(
            'Test Set Favourited')
        set_stat = str(response.content).find(
            'Test Set Status')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(set_fave < set_stat,
                        msg='Failed: Valid Set Name sorting')

    def test_rsort_name(self):
        """
        Test reverse sorting for Set Name
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=name')
        set_fave = str(response.content).find(
            'Test Set Favourited')
        set_stat = str(response.content).find(
            'Test Set Status')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(set_fave < set_stat,
                         msg='Failed: Valid Set Name reverse sorting')

    def test_sort_pieces(self):
        """
        Test sorting for # of Pieces
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=pieces')
        set_null = str(response.content).find(
            '<td class="set-pieces-col">None</td>')
        set_400 = str(response.content).find(
            '<td class="set-pieces-col">400</td>')
        set_6000 = str(response.content).find(
            '<td class="set-pieces-col">6000</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(set_400 < set_6000 < set_null,
                        msg='Failed: Valid # of Pieces sorting')

    def test_rsort_pieces(self):
        """
        Test reverse sorting for # of Pieces
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=pieces')
        set_null = str(response.content).find(
            '<td class="set-pieces-col">None</td>')
        set_400 = str(response.content).find(
            '<td class="set-pieces-col">400</td>')
        set_6000 = str(response.content).find(
            '<td class="set-pieces-col">6000</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(set_400 < set_6000 < set_null,
                         msg='Failed: Valid # of Pieces reverse sorting')

    def test_sort_status(self):
        """
        Test sorting for Build Status
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=status')
        built_set = str(response.content).find(
            '<td class="set-status-col">Built</td>')
        new_set = str(response.content).find(
            '<td class="set-status-col">New (Owned)</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(built_set < new_set,
                        msg='Failed: Valid Build Status sorting')

    def test_rsort_status(self):
        """
        Test reverse sorting for Build Status
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=status')
        built_set = str(response.content).find(
            '<td class="set-status-col">Built</td>')
        new_set = str(response.content).find(
            '<td class="set-status-col">New (Owned)</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(built_set < new_set,
                         msg='Failed: Valid Build Status reverse sorting')

    def test_sort_loc(self):
        """
        Test sorting for Location
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=loc')
        test_loc = str(response.content).find(
            '<td class="set-loc-col">Test</td>')
        no_loc = str(response.content).find(
            '<td class="set-loc-col">None</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(test_loc < no_loc,
                        msg='Failed: Valid Location sorting')

    def test_rsort_loc(self):
        """
        Test reverse sorting for Location
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=loc')
        test_loc = str(response.content).find(
            '<td class="set-loc-col">Test</td>')
        no_loc = str(response.content).find(
            '<td class="set-loc-col">None</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(test_loc < no_loc,
                         msg='Failed: Valid Location reverse sorting')

    def test_sort_missing(self):
        """
        Test sorting for Missing Pieces
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=missing')
        test_miss = str(response.content).find(
            '<td class="set-miss-col">Test</td>')
        no_miss = str(response.content).find(
            '<td class="set-miss-col">None</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(test_miss < no_miss,
                        msg='Failed: Valid Missing Pieces sorting')

    def test_rsort_missing(self):
        """
        Test reverse sorting for Missing Pieces
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=missing')
        test_miss = str(response.content).find(
            '<td class="set-miss-col">Test</td>')
        no_miss = str(response.content).find(
            '<td class="set-miss-col">None</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(test_miss < no_miss,
                         msg='Failed: Valid Missing Pieces reverse sorting')

    def test_sort_fave(self):
        """
        Test sorting for Favourited
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?sort=fav')
        test_fave = str(response.content).find(
            '<td>Test Set Favourited</td>')
        no_fave = str(response.content).find(
            '<td>Test Set Missing</td>')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(test_fave < no_fave,
                        msg='Failed: Valid Favourited sorting')

    def test_rsort_fave(self):
        """
        Test reverse sorting for Favourited
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?rsort=fav')
        test_fave = str(response.content).find(
            '<td>Test Set Favourited</td>')
        no_fave = str(response.content).find(
            '<td>Test Set Missing</td>')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(test_fave < no_fave,
                         msg='Failed: Valid Favourited reverse sorting')

    def test_filter_u500(self):
        """
        Test set filtering for # Pieces <500
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=u500')
        set_u500 = b'<td class="set-pieces-col">400</td>'
        set_o500 = b'<td class="set-pieces-col">900</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_o500, response.content,
                         msg='Failed: No results <500 filter')
        self.assertIn(set_u500, response.content,
                      msg='Failed: Valid <500 filtering')

    def test_filter_u1000(self):
        """
        Test set filtering for # Pieces <1000
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=u1000')
        set_u1000 = b'<td class="set-pieces-col">900</td>'
        set_o1000 = b'<td class="set-pieces-col">1100</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_o1000, response.content,
                         msg='Failed: No results <1000 filter')
        self.assertIn(set_u1000, response.content,
                      msg='Failed: Valid <1000 filtering')

    def test_filter_o500(self):
        """
        Test set filtering for # Pieces >500
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=o500')
        set_o500 = b'<td class="set-pieces-col">900</td>'
        set_u500 = b'<td class="set-pieces-col">400</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_u500, response.content,
                         msg='Failed: No results >500 filter')
        self.assertIn(set_o500, response.content,
                      msg='Failed: Valid >500 filtering')

    def test_filter_o1000(self):
        """
        Test set filtering for # Pieces >1000
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=o1000')
        set_o1000 = b'<td class="set-pieces-col">1100</td>'
        set_u1000 = b'<td class="set-pieces-col">900</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_u1000, response.content,
                         msg='Failed: No results >1000 filter')
        self.assertIn(set_o1000, response.content,
                      msg='Failed: Valid >1000 filtering')

    def test_filter_o2500(self):
        """
        Test set filtering for # Pieces >2500
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=o2500')
        set_o2500 = b'<td class="set-pieces-col">2600</td>'
        set_u2500 = b'<td class="set-pieces-col">1100</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_u2500, response.content,
                         msg='Failed: No results >2500 filter')
        self.assertIn(set_o2500, response.content,
                      msg='Failed: Valid >2500 filtering')

    def test_filter_o5000(self):
        """
        Test set filtering for # Pieces >5000
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=o5000')
        set_o5000 = b'<td class="set-pieces-col">6000</td>'
        set_u5000 = b'<td class="set-pieces-col">2600</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_u5000, response.content,
                         msg='Failed: No results >5000 filter')
        self.assertIn(set_o5000, response.content,
                      msg='Failed: Valid >5000 filtering')

    def test_filter_new(self):
        """
        Test set filtering for build status = New
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=new')
        built_set = b'<td class="set-status-col">Built</td>'
        new_set = b'<td class="set-status-col">New (Owned)</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(built_set, response.content,
                         msg='Failed: No results NEW filter')
        self.assertIn(new_set, response.content,
                      msg='Failed: Valid NEW filtering')

    def test_filter_bn(self):
        """
        Test set filtering for build status = Build Next
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=bnext')
        bn_set = b'<td class="set-status-col">Build Next</td>'
        built_set = b'<td class="set-status-col">Built</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(built_set, response.content,
                         msg='Failed: No results BN filter')
        self.assertIn(bn_set, response.content,
                      msg='Failed: Valid BN filtering')

    def test_filter_b(self):
        """
        Test set filtering for build status = Built
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=built')
        bn_set = b'<td class="set-status-col">Build Next</td>'
        built_set = b'<td class="set-status-col">Built</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(bn_set, response.content,
                         msg='Failed: No results B filter')
        self.assertIn(built_set, response.content,
                      msg='Failed: Valid B filtering')

    def test_filter_ex(self):
        """
        Test set filtering for build status = Extra
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=extra')
        built_set = b'<td class="set-status-col">Built</td>'
        ex_set = b'<td class="set-status-col">Extra</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(built_set, response.content,
                         msg='Failed: No results EX filter')
        self.assertIn(ex_set, response.content,
                      msg='Failed: Valid EX filtering')

    def test_filter_s(self):
        """
        Test set filtering for build status = Stored
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=stored')
        new_set = b'<td class="set-status-col">New (Owned)</td>'
        s_set = b'<td class="set-status-col">Stored</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(new_set, response.content,
                         msg='Failed: No results STORED filter')
        self.assertIn(s_set, response.content,
                      msg='Failed: Valid STORED filtering')

    def test_filter_wl(self):
        """
        Test set filtering for build status = Wish List
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=wishlist')
        s_set = b'<td class="set-status-col">Stored</td>'
        wl_set = b'<td class="set-status-col">Wish List</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(s_set, response.content,
                         msg='Failed: No results WL filter')
        self.assertIn(wl_set, response.content,
                      msg='Failed: Valid WL filtering')

    def test_filter_loc_y(self):
        """
        Test set filtering for Set Location = Yes
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=loc-yes')
        set_loc = b'<td class="set-loc-col">Test</td>'
        set_no_loc = b'<td class="set-loc-col">None</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_no_loc, response.content,
                         msg='Failed: No results Set Location filter')
        self.assertIn(set_loc, response.content,
                      msg='Failed: Valid Set Location filtering')

    def test_filter_loc_n(self):
        """
        Test set filtering for Set Location = No
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=loc-no')
        set_loc = b'<td class="set-loc-col">Test</td>'
        set_no_loc = b'<td class="set-loc-col">None</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_loc, response.content,
                         msg='Failed: No results no Set Location filter')
        self.assertIn(set_no_loc, response.content,
                      msg='Failed: Valid no Set Location filtering')

    def test_filter_miss_y(self):
        """
        Test set filtering for Missing Pieces = Yes
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=miss-yes')
        set_miss = b'<td class="set-miss-col">Test</td>'
        set_no_miss = b'<td class="set-miss-col">None</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_no_miss, response.content,
                         msg='Failed: No results Missing Pieces filter')
        self.assertIn(set_miss, response.content,
                      msg='Failed: Valid Missing Pieces filtering')

    def test_filter_miss_n(self):
        """
        Test set filtering for Missing Pieces = No
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=miss-no')
        set_miss = b'<td class="set-miss-col">Test</td>'
        set_no_miss = b'<td class="set-miss-col">None</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_miss, response.content,
                         msg='Failed: No results no Missing Pieces filter')
        self.assertIn(set_no_miss, response.content,
                      msg='Failed: Valid no Missing Pieces filtering')

    def test_filter_fave_y(self):
        """
        Test set filtering for Favourited = Yes
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=fav-yes')
        set_fave = b'<td>Test Set Favourited</td>'
        set_no_fave = b'<td>Test Set Missing</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_no_fave, response.content,
                         msg='Failed: No results Favourites filter')
        self.assertIn(set_fave, response.content,
                      msg='Failed: Valid Favourites filtering')

    def test_filter_fave_n(self):
        """
        Test set filtering for Favourited = No
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get('/collections/?filter=fav-no')
        set_fave = b'<td>Test Set Favourited</td>'
        set_no_fave = b'<td>Test Set Missing</td>'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(set_fave, response.content,
                         msg='Failed: No results no Favourites filter')
        self.assertIn(set_no_fave, response.content,
                      msg='Failed: Valid no Favourites filtering')


class TestCollections(TestCase):
    """
    Test view for collections
    """
    def setUp(self):
        """
        Create test set for test cases
        Create test users for test cases
        Create test collections for test cases
        """
        # Create test set
        LegoSet.objects.create(set_number=12345, set_name='Test Set')

        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_no_col',
            password='t€$T951',
            email='test_no_col@test.com',
            privacy='PRV'
        )

        # User with a collection without sets
        self.user = CustomUser.objects.create_user(
            username='test_col',
            password='t€$T951',
            email='test_col@test.com',
            privacy='PRV'
        )

        # User with a collection and with sets
        self.user = CustomUser.objects.create_user(
            username='test_set',
            password='t€$T951',
            email='test_sets@test.com',
            privacy='PRV'
        )

        # Create collection for test_col
        Collection.objects.create(
            collection_name='Test Collection No Sets',
            collection_owner=CustomUser.objects.get(username='test_col'))

        # Create collection and add set for test_set
        Collection.objects.create(
            collection_name='Test Collection With Sets',
            collection_owner=CustomUser.objects.get(username='test_set'))
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_set')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='NEW',
            favourited=0)

    def test_col_view_logged_out(self):
        """
        Test collections view when not logged in
        """
        self.client.logout()
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'create an account</a> to save and view',
                      response.content,
                      msg='Failed: Valid collections logged out view')

    def test_col_view_no_col(self):
        """
        Test collections view when logged in
        User without a collection
        """
        self.client.login(username='test_no_col', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create Collection',
                      response.content,
                      msg='Failed: Valid collections no collection view')

    def test_col_view_no_sets(self):
        """
        Test collections view when logged in
        User with collection without sets
        """
        self.client.login(username='test_col', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No sets in (filtered) collection.',
                      response.content,
                      msg='Failed: Valid collections no sets view')

    def test_col_view_w_sets(self):
        """
        Test collections view when logged in
        User with collection and sets
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Set Name',
                      response.content,
                      msg='Failed: Valid collections with sets view')

    def test_delete_col(self):
        """
        Test collection deletion
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.post(reverse('collections'),
                                    {'delete-col-button': True})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collection successfully deleted',
                      response.content,
                      msg='Failed: Successful collection deletion')


class TestProfileWidget(TestCase):
    """
    Test view for profile widget
    """
    def setUp(self):
        """
        Create test set for test cases
        Create test users for test cases
        Create test collections for test cases
        """
        # Create test set
        LegoSet.objects.create(set_number=12345, set_name='Test Set')

        # User without collection
        self.user = CustomUser.objects.create_user(
            username='test_no_col',
            password='t€$T951',
            email='test_no_col@test.com',
            privacy='PRV'
        )

        # User without sets
        self.user = CustomUser.objects.create_user(
            username='test_no_sets',
            password='t€$T951',
            email='test_no_sets@test.com',
            privacy='PRV'
        )

        # User with owned sets
        self.user = CustomUser.objects.create_user(
            username='test_set',
            password='t€$T951',
            email='test_sets@test.com',
            privacy='PRV'
        )

        # User with wish list sets
        self.user = CustomUser.objects.create_user(
            username='test_wl',
            password='t€$T951',
            email='test_wl@test.com',
            privacy='PRV'
        )

        # User with owned and wish list sets
        self.user = CustomUser.objects.create_user(
            username='test_sets_wl',
            password='t€$T951',
            email='test_sets_wl@test.com',
            privacy='PRV'
        )

        # Create collection for test_no_sets
        Collection.objects.create(
            collection_name='Test Collection No Sets',
            collection_owner=CustomUser.objects.get(username='test_no_sets'))

        # Create collection and add set for test_set
        Collection.objects.create(
            collection_name='Test Collection With Sets',
            collection_owner=CustomUser.objects.get(username='test_set'))
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_set')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='NEW',
            favourited=0)

        # Create collection and add wish list set for test_wl
        Collection.objects.create(
            collection_name='Test Collection With Wish List',
            collection_owner=CustomUser.objects.get(username='test_wl'))
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(username='test_wl')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='WL',
            favourited=0)

        # Create collection and add owned and wish list set for test_sets_wl
        Collection.objects.create(
            collection_name='Test Collection With Sets and Wish List',
            collection_owner=CustomUser.objects.get(
                username='test_sets_wl'))
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(
                    username='test_sets_wl')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='WL',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(
                    username='test_sets_wl')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='NEW',
            favourited=0)
        LegoCollection.objects.create(
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(
                    username='test_sets_wl')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='B',
            favourited=0)

    def test_home_widget_no_col(self):
        """
        Test profile widget on homepage
        User without collection
        """
        self.client.login(username='test_no_col', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sets owned: 0',
                      response.content,
                      msg='Failed: Valid homepage widget no collection (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid homepage widget no collection (wl)')

    def test_col_widget_no_col(self):
        """
        Test profile widget on collections page
        User without collection
        """
        self.client.login(username='test_no_col', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid collections widget no collection (sets)')
        self.assertIn(
            b'Wish list: 0',
            response.content,
            msg='Failed: Valid collections widget no collection (wl)')

    def test_profile_no_col(self):
        """
        Test set details on profile page
        User without collection
        """
        self.client.login(username='test_no_col', password='t€$T951')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid profile widget no collection (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid profile widget no collection (wl)')

    def test_shared_no_col(self):
        """
        Test set details on shared page
        User without collection
        """
        self.client.login(username='test_no_col', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid shared widget no collection (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid shared widget no collection (wl)')

    def test_home_widget_no_sets(self):
        """
        Test profile widget on homepage
        User with collection without sets
        """
        self.client.login(username='test_no_sets', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sets owned: 0',
                      response.content,
                      msg='Failed: Valid homepage widget no sets (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid homepage widget no sets (wl)')

    def test_col_widget_no_sets(self):
        """
        Test profile widget on collections page
        User with collection without sets
        """
        self.client.login(username='test_no_sets', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid collections widget no sets (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid collections widget no sets (wl)')

    def test_profile_no_sets(self):
        """
        Test set details on profile page
        User with collection without sets
        """
        self.client.login(username='test_no_sets', password='t€$T951')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid profile widget no sets (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid profile widget no sets (wl)')

    def test_shared_no_sets(self):
        """
        Test set details on shared page
        User with collection without sets
        """
        self.client.login(username='test_no_sets', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid shared widget no sets (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid shared widget no sets (wl)')

    def test_home_widget_set(self):
        """
        Test profile widget on homepage
        User with collection and set
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 1',
            response.content,
            msg='Failed: Valid homepage widget with owned set (sets)')
        self.assertIn(
            b'Wish list: 0',
            response.content,
            msg='Failed: Valid homepage widget with owned set (wl)')

    def test_col_widget_set(self):
        """
        Test profile widget on collections page
        User with collection and set
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 1',
            response.content,
            msg='Failed: Valid collections widget with owned set (sets)')
        self.assertIn(
            b'Wish list: 0',
            response.content,
            msg='Failed: Valid collections widget with owned set (wl)')

    def test_profile_set(self):
        """
        Test set details on profile page
        User with collection and set
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 1',
            response.content,
            msg='Failed: Valid profile widget with owned set (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid profile widget with owned set (wl)')

    def test_shared_set(self):
        """
        Test set details on shared page
        User with collection and set
        """
        self.client.login(username='test_set', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 1',
            response.content,
            msg='Failed: Valid shared widget with owned set (sets)')
        self.assertIn(b'Wish list: 0',
                      response.content,
                      msg='Failed: Valid shared widget with owned set (wl)')

    def test_home_widget_wl(self):
        """
        Test profile widget on homepage
        User with wish list set, without owned set
        """
        self.client.login(username='test_wl', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid homepage widget with wish list set (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid homepage widget with wish list set (wl)')

    def test_col_widget_wl(self):
        """
        Test profile widget on collections page
        User with wish list set, without owned set
        """
        self.client.login(username='test_wl', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid collections widget with wish list set (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid collections widget with wish list set (wl)')

    def test_profile_wl(self):
        """
        Test set details on profile page
        User with wish list set, without owned set
        """
        self.client.login(username='test_wl', password='t€$T951')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid profile widget with wish list set (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid profile widget with wish list set (wl)')

    def test_shared_wl(self):
        """
        Test set details on shared page
        User with wish list set, without owned set
        """
        self.client.login(username='test_wl', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 0',
            response.content,
            msg='Failed: Valid shared widget with wish list set (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid shared widget with wish list set (wl)')

    def test_home_widget_sets_wl(self):
        """
        Test profile widget on homepage
        User with wish list and owned sets
        """
        self.client.login(username='test_sets_wl', password='t€$T951')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 2',
            response.content,
            msg='Failed: Valid homepage widget with WL and owned sets (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid homepage widget with WL and owned sets (wl)')

    def test_col_widget_sets_wl(self):
        """
        Test profile widget on collections page
        User with wish list set and owned sets
        """
        self.client.login(username='test_sets_wl', password='t€$T951')
        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 2',
            response.content,
            msg='Failed: Valid collections widget with WL & owned sets (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid collections widget with WL & owned sets (wl)')

    def test_profile_sets_wl(self):
        """
        Test set details on profile page
        User with wish list and owned sets
        """
        self.client.login(username='test_sets_wl', password='t€$T951')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 2',
            response.content,
            msg='Failed: Valid profile widget with WL & owned sets (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid profile widget with WL & owned sets (wl)')

    def test_shared_sets_wl(self):
        """
        Test set details on shared page
        User with wish list and owned sets
        """
        self.client.login(username='test_sets_wl', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Sets owned: 2',
            response.content,
            msg='Failed: Valid shared widget with WL and owned sets (sets)')
        self.assertIn(
            b'Wish list: 1',
            response.content,
            msg='Failed: Valid shared widget with WL and owned sets (wl)')


class TestProfile(TestCase):
    """
    Test profile page views
    """
    def setUp(self):
        """
        Create test user for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

    def test_profile_logged_out(self):
        """
        Test profile view when not logged in
        """
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Forgot Login/Password',
                      response.content,
                      msg='Failed: Valid profile logged out view')

    def test_profile_logged_in(self):
        """
        Test profile view when logged in
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Email:',
                      response.content,
                      msg='Failed: Valid profile logged in view')

    def test_username_change_valid(self):
        """
        Test username update
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'),
                                    {'username': 'test_change',
                                     'username-button': True},
                                    follow=True)
        self.assertIn(b'Your username has been successfully updated',
                      response.content,
                      msg='Failed: Valid username change')

    def test_username_change_invalid(self):
        """
        Test username update
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'),
                                    {'username': 'test_user',
                                     'username-button': True},
                                    follow=True)
        self.assertIn(b'An account with that username already exists.',
                      response.content,
                      msg='Failed: Invalid username change')

    def test_email_change_valid(self):
        """
        Test email update
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'),
                                    {'email': 'test_change@test.com',
                                     'profile-email-button': True},
                                    follow=True)
        self.assertIn(b'Your email address has been successfully updated',
                      response.content,
                      msg='Failed: Valid email change')

    def test_email_change_invalid(self):
        """
        Test email update
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'),
                                    {'email': 'test_user@test.com',
                                     'profile-email-button': True},
                                    follow=True)
        self.assertIn(b'An account with that email address already exists.',
                      response.content,
                      msg='Failed: Invalid email change')

    def test_privacy_change(self):
        """
        Test privacy setting update
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'),
                                    {'privacy': 'PUB',
                                     'privacy-button': True},
                                    follow=True)
        self.assertIn(b'Your privacy settings have been successfully updated',
                      response.content,
                      msg='Failed: Valid Privacy change')

    def test_delete_account(self):
        """
        Test account deletion
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('profile'), {
            'delete': 1,
            'delete-button': True})
        self.assertIn(b'Account successfully deleted',
                      response.content,
                      msg='Failed: Valid account deletion')


class TestShared(TestCase):
    """
    Test Shared page views
    """
    def setUp(self):
        """
        Create test user for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

    def test_shared_logged_out(self):
        """
        Test Shared view when not logged in
        """
        self.client.logout()
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Forgot Login/Password',
                      response.content,
                      msg='Failed: Valid Shared logged out view')

    def test_shared_logged_in(self):
        """
        Test Shared view when logged in
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('shared'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sharing features coming soon!',
                      response.content,
                      msg='Failed: Valid Shared logged in view')


class TestCreateCollection(TestCase):
    """
    Test view for creating a collection
    """
    def setUp(self):
        """
        Create test user for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

    def test_create_col_logged_out(self):
        """
        Test create collection page when logged out
        """
        self.client.logout()
        response = self.client.get(reverse('create_collection'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Log In</h2>',
                      response.content,
                      msg='Failed: Valid Create Collection logged out view')

    def test_create_col(self):
        """
        Test create collection page
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('create_collection'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collection name:</label>',
                      response.content,
                      msg='Failed: Valid Create Collection view')

    def test_create_col_valid(self):
        """
        Test valid create collection
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('create_collection'),
                                    {'collection_name': 'Test Collection',
                                     'create-col-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your collection has been successfully created.',
                      response.content,
                      msg='Failed: Valid created collection')

    def test_create_col_invalid(self):
        """
        Test invalid create collection
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('create_collection'),
                                    {'collection_name': '',
                                     'create-col-button': True},
                                    follow=True)
        self.assertIn(b'Collection name:</label>',
                      response.content,
                      msg='Failed: Invalid create collection form')


class TestEditCollection(TestCase):
    """
    Test view for editing a collection
    """
    def setUp(self):
        """
        Create test user for test cases
        Create test set for test cases
        Create test collection for test cases
        Add test set to collection for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

        LegoSet.objects.create(set_number=12345, set_name='Test Set')
        Collection.objects.create(
            collection_name='Test Collection',
            collection_owner=CustomUser.objects.get(username='test_user'))
        LegoCollection.objects.create(
            pk=1,
            collection=Collection.objects.get(
                collection_owner=CustomUser.objects.get(
                    username='test_user')),
            set=LegoSet.objects.get(set_number=12345),
            build_status='NEW',
            favourited=0)

    def test_edit_col_logged_out(self):
        """
        Test edit collection page logged out
        """
        self.client.logout()
        response = self.client.get(reverse('edit_collection'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'create an account</a> to save and view',
                      response.content,
                      msg='Failed: Valid Edit Collection view (logged out)')

    def test_edit_col(self):
        """
        Test edit collection page logged in
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('edit_collection'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'col-edit-opt',
                      response.content,
                      msg='Failed: Valid Edit Collection view (logged in)')

    def test_edit_col_details_valid(self):
        """
        Test valid edit collection
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('edit_collection'),
                                    {'collection_name': 'test_collection',
                                     '1-build_status': 'EX',
                                     '1-set_location': 'loc test',
                                     '1-missing_pieces': 'pieces test',
                                     '1-favourited': 1,
                                     'update-col-button': True},
                                    follow=True)
        self.assertIn(b'Collection updated successfully.',
                      response.content)
        self.assertIn(b'<td class="set-status-col">Extra</td>',
                      response.content,
                      msg='Failed: Valid collection edit')

    def test_edit_col_details_invalid(self):
        """
        Test invalid edit collection
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('edit_collection'),
                                    {'collection_name': 'test_collection',
                                     '1-build_status': '',
                                     'update-col-button': True},
                                    follow=True)
        self.assertIn(b'<td class="set-status-col">New (Owned)</td>',
                      response.content,
                      msg='Failed: Invalid create collection form')

    def test_edit_col_delete_set(self):
        """
        Test set deletion in edit collection
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('edit_collection'),
                                    {'collection_name': 'test_collection',
                                     '1-build_status': 'EX',
                                     'delete-set': 1,
                                     'update-col-button': True},
                                    follow=True)
        self.assertIn(b'No sets in (filtered) collection.',
                      response.content,
                      msg='Failed: Valid collection set deletion')


class TestCreateSet(TestCase):
    """
    Test view for creating a set
    """
    def setUp(self):
        """
        Create test user for test cases
        Create test collection for test cases
        Create test set for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

        Collection.objects.create(
            collection_name='Test Collection',
            collection_owner=CustomUser.objects.get(username='test_user'))
        LegoSet.objects.create(set_number=98765, set_name='Test Set Exists')

    def test_create_set_logged_out(self):
        """
        Test set creation page logged out
        """
        self.client.logout()
        response = self.client.get(reverse('create_set'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'create an account</a> to save and view',
                      response.content,
                      msg='Failed: Valid Create Set view (logged out)')

    def test_create_set(self):
        """
        Test valid view for creating a set
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('create_set'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!-- Form to create a new lego set -->',
                      response.content,
                      msg='Failed: Valid Create Set view')

    def test_create_set_valid(self):
        """
        Test valid set creation
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('create_set'),
                                    {'set_number': 12345,
                                     'set_name': 'Test Set Name',
                                     'create-set-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You successfully created a set.',
                      response.content,
                      msg='Failed: Valid set creation')

    def test_create_set_invalid(self):
        """
        Test invalid set creation
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('create_set'),
                                    {'set_number': '',
                                     'set_name': '',
                                     'create-set-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required.',
                      response.content,
                      msg='Failed: Invalid set creation')

    def test_create_set_exists(self):
        """
        Test set creation when the set number already exists
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('create_set'),
                                    {'set_number': 98765,
                                     'set_name': 'Test Set Exists',
                                     'create-set-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This set number already exists.',
                      response.content,
                      msg='Failed: Invalid set creation (set already exists)')


class TestAddSet(TestCase):
    """
    Test view for adding a set
    """
    def setUp(self):
        """
        Create test user for test cases
        Create test collection for test cases
        Create test set for test cases
        """
        # User without a collection
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='t€$T951',
            email='test_user@test.com',
            privacy='PRV'
        )

        Collection.objects.create(
            collection_name='Test Collection',
            collection_owner=CustomUser.objects.get(username='test_user'))
        LegoSet.objects.create(set_number=12345, set_name='Test Set')

    def test_add_set_logged_out(self):
        """
        Test set addition page logged out
        """
        self.client.logout()
        response = self.client.get(reverse('add_set'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'create an account</a> to save and view',
                      response.content,
                      msg='Failed: Valid Add Set view (logged out)')

    def test_add_set(self):
        """
        Test valid view for adding a set
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.get(reverse('add_set'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!-- Form to add a set to the collection -->',
                      response.content,
                      msg='Failed: Valid Add Set view')

    def test_add_set_valid(self):
        """
        Test valid set addition
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('add_set'),
                                    {'set': 12345,
                                     'build_status': 'NEW',
                                     'add-set-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Set successfully added to your collection.',
                      response.content,
                      msg='Failed: Valid set addition')

    def test_add_set_invalid(self):
        """
        Test invalid set addition
        """
        self.client.login(username='test_user', password='t€$T951')
        response = self.client.post(reverse('add_set'),
                                    {'set': '',
                                     'build_status': '',
                                     'add-set-button': True},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required.',
                      response.content,
                      msg='Failed: Invalid set addition')
