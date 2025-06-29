# 📚 Student Management System

A GUI-based Python application for managing university student records, built using **Tkinter**. This system enables users to **add**, **search**, **update**, **delete**, and **view** detailed information about students including **courses**, **grades**, **credit hours**, and **CGPA**.

---

## ✨ Features

- 📋 View all students with ID, Name, CMS_ID, Age, and CGPA
- 🔍 Search students by ID or CMS_ID
- ➕ Add new student records with semester-wise course details
- ✏️ Update existing student information
- 🗑️ Delete a student record
- 📖 View enrolled courses with grades and credit hours
- 📤 Save/load data to/from JSON file
- 📊 Automatic CGPA calculation from grades and credit hours
- 🖥️ User-friendly graphical interface using **Tkinter**

---

## 📦 Project Structure


## ⚙️ Technologies Used

- **Python 3.x**
- **Tkinter** (GUI)
- **JSON** (for data storage)
- **Regular Expressions** (for parsing credit hours)
- **Jupyter Notebook** (for development and testing)

---

## 🧠 Core Functionalities

### 🎓 Student Management
- Student details include ID, Name, CMS_ID, Age, and Semester-wise course data.
- Each course contains:
  - Grade (A, B+, C+, etc.)
  - Credit Hours in format `Lecture+Lab` (e.g., 3+1)

### 📈 GPA/CGPA Calculation
- Converts letter grades to numeric GPA.
- Computes GPA per course and overall CGPA.

### 🖼️ Graphical User Interface
- Buttons for each operation
- `Treeview` table to display students
- Multiple popup windows for data entry and search

---

## 🚀 How to Run

1. Make sure Python is installed (`python --version`)
2. Install required modules if needed:
   ```bash
   pip install tk
