from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class DonationCRUD(CRUDBase):
    """
    Класс для CRUD-операций модели Donation.
    """

    async def get_donation_by_user(
            self,
            user: User,
            session: AsyncSession
    ):
        """Запрос пожертвований текущего юзера."""

        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()


donation_crud = DonationCRUD(Donation)
