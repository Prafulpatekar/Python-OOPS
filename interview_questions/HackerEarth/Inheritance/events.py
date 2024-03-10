from collections.abc import Iterable


class Event:
    def __init__(self, name,address,start_data,start_time):
        self.name = name
        self.address = address
        self.start_data = start_data
        self.start_time = start_time

class Exhibition(Event):
    def __init__(self,name,address,start_data,start_time,event_type,end_date):
        super().__init__(name,address,start_data,start_time)
        self.__event_type = event_type
        self.__end_date = end_date

    def display(self):
        print(f"Exhibition {self.name} is of type {self.__event_type} and ends on {self.__end_date}")

        

if __name__ == '__main__':
    exhibition = Exhibition("My Event", "Bangalore", "2020-01-01", "10:00:00", "Exhibition", "2020-01-01")
    exhibition.display()