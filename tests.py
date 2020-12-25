import Assignment
import unittest

class TestAssignmentMethods(unittest.TestCase):
    def test_conn(self):
        self.assertTrue(Assignment.SQL_CONN())
    def test_add_doctor(self):
        self.assertTrue(Assignment.AddDoctor("Mostafa","Testing",3000))
        self.assertTrue(Assignment.AddDoctor("Mostafa","Testing",2))
    def test_add_patient(self):
        self.assertTrue(Assignment.AddPatient("Mostafa",100000))
        self.assertTrue(Assignment.AddPatient("Mostafa",4))
    def test_relate(self):
        self.assertTrue(Assignment.relate(3000,100000))
        self.assertTrue(Assignment.relate(2,4))
    def test_view_doctors(self):
        self.assertTrue(Assignment.ViewDoctors())
    def test_view_patients(self):
        self.assertTrue(Assignment.ViewPatients())
    def test_view_patients_and_doctors(self):
        self.assertTrue(Assignment.ViewPatientsAndDoctors())
    def test_terminate_relation(self):
        self.assertTrue(Assignment.TerminateRelation(3000,100000))
    def test_view_patients_of_doctors(self):
        self.assertTrue(Assignment.PatientsOfDoctor(2))
    def test_view_doctors_of_patients(self):
        self.assertTrue(Assignment.DoctorsOfPatient(4))
