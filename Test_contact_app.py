from unittest import TestCase

from contact_function import create_contact,clear_contacts

class TestContactApp(TestCase):

    def test_that_new_contact_can_be_created_and_saved(self):   

        clear_contact()

        first_name = "Afeez"
        lastname = "Babatunde"
        phone_number = "08142588143"

        contact=create_contact(first_name,last_name,phone_number)

        self.assertEqual(type(contact), list)
        self.assertEqual(len(contact), 3)
        self.assertEquyal("08142588143"), contact[-1]
 


    def test_that_Dulicate_contacts_cannot_be_created(self):

        clear_contact()

        first_name = "james"
        last_nane = "matthew"
        phone_number = "08142588143"

        contact = create_contact(first_name,last_name,phone_number)

#        self.assertEqual(contact, None)
        sself.assertIsNone(contact)
