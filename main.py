import os

from typing import AsyncGenerator
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select
from uvicorn import lifespan

import models
import schemas
from models import Base
from schemas import TransactionRead
from dotenv import load_dotenv

from contextlib import asynccontextmanager

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set")
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
app = FastAPI(lifespan=lifespan)
@app.get("/")
async def root():
    return {"status": "ok"}
@app.post(
    "/transactions",
    response_model=TransactionRead
)
async def create_transaction(
        item: schemas.TransactionCreate,
        db: AsyncSession = Depends(get_db)
):
    db_item = models.Transaction(**item.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
@app.get("/transactions", response_model=list[schemas.TransactionRead])
async def read_transactions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Transaction))
    return result.scalars().all()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
