class Item:
    def __init__(self,
                 quantity,
                 delta,
                 start_value,
                 current_value,
                 interval,
                 number=None,
                 status='в очереди',
                 start_date='в очереди'):
        self.quantity = quantity
        self.delta = delta
        self.start_value = start_value
        self.current_value = current_value
        self.interval = interval
        self.number = number
        self.status = status
        self.start_date = start_date
