from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import operation
from src.operations.shemas import OperationCreate, ProductCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get('/')
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result


@router.post('/')
async def post_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': "success"}


# @router.put('/')
# async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(operation).where(operation.c.type == operation_type)
#     result = await session.execute(query)
#     return result
#

@router.post("/product/")
async def post_specific_operations(operation_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    # stmt = insert(ProductCreate).values(**operation_product.dict())
    # await session.execute(stmt)
    await session.commit()
    return operation_product
