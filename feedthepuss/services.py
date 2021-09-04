from feedthepuss.models import User


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
            pet.Feed()
            pet.save()
