from datetime import date, datetime
from feedthepuss.models import Pet
from django.test import TestCase
from feedthepuss.models import User, Pet,Report
from feedthepuss.services import UserService
# Create your tests here.


class TaskTest(TestCase):

    @classmethod
    def setUp(self):
        user1 = User.objects.create(email="test1@gmail.com", age=25, sex="Male")
        user2 = User.objects.create(email="test2@gmail.com", age=25, sex="Female")

        user1 = User.objects.get(email="test1@gmail.com")
        user2 = User.objects.get(email="test2@gmail.com")
        

        pet1 = Pet(user=user1, name= "dog1", weight=30)
        pet2 = Pet(user=user2, name= "cat1", weight=4)
        
        pet1.save()
        pet2.save()

        Report.objects.create(created_by=user1, title="I dont cheat", body="I will win", is_success=True, mealtime=datetime.utcnow())
        Report.objects.create(created_by=user1, title="I dont cheat", body="I will win", is_success=True, mealtime=datetime.utcnow())

        Report.objects.create(created_by=user2, title="I gotta eat", body="I cannot win", is_success=False, mealtime=datetime.utcnow())
        
    
    
    
    def test_user1(self):
        user1 = User.objects.get(email="test1@gmail.com")
        pet1 = Pet.objects.get(user=user1)
        UserService.reportSuccess(user1.email, schedule=60)
        self.AssertEquals(pet1.weight, 50)
        
    def test_user2(self):
        user2 = User.objects.get(email="test2@gmail.com")
        pet1 = Pet.objects.get(user=user2)
        UserService.reportSuccess(user2.email, schedule=60)
        self.AssertEquals(pet1.weight, 4)