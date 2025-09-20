###How the System Works

In the Employee Leave Management System, the workflow begins when an employee submits a leave application by entering their employee ID, name, number of leave days, and the reason for the leave. Once the application is submitted, the system automatically evaluates it: if the requested leave is less than three days, it is automatically approved; otherwise, the application status is set to pending. Pending applications are then reviewed by a manager, who can either approve or reject the leave. After the manager's decision, the system updates the status of the application accordingly. All leave applications, along with their details such as employee information, leave days, reason, and status, can be displayed either in full detail or as a summary. Finally, the system generates overall statistics, showing the total number of applications and a breakdown of approved, pending, and rejected requests. This structured workflow ensures that the leave approval process is clear, efficient, and easy to track.

##Software Design Principles Applied##

The Employee Leave Management System follows several important software design principles to make the code clean, easy to maintain, and scalable:

Single Responsibility Principle (SRP): Each method does only one specific task, such as collecting employee details, applying for leave, checking automatic approval, handling manager review, displaying application details, or calculating statistics.

KISS (Keep It Simple, Stupid): The logic is simple and straightforward, with easy-to-understand conditions for automatic approval and yes/no input for manager decisions.

Encapsulation: Employee and leave information is safely stored inside the LeaveApplication class and accessed only through class methods.

High Cohesion: All attributes and behaviors related to leave management are grouped together in the LeaveApplication class.

Low Coupling: The main program controls the workflow without directly modifying the internal data of the leave applications.

Information Expert: The LeaveApplication class holds all the data needed to process leave requests efficiently.

Separation of Concerns: Input handling, decision logic, display, and statistics calculation are separated into dedicated methods and functions.

Flexibility and Extensibility: Features like summary/full display and dynamic statistics make it easy to adapt the system for future requirements.
