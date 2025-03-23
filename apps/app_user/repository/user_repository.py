from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_user.models import User
from apps.app_user.utils import to_domain_user


class UserRepository(IUserRepository):
    def get(self, *args, **kwargs):
        return User.objects

    def get_by_id(self, id, *args, **kwargs):
        user = User.objects.get(id=id)
        return to_domain_user(user)
    
    def get_by_email(self, email, *args, **kwargs):
        user = User.objects.get(
            email = email
        )
        return to_domain_user(user)
    
    def update(self, dto, *args, **kwargs):
        user = User.objects.get(id = dto.id)
        user.email = dto.email
        user.password = dto.password
        user.client_type = dto.client_type
        user.city = dto.city
        user.is_superuser = dto.is_superuser
        user.is_staff = dto.is_staff
        user.save()
        return to_domain_user(user)
    
    def add(self, dto, *args, **kwargs):
        user = User(
            email = dto.email,
            password = dto.password,
            client_type = dto.client_type,
            city = dto.city,
            is_superuser = dto.is_superuser,
            is_staff = dto.is_staff
        )
        user.save()
        return to_domain_user(user)
    
    def delete(self, id, *args, **kwargs):
        user = User.objects.get(
            id = id
        )
        user.delete()
        return to_domain_user(user)
        