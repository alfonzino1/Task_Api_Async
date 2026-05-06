from pydantic import BaseModel, ConfigDict


class TransactionCreate(BaseModel):
    manager : str
    amount : float

class TransactionRead(TransactionCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
