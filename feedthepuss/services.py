from feedthepuss.models import User, Report
from datetime import datetime
class UserService:
    def login(self, email: str, password: str):
        from django.contrib.auth import authenticate

        user = authenticate(username="john", password="secret")
        if user is not None:
            pass
        else:
            pass

    @staticmethod
    def reportSuccess(user: User):
        # User Must have A pet
        pet = user.getPet()
        if pet is not None:
            if UserService.hasNotCheated(user):
                pet.Feed()
                pet.save()
                user.resetCheatDay()
            else:
                user.incCheatDay()

    def hasNotCheated(current:User):
        # filters the code by
        dayreports = Report.objects.filter(user=current, created_at__gte= datetime.today(), created_at__lt = datetime.today() + datetime.timedelta(days=1))

        if not dayreports.exists():
            return False
        
        if dayreports.filter(is_meal=False).exists():
            return False
        

        return dayreports.count() == dayreports.filter(is_meal=False) == 3
