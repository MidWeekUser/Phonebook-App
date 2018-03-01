"""
Phonebook testing
"""

import unittest

from contacts import Contacts


class ContactsTest(unittest.TestCase):

    def setUp(self):
        self.phonecontacts = Contacts('tmpdir')

    def tearDown(self):
        self.phonecontacts.clear()

    def testing_to_find_entries(self):
        self.phonecontacts.add_contact('Mwangi', '1564898')
        self.assertEqual('1564898', self.phonecontacts.check_name('Mwangi'))

    def test_if_phone_book_is_empty(self):
        self.assertTrue(self.phonecontacts.consistency())

    def test_phonebook_with_normal_entries_consistency(self):
        self.phonecontacts.add_contact('Mwangi', '87923')
        self.phonecontacts.add_contact('Ochieng', '48648')
        self.assertTrue(self.phonecontacts.consistency())

    def testing_for_duplicate_entries(self):
        self.phonecontacts.add_contact('Mwangi', '48648')
        self.phonecontacts.add_contact('Ochieng', '48648')
        self.assertFalse(self.phonecontacts.consistency())

    def testing_adding_new_contacts(self):
        self.phonecontacts.add_contact('Atieno', '475869')
        self.assertIn('Atieno', self.phonecontacts.get_all_names())
        self.assertIn('475869', self.phonecontacts.check_name('Atieno'))

    def testing_removing_contacts(self):
        self.phonecontacts.add_contact('Atieno', '475869')
        self.phonecontacts.remove_contact('Atieno', '475869')
        self.assertIn('Atieno', self.phonecontacts.get_all_names())
        self.assertIn('475869', self.phonecontacts.check_name('Atieno'))
