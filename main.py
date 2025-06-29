# %% [markdown]
# STUDENT MANAGEMENT SYSTEM: 

# %% [markdown]
# importing dependencies

# %%
import re
import tkinter as tk
from tkinter import messagebox, ttk
import json

# %% [markdown]
# Sample Student Data (my own course data)

# %%
# I made a list of Students which includes all Students and their info in a Dictionary
# this is my own Sample data which I've used to test functions
student_001 = {
    "id": "S001",
    "name": "Ahmed Sultan",
    "age": 18,
    "CMS_ID": 518505,
    "courses": {
        "Semester 1": {
            'Engineering Drawing' : {'Grade': 'A' , 'Credit_Hours' : '0+2'},
            'Ideology and Constitution of Pakistan' : {'Grade': 'D+' , 'Credit_Hours' : '2+0'},
            'Engineering Statics' : {'Grade': 'B+' , 'Credit_Hours' : '2+0'},
            'Calculus and Analytical Geometry' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Occupational Health and Safety' : {'Grade': 'C+' , 'Credit_Hours' : '1+0'},
            'Functional English' : {'Grade': 'B+' , 'Credit_Hours' : '3+0'},
            'Application of ICT' : {'Grade': 'B+' , 'Credit_Hours' : '2+1'}
        },
        "Semester 2": {
            'Fundamentals of Programming' : {'Grade': 'A' , 'Credit_Hours' : '2+1'},
            'Applied Physics' : {'Grade': 'A' , 'Credit_Hours' : '2+1'},
            'Differential Equations' : {'Grade': 'B+' , 'Credit_Hours' : '3+0'},
            'Islamic Studies' : {'Grade': 'B+' , 'Credit_Hours' : '2+0'},
            'Professional Ethics' : {'Grade': 'B' , 'Credit_Hours' : '2+0'},
            'Electric Circuit Analysis' : {'Grade': 'A' , 'Credit_Hours' : '3+1'},
            'Workshop Practice' : {'Grade': 'B' , 'Credit_Hours' : '0+1'}
        }
    }
}

student_002 = {
    "id": "S002",
    "name": "Muhammad Ibrahim",
    "age": 18,
    "CMS_ID": 508142,
    "courses": {
        "Semester 1": {
            'Engineering Drawing' : {'Grade': 'A' , 'Credit_Hours' : '0+2'},
            'Ideology and Constitution of Pakistan' : {'Grade': 'A' , 'Credit_Hours' : '2+0'},
            'Engineering Statics' : {'Grade': 'A' , 'Credit_Hours' : '2+0'},
            'Calculus and Analytical Geometry' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Occupational Health and Safety' : {'Grade': 'A' , 'Credit_Hours' : '1+0'},
            'Functional English' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Application of ICT' : {'Grade': 'A' , 'Credit_Hours' : '2+1'}
        },
        "Semester 2": {
            'Fundamentals of Programming' : {'Grade': 'A' , 'Credit_Hours' : '2+1'},
            'Applied Physics' : {'Grade': 'A' , 'Credit_Hours' : '2+1'},
            'Differential Equations' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Islamic Studies' : {'Grade': 'A' , 'Credit_Hours' : '2+0'},
            'Professional Ethics' : {'Grade': 'A' , 'Credit_Hours' : '2+0'},
            'Electric Circuit Analysis' : {'Grade': 'A' , 'Credit_Hours' : '3+1'},
            'Workshop Practice' : {'Grade': 'B+' , 'Credit_Hours' : '0+1'}
        }
    }
}

student_003 = {
    "id": "S003",
    "name": "Suleman Qureshi",
    "age": 19,
    "CMS_ID": 531542,
    "courses": {
        "Semester 1": {
            'Engineering Drawing' : {'Grade': 'A' , 'Credit_Hours' : '0+2'},
            'Ideology and Constitution of Pakistan' : {'Grade': 'B+' , 'Credit_Hours' : '2+0'},
            'Engineering Statics' : {'Grade': 'B' , 'Credit_Hours' : '2+0'},
            'Calculus and Analytical Geometry' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Occupational Health and Safety' : {'Grade': 'A' , 'Credit_Hours' : '1+0'},
            'Functional English' : {'Grade': 'C+' , 'Credit_Hours' : '3+0'},
            'Application of ICT' : {'Grade': 'B' , 'Credit_Hours' : '2+1'}
        },
        "Semester 2": {
            'Fundamentals of Programming' : {'Grade': 'D+' , 'Credit_Hours' : '2+1'},
            'Applied Physics' : {'Grade': 'A' , 'Credit_Hours' : '2+1'},
            'Differential Equations' : {'Grade': 'A' , 'Credit_Hours' : '3+0'},
            'Islamic Studies' : {'Grade': 'B' , 'Credit_Hours' : '2+0'},
            'Professional Ethics' : {'Grade': 'A' , 'Credit_Hours' : '2+0'},
            'Electric Circuit Analysis' : {'Grade': 'A' , 'Credit_Hours' : '3+1'},
            'Workshop Practice' : {'Grade': 'B+' , 'Credit_Hours' : '0+1'}
        }
    }
}

