from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.operations import Operation

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(session: Session = Depends(get_session)):
    operations = (
        session
        .query(tables.Operation)
        .all()
    )
    return operations
