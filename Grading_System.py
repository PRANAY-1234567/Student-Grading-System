class Student:
    def __init__(self):
        self.name = ""
        self.roll = 0

    def set_data(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Student name     : {self.name}")
        print(f"Roll number      : {self.roll}")


class Exam(Student):
    def __init__(self):
        super().__init__()
        self.marks = []

    def set_data(self, name, roll, marks):
        # Calling the parent (Student) version of set_data
        super().set_data(name, roll)
        self.marks = marks

    def display(self):
        # Calling the parent (Student) version of display
        super().display()
        for i, mark in enumerate(self.marks):
            print(f"Subject {i + 1}        : {mark}")


class Result(Exam):
    def __init__(self):
        super().__init__()
        self.total_marks = 0
        self.percent = 0.0

    def process(self):
        self.total_marks = sum(self.marks)
        # Using 6.0 to ensure float division as per your Java logic
        self.percent = self.total_marks / 6.0

    def display(self):
        # Calling the parent (Exam) version of display
        super().display()
        print(f"Total marks      : {self.total_marks}")
        print(f"Percentage       : {self.percent:.2f}")


# Main execution block (Equivalent to your Inh5 class)
if __name__ == "__main__":
    r = Result()
    name = "Ankush Tadke"
    roll = 64
    marks = [92, 87, 74, 84, 99, 85]
    
    r.set_data(name, roll, marks)
    r.process()
    r.display()