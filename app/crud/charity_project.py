from sqlalchemy import select, true, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject

# from crud.base import CRUDBase
# from models import CharityProject


class CharityProjectCRUD(CRUDBase):
    """
    Класс для CRUD-операций модели CharityProject.
    Добавлен метод для запроса пожертвований текущего юзера.
    """

    async def get_top_quick_closure_projects(self, session=AsyncSession):
        """
        Получает список проектов, отсортированных по скорости закрытия.
        """

        projects = await session.execute(
            select(
                [CharityProject.name,
                 CharityProject.description,
                 (
                    func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date)
                 ).label('closing_time')]
            ).where(CharityProject.fully_invested == true()
            ).order_by('closing_time')
        )
        projects = projects.all()
        return projects


charity_project_crud = CharityProjectCRUD(CharityProject)
