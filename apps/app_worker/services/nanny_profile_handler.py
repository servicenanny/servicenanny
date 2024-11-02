from dataclasses import dataclass

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.db import transaction

from apps.app_worker.models import Nanny
from apps.app_infrastructure.models import City


@dataclass
class UpdateUserDTO:
    """
    DTO for update user info in nanny profile
    """
    user_id: int
    first_name: str
    last_name: str


@dataclass
class UpdateNannyDTO:
    """
    DTO for update nanny info in nanny profile
    """
    user_id: int
    phone_number: str
    cost_per_hour: int
    photo: str
    city: City
    work_days: str
    age: int
    experience: int
    describe: str

@dataclass
class UpdateProfileDTO(UpdateNannyDTO, UpdateUserDTO):
    ...


class NannyProfileHandler:
    def update_profile(self, dto: UpdateProfileDTO) -> None:
        self.update_user_info(dto)
        self.update_nanny_info(dto)

    def update_user_info(self, dto: UpdateUserDTO) -> AbstractBaseUser:
        user = get_user_model().objects.get(id = dto.user_id)
        user.first_name = dto.first_name
        user.last_name = dto.last_name
        user.save()
        return user

    def update_nanny_info(self, dto: UpdateNannyDTO) -> Nanny:
        nanny = Nanny.objects.get(user__id = dto.user_id)
        raise Exception(nanny)
        nanny.phone_number = dto.phone_number
        nanny.cost_per_hour = dto.cost_per_hour
        nanny.photo = dto.photo
        nanny.city = dto.city
        nanny.work_days = dto.work_days
        nanny.age = dto.age
        nanny.experience = dto.experience
        nanny.describe = dto.describe
        nanny.save()
        return nanny