from domain.repository.mapper import IMapper
from domain.entity import UserSubscribe as DUserSubscribe
from domain.entity.type import CLIENT_TYPE
from apps.app_subscribe.models import UserSubscribe
from apps.app_user.utils.to_domain import to_domain_user


class UserSubscribeMapper(IMapper[DUserSubscribe, UserSubscribe]):
    def to_domain(self, model):
        return DUserSubscribe(
            id = model.id,
            created_at = model.created_at,
            user_id = model.user.id,
            subscribe_type = model.subscribe_type
        )
    
    def to_model(self, entity):
        return UserSubscribe(
            id = entity.id,
            subscribe_type = entity.subscribe_type,
            created_at = entity.created_at
        )
    
    def deep_to_domain(self, model):
        subscribe_type = CLIENT_TYPE.from_value(model.subscribe_type)
        return DUserSubscribe(
            id = model.id,
            created_at = model.created_at,
            user_id = model.user.id,
            subscribe_type = subscribe_type,
            user = to_domain_user(model.user)
        )