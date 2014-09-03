import unittest
from contact.models import MyContact
from contact.app import get_app
from contact.database import drop_all_tables


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        app = get_app('test')
        self.app = app.test_client()

    @classmethod
    def tearDownClass(self):
        print "dropping tables after test suite run completely"
        drop_all_tables(self.app.application)

    def test_01_empty_data(self):
        rv = self.app.get('/')
        assert "Please add some contacts" in rv.data, "Emtpy database test failed!"

    def test_02_post_new_contact(self):
        rv = self.app.post('/add', data={'name': 'Test', 'number': '123455', 'about': 'test about'})
        assert "Redirecting..." in rv.data, "ERROR - Not redirected to index page after create"
        rv_index = self.app.get('/')
        assert "Test-123455" in rv_index.data, "ERROR - saved item not displayed."

    def test_03_post_edit_contact(self):
        contact = MyContact.query.first()
        rv = self.app.post('/edit/contact/{id}'.format(id=contact.id), data={'name': 'Test-Update', 'number': '123455', 'about': 'test about'})
        assert "Contact Updated !!" in rv.data, "ERROR - Updated flash message not found."
        assert "Test-Update" in rv.data, "ERROR - saved item not displayed"
        self.assertEqual("<MyContact - Test-Update - 123455>", MyContact.query.first().__repr__(), 'ERROR - Update not reflected in database')

    def test_delete_contact(self):
        contact = MyContact.query.first()
        rv = self.app.post('/delete/contact/{id}'.format(id=contact.id))
        assert "Redirecting..." in rv.data, "ERROR - Not redirected to index page after delete"
        self.assertEqual(MyContact.query.get(contact.id), None, "ERROR - Deleted contact still quried.")

if __name__ == '__main__':
    unittest.main()
