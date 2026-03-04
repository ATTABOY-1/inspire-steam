# ============================================
#SCHOOL MANAGEMENT SYSTEM 
# Developer: Alvin Njuguna
# ============================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from openpyxl import Workbook
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced School Management System")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        self.dark_mode = False
        self.students = []

        self.setup_ui()

    # ================= UI SETUP =================
    def setup_ui(self):
        self.root.configure(bg="#f0f2f5")

        # Sidebar
        self.sidebar = tk.Frame(self.root, width=220, bg="#1f4e79")
        self.sidebar.pack(side="left", fill="y")

        self.content = tk.Frame(self.root, bg="#f0f2f5")
        self.content.pack(side="right", fill="both", expand=True)

        title = tk.Label(self.sidebar,
                         text="SMS PRO",
                         bg="#1f4e79",
                         fg="white",
                         font=("Segoe UI", 18, "bold"))
        title.pack(pady=30)

        self.create_sidebar_button("Dashboard", self.show_dashboard)
        self.create_sidebar_button("Register Student", self.show_register)
        self.create_sidebar_button("View Students", self.show_students)
        self.create_sidebar_button("Toggle Dark Mode", self.toggle_theme)

        self.show_dashboard()

    def create_sidebar_button(self, text, command):
        btn = tk.Button(self.sidebar,
                        text=text,
                        command=command,
                        bg="#1f4e79",
                        fg="white",
                        font=("Segoe UI", 11),
                        bd=0,
                        pady=12,
                        cursor="hand2",
                        activebackground="#163a5f")
        btn.pack(fill="x")

    # ================= DASHBOARD =================
    def show_dashboard(self):
        self.clear_content()

        title = tk.Label(self.content,
                         text="Dashboard Overview",
                         font=("Segoe UI", 20, "bold"),
                         bg=self.content["bg"])
        title.pack(pady=20)

        total = len(self.students)

        stats = tk.Label(self.content,
                         text=f"Total Registered Students: {total}",
                         font=("Segoe UI", 14),
                         bg=self.content["bg"])
        stats.pack(pady=10)

        if total > 0:
            courses = {}
            for s in self.students:
                courses[s["course"]] = courses.get(s["course"], 0) + 1

            fig, ax = plt.subplots(figsize=(5, 4))
            ax.bar(courses.keys(), courses.values())
            ax.set_title("Students Per Course")

            canvas = FigureCanvasTkAgg(fig, master=self.content)
            canvas.draw()
            canvas.get_tk_widget().pack()

    # ================= REGISTER =================
    def show_register(self):
        self.clear_content()

        frame = tk.Frame(self.content, bg=self.content["bg"])
        frame.pack(pady=20)

        fields = ["ID", "First Name", "Last Name", "Course", "Phone"]
        self.entries = {}

        for i, field in enumerate(fields):
            tk.Label(frame,
                     text=field,
                     font=("Segoe UI", 11),
                     bg=self.content["bg"]).grid(row=i, column=0, pady=10, sticky="w")

            entry = tk.Entry(frame, font=("Segoe UI", 11), width=30)
            entry.grid(row=i, column=1, pady=10)

            key = field.lower().replace(" ", "_")  # FIXED KEY FORMAT
            self.entries[key] = entry

        tk.Button(frame,
                  text="Register Student",
                  bg="#28a745",
                  fg="white",
                  font=("Segoe UI", 11, "bold"),
                  command=self.add_student).grid(row=6, columnspan=2, pady=20)

    def add_student(self):
        data = {k: v.get() for k, v in self.entries.items()}

        if not all(data.values()):
            messagebox.showwarning("Error", "All fields required")
            return

        self.students.append(data)
        messagebox.showinfo("Success", "Student Registered Successfully")
        self.show_dashboard()

    # ================= VIEW STUDENTS =================
    def show_students(self):
        self.clear_content()

        frame = tk.Frame(self.content)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        columns = ("ID", "First Name", "Last Name", "Course", "Phone")

        tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for s in self.students:
            tree.insert("", "end",
                        values=(s["id"],
                                s["first_name"],
                                s["last_name"],
                                s["course"],
                                s["phone"]))

        tree.pack(fill="both", expand=True)

        tk.Button(self.content,
                  text="Export to Excel",
                  bg="#007bff",
                  fg="white",
                  font=("Segoe UI", 11, "bold"),
                  command=self.export_excel).pack(pady=10)

    # ================= EXPORT =================
    def export_excel(self):
        if not self.students:
            messagebox.showwarning("Error", "No students to export")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")

        if file_path:
            wb = Workbook()
            ws = wb.active
            ws.append(["ID", "First Name", "Last Name", "Course", "Phone"])

            for s in self.students:
                ws.append([s["id"],
                           s["first_name"],
                           s["last_name"],
                           s["course"],
                           s["phone"]])

            wb.save(file_path)
            messagebox.showinfo("Success", "Data Exported Successfully")

    # ================= THEME =================
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.root.configure(bg="#1e1e1e")
            self.content.configure(bg="#2d2d2d")
        else:
            self.root.configure(bg="#f0f2f5")
            self.content.configure(bg="#f0f2f5")

    # ================= UTIL =================
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()