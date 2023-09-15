from pydantic import BaseModel

STATUS_IN_DELIVERY = 1
STATUS_IN_READY = 2
class OrdersDto(BaseModel):
    product: str
    user: str
    delivery: str