# Requisition System

This project is a Python prototype of a requisition management system.  
It demonstrates how **software design principles** can be applied to create structured, reusable, and maintainable code.

---

## 📌 Features
- Create requisitions using a constructor.
- Store requisitions in a class-level list.
- Display all requisitions.
- Manager can approve or reject requisitions.
- Generate statistics on requisitions (Approved, Rejected, Pending).

---

## ⚙️ Software Design Principles Applied

### 1. Encapsulation
- Data (`employee_name`, `item`, `quantity`, etc.) and related behaviors (methods) are wrapped inside the `RequisitionSystem` class.
- This hides the internal representation and provides a clean interface.

### 2. Information Expert
- The `RequisitionSystem` class stores requisition data and is responsible for displaying and processing it.
- Responsibility is given to the object that has the necessary information.

### 3. High Cohesion
- Each method has a **single, focused responsibility** (e.g., `display_requisition()` only displays data, `show_statistics()` only calculates stats).
- This makes the system easier to understand and maintain.

### 4. Low Coupling
- Objects manage their own state and add themselves to the global requisition list.
- External code does not need to handle the internal structure, reducing dependencies.

### 5. Abstraction
- The `add_manager_response()` method allows users to set responses without knowing the internal storage details.
- Users interact with simple, meaningful operations.

### 6. Separation of Concerns
- The system separates **core data storage**, **managerial response handling**, and **statistics reporting** into distinct methods.
- This improves modularity and reduces complexity.

### 7. Reusability
- The class can be reused for future extensions, such as:
  - Saving requisitions to a database.
  - Adding a user interface.
  - Expanding managerial response options.

---

## 🚀 How to Run
1. Save the file as `requisitionsystem.py`.
2. Run in terminal:
   ```bash
   python requisitionsystem.py
