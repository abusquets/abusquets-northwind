from auth.di.mixins import AuthContainerMixin
from config import settings
from infra.cache.ports import AbstractCacheRepository
from infra.cache.redis_cache import RedisCache
from infra.database.sqlalchemy.session import AbstractDatabase, Database
from northwind.di.mixins import NorthwindContainerMixin
from utils.di import DIContainer, di_singleton


class AppContainerMixin:
    db: AbstractDatabase
    cache_repository: AbstractCacheRepository

    def _get_db(self) -> AbstractDatabase:
        return Database()

    @di_singleton
    def _get_cache_repository(self) -> AbstractCacheRepository:
        return RedisCache(
            url=settings.REDIS_URL,
            user=settings.REDIS_USER,
            password=settings.REDIS_PASSWORD,
        )


# @singleton
class AppContainer(NorthwindContainerMixin, AuthContainerMixin, AppContainerMixin, DIContainer):
    pass
