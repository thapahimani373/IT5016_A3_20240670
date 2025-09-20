# Employee Leave Management System
* Overview

The Employee Leave Management System is a Python-based console application designed to make managing employee leave requests simple and efficient. Employees can submit leave applications, and the system processes approvals either automatically or through manager review, following company rules. The project is built with key software design principles in mind, ensuring that the code is modular, easy to maintain, and scalable for future improvements.

* Workflow

The workflow in this system is straightforward and easy to follow. Employees start by submitting a leave application, providing their employee ID, name, number of leave days, and the reason for leave. The system evaluates each application automatically: if the leave is less than three days, it is approved immediately. For longer leaves, the application is marked as pending and reviewed by a manager, who can approve or reject it. All leave requests are stored in a central list, making it easy to view them in full detail or as a summary. The system also generates statistics showing the total number of applications, as well as how many were approved, pending, or rejected. This workflow ensures a clear, organized, and efficient leave management process.

* Features

This system allows employees to submit leave requests quickly and efficiently. Short leaves of less than three days are automatically approved, while longer requests are sent for manager review. Every application is stored in a central list and can be displayed either in full detail or as a concise summary. The system calculates and presents statistics, including the total number of applications and the breakdown of approved, pending, and rejected requests. Each leave request receives a unique ID for easy tracking, and the program is designed to be flexible, allowing future updates for additional rules or new features.

* Software Design Principles Applied

The Employee Leave Management System is built using several software design principles to ensure clean, maintainable, and reliable code:

Single Responsibility Principle (SRP): Each method performs only one task, such as collecting employee details, processing leave, reviewing manager decisions, displaying applications, or calculating statistics.

* KISS (Keep It Simple, Stupid): The logic is simple and clear, using straightforward conditions for automatic approval and yes/no manager inputs.

* Encapsulation: Employee and leave information is stored safely inside the LeaveApplication class and accessed only through class methods.

* High Cohesion: All leave-related attributes and behaviors are grouped within the LeaveApplication class.

* Low Coupling: The main program manages workflow without directly interfering with the internal data of each leave application.

* Information Expert: The LeaveApplication class contains all the necessary information to process leave requests efficiently.

* Separation of Concerns: Input handling, decision-making, display, and statistics calculation are all managed in separate methods for clarity and maintainability.

* Flexibility and Extensibility: Features like summary/full display and dynamic statistics make it easy to adapt the system for new requirements or additional functionality in the future.

## How the Code Works

When a new leave request is submitted, the system creates a LeaveApplication object and automatically assigns it a unique application ID. The program collects the employee’s details, including ID, name, number of leave days, and reason for leave. It then evaluates the request: leave under three days is automatically approved, while longer requests are marked as pending. Pending applications are reviewed by a manager, who can approve or reject them. All applications are stored in a central list, which allows the program to display either full details or a summary of each request. At the end, the system calculates and displays statistics, showing the total number of leave requests and how many were approved, pending, or rejected. Each function is designed with a clear responsibility, keeping the code organized, maintainable, and easy to understand.
