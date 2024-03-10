from abc import ABC,abstractmethod

class Event(ABC):
    @abstractmethod
    def cal_total_spent(self):
        pass

    @abstractmethod
    def cal_total_revenue(self):
        pass

    @abstractmethod
    def profit_or_loss(self):
        pass


class Exhibition(Event):
    def __init__(self,no_of_stall,cost_per_stall,no_of_entries,cost_per_entry) -> None:
        super().__init__()
        self.no_of_stall = no_of_stall
        self.cost_per_stall = cost_per_stall
        self.no_of_entries = no_of_entries
        self.cost_per_entry = cost_per_entry

    def cal_total_spent(self):
        return self.no_of_stall * self.cost_per_stall

    def cal_total_revenue(self):
        return self.no_of_entries * self.cost_per_entry
    
    def profit_or_loss(self) -> str:
        if self.cal_total_revenue() > self.cal_total_spent():
            return "Profit"
        elif self.cal_total_revenue() < self.cal_total_spent():
            return "Loss"
        else:
            return "No Loss No Profit"
        
    def display(self):
        print(f"Total Spent: {self.cal_total_spent()} and Total Revenue: {self.cal_total_revenue()}")

if __name__ == "__main__":
    exhibition = Exhibition(10,90,10,100)
    print(exhibition.cal_total_spent())
    print(exhibition.cal_total_revenue())
    print(exhibition.profit_or_loss())
    exhibition.display()