def load_students_from_json(filename="students.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# %%
students = load_students_from_json()


# %% [markdown]
# Student Info Displaying Function to Access Details

# %%
def display_student_info(student):
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"CMS_ID: {student['CMS_ID']}\n")
    
    for semester, courses in student['courses'].items():
        print(f"{semester}:")
        for course, info in courses.items():
            print(f"  {course} - Grade: {info['Grade']}, Credit Hours: {info['Credit_Hours']}")
        print()
        
# Test
display_student_info(student_001)


# %% [markdown]
# Function for Credit Hour Details for Every Semester

# %%
def semester_wise_credit_hours(student):
    grand_total_lecture = 0
    grand_total_lab = 0
    
    print(f"Credit Hour Breakdown for {student['name']}:\n")

    for semester, courses in student["courses"].items():
        semester_lecture = 0
        semester_lab = 0
        
        for info in courses.values():
            match = re.match(r"(\d+)\+(\d+)", info["Credit_Hours"])
            if match:
                semester_lecture += int(match.group(1))
                semester_lab += int(match.group(2))
        
        total = semester_lecture + semester_lab
        print(f"{semester}:")
        print(f"  Lecture Hours: {semester_lecture}")
        print(f"  Lab Hours: {semester_lab}")
        print(f"  Total Credit Hours: {total}\n")
        
        grand_total_lecture += semester_lecture
        grand_total_lab += semester_lab
    
    print("Overall Total:")
    print(f"  Lecture Hours: {grand_total_lecture}")
    print(f"  Lab Hours: {grand_total_lab}")
    print(f"  Total Credit Hours: {grand_total_lecture + grand_total_lab}")

# Test
semester_wise_credit_hours(student_001)


# %%
def find_lecture_courses(student):
    print("Courses with lecture hours:\n")
    for semester, courses in student['courses'].items():
        for course, info in courses.items():
            match = re.match(r"(\d+)\+(\d+)", info["Credit_Hours"])
            if match and int(match.group(1)) > 0:
                print(f"{semester} - {course}: {info['Credit_Hours']} (Grade: {info['Grade']})")

# Test
find_lecture_courses(student_001)

# %%
def find_lab_courses(student):
    print("Courses with lab hours:\n")
    for semester, courses in student['courses'].items():
        for course, info in courses.items():
            match = re.match(r"(\d+)\+(\d+)", info["Credit_Hours"])
            if match and int(match.group(2)) > 0:
                print(f"{semester} - {course}: {info['Credit_Hours']} (Grade: {info['Grade']})")

# Test
find_lab_courses(student_001)

# %% [markdown]
# Adding Student Helping Functions

# %%
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def valid_credit_format(ch):
    return re.fullmatch(r"\d+\+\d+", ch)

def find_student_by_id_or_cms(students, sid=None, cms=None):
    for student in students:
        if (sid and student['id'] == sid) or (cms and student['CMS_ID'] == cms):
            return student
    return None


# %%

