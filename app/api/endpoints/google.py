from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser, current_user

from app.crud.charity_project import charity_project_crud

from app.services.google_api import (spreadsheets_create,
                                     spreadsheets_update_value,
                                     set_user_permissions)

# from core.db import get_async_session
# from core.google_client import get_service
# from core.user import current_superuser, current_user
#
# from crud.charity_project import charity_project_crud
#
# from services.google_api import (spreadsheets_create,
#                                  spreadsheets_update_value,
#                                  set_user_permissions)

router = APIRouter()


@router.get(
    '/',
    # response_model=list[dict[str, int]],
    dependencies=[Depends(current_superuser)],
)
async def get_projects_by_completion_rate(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)
):
    projects = await charity_project_crud.get_top_quick_closure_projects(
        session=session
    )
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(
        spreadsheetid,
        projects,
        wrapper_services
    )
    return projects
