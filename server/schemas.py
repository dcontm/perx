class Item:
    def __init__(self,
                 quantity,
                 delta,
                 start_value,
                 current_value,
                 interval,
                 number=None,
                 status='in the queue',
                 start_date='В очереди'):
        self.quantity = quantity
        self.delta = delta
        self.start_value = start_value
        self.current_value = current_value
        self.interval = interval
        self.number = number
        self.status = status
        self.start_date = start_date


''''
class Item(BaseModel):
    position: int = None
    quantity: int
    delta: float
    start_value: float
    current_value: float
    interval: float
    status: str = 'in the queue'
    start_date: str = '01.01'

    class Config:
        orm_mode = True

    @validator('quantity', 'delta', 'start_value', 'interval')
    def validation_quantity(cls, v):
        for i in v:
            if i < 1:
                raise ValueError('Все значения должны быть больше 0')
        return v
'''