def save_students_to_json(students, filename="students.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)
    print(f"✅ Students data saved to {filename}")
save_students_to_json(students , filename="students.json")


# %% [markdown]
# Adding Student Function to add more students in list

# %%
def add_student():
    sid = input("Enter student ID: ")
    cms = get_int("Enter CMS ID: ")

    existing = find_student_by_id_or_cms(students, sid=sid, cms=cms)
    
    if existing:
        print(f"\n Student with ID '{sid}' or CMS '{cms}' already exists. Updating their record.\n")
        student = existing
    else:
        student = {"id": sid, "CMS_ID": cms}
        student["name"] = input("Enter student name: ")
        student["age"] = get_int("Enter student age: ")
        student["courses"] = {}
        students.append(student)

    while True:
        semester_name = input("Enter semester name (e.g., Semester 1): ")
        if semester_name not in student["courses"]:
            student["courses"][semester_name] = {}

        while True:
            course_name = input(f"  Enter course name for {semester_name}: ")

            if course_name in student["courses"][semester_name]:
                choice = input(f"⚠️ Course '{course_name}' already exists in {semester_name}. Overwrite? (y/n): ").lower()
                if choice != 'y':
                    print("⏩ Skipping this course.\n")
                    continue

            grade = input(f"    Enter grade for {course_name}: ")

            while True:
                credit_hours = input(f"    Enter credit hours (e.g., 2+1): ")
                if valid_credit_format(credit_hours):
                    break
                else:
                    print("❌ Invalid format. Use format L+L, like 3+0 or 2+1.")

            student["courses"][semester_name][course_name] = {
                "Grade": grade,
                "Credit_Hours": credit_hours
            }

            more_courses = input(f"  Add another course to {semester_name}? (y/n): ").lower()
            if more_courses != 'y':
                break

        more_semesters = input("Add another semester? (y/n): ").lower()
        if more_semesters != 'y':
            break

    print(f"\n✅ Student '{student['name']}' added/updated successfully!\n")
    save_students_to_json(students , filename="students.json")

# %%
def grade_to_num(grade):
    """
    Converts a letter grade (e.g., 'B+') into its numeric GPA equivalent.
    """
    grade = grade.strip().upper()

    mapping = {
        'A': 4.0,
        'B+': 3.5,
        'B': 3.0,
        'C+': 2.5,
        'C': 2.0,
        'D+': 1.5,
        'D': 1.0,
        'F': 0.0
    }

    if grade in mapping:
        return mapping[grade]
    else:
        raise ValueError(f"❌ Invalid grade: '{grade}'")


# %%
def calculate_total_grade_points(student):
    """
    Calculates the total grade points for a student across all semesters.
    Grade Points = Sum of (Credit Hours x GPA) for each course.
    """
    total_grade_points = 0
    total_credit_hours = 0

    for semester, courses in student["courses"].items():
        for course, info in courses.items():
            credit_match = re.match(r"(\d+)\+(\d+)", info["Credit_Hours"])
            if credit_match:
                lecture = int(credit_match.group(1))
                lab = int(credit_match.group(2))
                ch = lecture + lab
                try:
                    gpa = grade_to_num(info["Grade"])
                    total_grade_points += ch * gpa
                    total_credit_hours += ch
                except ValueError as e:
                    print(f"⚠️ Skipping course '{course}' due to invalid grade: {info['Grade']}")
            else:
                print(f"⚠️ Invalid credit format for course: {course}")
    
    return float(total_grade_points), float(total_credit_hours)


# %%
def CGPA(Student):
    (grade, CH) = calculate_total_grade_points(Student)
    C_GPA = grade / CH if CH != 0 else 0.0
    return round(C_GPA, 2)


# %%
def display_all_students(students):
    print("📋 All Students:")
    for s in students:
        print(f"- {s['id']}: {s['name']} (CMS: {s['CMS_ID']})")

display_all_students(students)


# %% [markdown]
# GUI USING TKINTER

# %% [markdown]
# View all students and search for student details

# %%
def view_all_students():
    tree.delete(*tree.get_children())
    for student in students:
        try:
            cgpa = CGPA(student)
        except:
            cgpa = "N/A"
        tree.insert('', 'end', values=(
            student["id"],
            student["name"],
            student["CMS_ID"],
            student.get("age", "N/A"),
            cgpa
        ))


def search_student_gui():
    def search():
        sid = id_entry.get().strip()
        cms_input = cms_entry.get().strip()
        cms = int(cms_input) if cms_input.isdigit() else None

        student = find_student_by_id_or_cms(students, sid if sid else None, cms)

        if student:
            result = f"\nID: {student['id']}\nName: {student['name']}\nCMS_ID: {student['CMS_ID']}\nAge: {student.get('age', 'N/A')}\nCGPA: {CGPA(student)}"
            messagebox.showinfo("Student Found", result)
        else:
            messagebox.showerror("Not Found", "Student not found.")

    win = tk.Toplevel(root)
    win.title("Search Student")
    win.geometry("300x200")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Student ID:", bg="#f0f4f7").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)

    tk.Label(win, text="CMS ID:", bg="#f0f4f7").pack(pady=5)
    cms_entry = tk.Entry(win)
    cms_entry.pack(pady=5)

    tk.Button(win, text="Search", command=search).pack(pady=10)


# %% [markdown]
# Adding student data function

# %%
def add_student_gui():
    def submit():
        sid = id_entry.get()
        name = name_entry.get()
        cms_input = cms_entry.get()
        age_input = age_entry.get()

        if not sid or not name or not cms_input.isdigit() or not age_input.isdigit():
            messagebox.showerror("Invalid Input", "Please enter all fields correctly.")
            return

        cms = int(cms_input)
        age = int(age_input)

        existing = find_student_by_id_or_cms(students, sid=sid, cms=cms)

        if existing:
            messagebox.showwarning("Exists", f"Student with ID {sid} or CMS {cms} already exists. Updating record.")
            student = existing
        else:
            student = {"id": sid, "name": name, "CMS_ID": cms, "age": age, "courses": {}}
            students.append(student)

        save_students_to_json(students)
        view_all_students()
        messagebox.showinfo("Success", "Student added or updated successfully.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Add Student")
    win.geometry("300x350")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="ID:", bg="#f0f4f7").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)

    tk.Label(win, text="Name:", bg="#f0f4f7").pack(pady=5)
    name_entry = tk.Entry(win)
    name_entry.pack(pady=5)

    tk.Label(win, text="CMS ID:", bg="#f0f4f7").pack(pady=5)
    cms_entry = tk.Entry(win)
    cms_entry.pack(pady=5)

    tk.Label(win, text="Age:", bg="#f0f4f7").pack(pady=5)
    age_entry = tk.Entry(win)
    age_entry.pack(pady=5)

    tk.Button(win, text="Submit", command=submit).pack(pady=10)

