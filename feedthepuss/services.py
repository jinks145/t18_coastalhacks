from feedthepuss.models import User, Report
from datetime import datetime, timedelta


class UserService:
    @staticmethod
    def reportSuccess(user: User):
        # User Must have A pet
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
