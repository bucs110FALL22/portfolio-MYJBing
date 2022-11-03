import time

class Animal:
    def __init__(self, name: str, type: str):
        '''
        constructor
        name: (str) Name of the animal
        type: (str): Type of the animal.'dog' or 'cat'
        '''
        self.name = name
        self.type = type
        self.id = id(name)
        self.arrived_date = time.strftime("%d/%m/%Y")
        self.adopted_date = ''
