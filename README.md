This README provides an overview of the Student Grading System, a simple Python application that demonstrates the concept of Multilevel Inheritance.

📌 Project Overview
This project simulates a basic academic record system. It captures student identity, exam scores, and calculates the final result. The logic is spread across three hierarchical classes to ensure a clean separation of concerns:

Student (Base Class): Handles basic identity like Name and Roll Number.

Exam (Derived from Student): Manages a list of marks for different subjects.

Result (Derived from Exam): Processes the total marks and calculates the percentage.

🏗️ Architecture: Multilevel Inheritance
The program follows a linear inheritance chain. This allows the Result class to access properties and methods from both Exam and Student.

🚀 How to Run
Prerequisites: Ensure you have Python 3.x installed.

Execution: Save the code in a file named student_result.py and run it via the terminal:

Bash
python student_result.py
💻 Code Structure
1. Class Student
Attributes: name, roll

Methods: * set_data(name, roll): Assigns basic info.

display(): Prints student identification.

2. Class Exam
Attributes: Inherits from Student, adds marks (list).

Methods: * set_data(name, roll, marks): Uses super() to set student info and then stores marks.

display(): Prints marks for each subject.

3. Class Result
Attributes: Inherits from Exam, adds total_marks and percent.

Methods: * process(): Calculates the sum of marks and the percentage based on 6 subjects.

display(): Combines data from all parent classes to show the final report card.

📊 Sample Output
When executed, the program generates a formatted report:

Plaintext
Student name     : Ankush Tadke
Roll number      : 64
Subject 1        : 92
Subject 2        : 87
...
Total marks      : 521
Percentage       : 86.83
🛠️ Key Python Features Used
Inheritance: Using class Child(Parent) to pass down functionality.

super() Function: Used to call parent methods, avoiding code duplication.

F-Strings: For clean, formatted string output and decimal precision.

__main__ Guard: Ensures the script runs only when executed directly.

<img width="741" height="848" alt="image" src="https://github.com/user-attachments/assets/03ba67ba-5248-4094-9842-af1de119f739" />
