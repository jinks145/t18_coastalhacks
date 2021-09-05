from feedthepuss.models import User, Report
from datetime import datetime, timedelta
from background_task import background
from background_task.models import Task

class UserService:

    
    
    @staticmethod
    @background(schedule=datetime.today().replace(hour=22, minute=30))
    def reportSuccess(email: str):
        # User Must have A pet
        user = User.objects.get(email)
        pet = user.getPet()
        if pet is not None and UserService.hasNotCheated(user):
            pet.Feed()
            pet.save()

    @staticmethod
    def hasNotCheated(current: User):
        # filters the code by
        dayreports = Report.objects.filter(
            created_by=current,
            created_at__lte=datetime.today(),
            created_at__gte=datetime.today() - timedelta(days=2),
        )
        if dayreports.count() == 2 or dayreports.filter(is_success=False).exists():
            return False
        return True