# %% [markdown]
# Add Courses for New Students

# %%
def add_courses_gui():
    def load_student():
        nonlocal student
        sid = sid_entry.get().strip()
        student = find_student_by_id_or_cms(students, sid=sid)

        if not student:
            messagebox.showerror("Not Found", "Student not found.")
            return
        student_info_label.config(text=f"Editing Courses for {student['name']}")

    def add_course():
        semester = semester_entry.get().strip()
        course = course_entry.get().strip()
        grade = grade_entry.get().strip()
        ch = credit_entry.get().strip()

        if not semester or not course or not grade or not valid_credit_format(ch):
            messagebox.showerror("Invalid Input", "Please fill all fields correctly.\nCredit Hours format: L+L (e.g., 2+1)")
            return

        if semester not in student["courses"]:
            student["courses"][semester] = {}

        student["courses"][semester][course] = {
            "Grade": grade,
            "Credit_Hours": ch
        }

        messagebox.showinfo("Added", f"Course '{course}' added to {semester}.")
        save_students_to_json(students)

        # Clear input fields
        course_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        credit_entry.delete(0, tk.END)

    student = None
    win = tk.Toplevel(root)
    win.title("Add Courses to Student")
    win.geometry("400x450")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Student ID:", bg="#f0f4f7").pack(pady=5)
    sid_entry = tk.Entry(win)
    sid_entry.pack(pady=5)
    tk.Button(win, text="Load Student", command=load_student).pack(pady=5)

    student_info_label = tk.Label(win, text="", bg="#f0f4f7", fg="blue")
    student_info_label.pack(pady=5)

    tk.Label(win, text="Semester Name:", bg="#f0f4f7").pack(pady=5)
    semester_entry = tk.Entry(win)
    semester_entry.pack(pady=5)

    tk.Label(win, text="Course Name:", bg="#f0f4f7").pack(pady=5)
    course_entry = tk.Entry(win)
    course_entry.pack(pady=5)

    tk.Label(win, text="Grade (A, B+, etc):", bg="#f0f4f7").pack(pady=5)
    grade_entry = tk.Entry(win)
    grade_entry.pack(pady=5)

    tk.Label(win, text="Credit Hours (e.g., 3+0):", bg="#f0f4f7").pack(pady=5)
    credit_entry = tk.Entry(win)
    credit_entry.pack(pady=5)

    tk.Button(win, text="➕ Add Course", command=add_course).pack(pady=10)

# %% [markdown]
# Save All new Entries

# %%
def save_all_data_gui():
    save_students_to_json(students)
    messagebox.showinfo("Saved", "✅ All student data has been saved to students.json.")

# %% [markdown]
# setting up GUI for Student management system

# %%
# --- Main Window ---

root = tk.Tk()
root.title("Student Management System")
root.geometry("900x600")
root.configure(bg="#f0f4f7")

