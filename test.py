import unittest 
import pythonassignment
import persons
class username_exist(unittest.TestCase):

    def test_sql_inj(self):
        with self.assertRaises(Exception) as x:
            pythonassignment.userexists("' or '' = '") 
        self.assertTrue(x.exception,Exception('username not in database'))
    def test_not_in_database(self):
        with self.assertRaises(Exception):
            pythonassignment.userexists("' or '' = '")
    def test_not_specified_city(self):
        a = persons.person('randomusername')
        self.assertEqual(a.city,'Roorkee')
    def test_specified_city(self):
        city = 'city'
        a = persons.person('username',city=city)
        self.assertEqual(a.city,city)
    def test_work_not_exist(self):
        with self.assertRaises(AttributeError):
            persons.scrape('abk.maloo')
            persons.person.names['abk.maloo'].work
    def test_show(self):
        username = 'usename'
        self.assertTrue('My name is username and my current city is Roorkee', persons.person(username).show())
    def test_favs_not_exist(self):
        a = persons.scrape('swapnil.negi09')
        self.assertEqual(a,'no favourites to show')
    def test_favs_exist(self):
        a = persons.scrape('k4ni5h')
        self.assertEqual(type(a),type({}))
    def test_alreadyscraped(self):
        a = persons.scrape('shaddygarg')
        a = persons.scrape('shaddygarg')
        self.assertEqual(a,persons.person.names['shaddygarg'].show())
    def test_person_not_indb(self):
        
        with self.assertRaises(Exception) as x:
            persons.scrape('asd')
        self.assertTrue(x.exception,Exception('username not in database'))
if __name__ =='__main__':
    unittest.main()