title_label = tk.Label(root, text="📚 Student Management System", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Buttons
button_frame = tk.Frame(frame, bg="#ffffff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="📋 View All Students", width=20, command=view_all_students).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="🔍 Search Student", width=20, command=search_student_gui).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="➕ Add Student", width=20, command=add_student_gui).grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="❌ Exit", width=20, command=root.destroy).grid(row=0, column=3, padx=10)
tk.Button(button_frame, text="➕ Add Courses", width=20, command=add_courses_gui).grid(row=1, column=3, padx=10, pady=5)
tk.Button(button_frame, text="💾 Save All Data", width=20, command=save_all_data_gui).grid(row=2, column=0, padx=10, pady=5)

# Treeview
columns = ("ID", "Name", "CMS_ID", "Age", "CGPA")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(fill="both", expand=True, padx=20)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

# %% [markdown]
# Update Existing Student through GUI 

# %%
def update_student_gui():
    def update():
        sid = id_entry.get()
        student = find_student_by_id_or_cms(students, sid=sid)

        if not student:
            messagebox.showerror("Not Found", f"Student ID '{sid}' not found.")
            return

        name = name_entry.get()
        cms_input = cms_entry.get()
        age_input = age_entry.get()

        if not name or not cms_input.isdigit() or not age_input.isdigit():
            messagebox.showerror("Invalid Input", "Please enter all fields correctly.")
            return

        student["name"] = name
        student["CMS_ID"] = int(cms_input)
        student["age"] = int(age_input)

        save_students_to_json(students)
        view_all_students()
        messagebox.showinfo("Updated", f"Student '{sid}' updated successfully.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Update Student")
    win.geometry("300x350")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Student ID to Update:", bg="#f0f4f7").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)

    tk.Label(win, text="New Name:", bg="#f0f4f7").pack(pady=5)
    name_entry = tk.Entry(win)
    name_entry.pack(pady=5)

    tk.Label(win, text="New CMS ID:", bg="#f0f4f7").pack(pady=5)
    cms_entry = tk.Entry(win)
    cms_entry.pack(pady=5)

    tk.Label(win, text="New Age:", bg="#f0f4f7").pack(pady=5)
    age_entry = tk.Entry(win)
    age_entry.pack(pady=5)

    tk.Button(win, text="Update", command=update).pack(pady=10)

# %% [markdown]
# DELETE STUDENT THROUGH GUI

# %%
def delete_student_gui():
    def delete():
        sid = id_entry.get().strip()
        student = find_student_by_id_or_cms(students, sid=sid)

        if student:
            confirm = messagebox.askyesno("Confirm", f"Delete student {student['name']}?")
            if confirm:
                students.remove(student)
                save_students_to_json(students)
                view_all_students()
                messagebox.showinfo("Deleted", "Student deleted successfully.")
                win.destroy()
        else:
            messagebox.showerror("Not Found", "Student not found.")

    win = tk.Toplevel(root)
    win.title("Delete Student")
    win.geometry("250x150")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Enter Student ID:", bg="#f0f4f7").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)
    tk.Button(win, text="Delete", command=delete).pack(pady=10)

def view_courses_gui():
    def show():
        sid = id_entry.get().strip()
        student = find_student_by_id_or_cms(students, sid=sid)

        if not student:
            messagebox.showerror("Not Found", "Student not found.")
            return

        result = f"Courses for {student['name']}\n\n"
        for sem, courses in student["courses"].items():
            result += f"{sem}:\n"
            for cname, info in courses.items():
                result += f"  {cname} - Grade: {info['Grade']}, Credit Hours: {info['Credit_Hours']}\n"
            result += "\n"

        messagebox.showinfo("Course Info", result)

    win = tk.Toplevel(root)
    win.title("View Course Details")
    win.geometry("300x150")
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Enter Student ID:", bg="#f0f4f7").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)
    tk.Button(win, text="Show Courses", command=show).pack(pady=10)

# Add buttons for new features to your existing button_frame:
tk.Button(button_frame, text="✏️ Update Student", width=20, command=update_student_gui).grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text="🗑️ Delete Student", width=20, command=delete_student_gui).grid(row=1, column=1, padx=10, pady=5)
tk.Button(button_frame, text="📖 View Courses", width=20, command=view_courses_gui).grid(row=1, column=2, padx=10, pady=5)

# %% [markdown]
# RUN the GUI

# %%
root.mainloop()


