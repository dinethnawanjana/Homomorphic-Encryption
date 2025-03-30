import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar
import time

class OperationsPage(tk.Frame):
    def __init__(self, master, numeric_encryption, text_encryption):
        super().__init__(master)
        self.master = master
        self.numeric_encryption = numeric_encryption
        self.text_encryption = text_encryption

        # Operation state
        self.first_encrypted = None
        self.second_encrypted = None
        self.operation_mode = StringVar(value='Homomorphic Add')
        self.operation_result = None  # Initialize operation result storage

        # Callback for dashboard tracking
        self.on_operation_complete = None

        # Create page layout
        self.create_operations_page()

    def create_operations_page(self):
        # Title
        title_label = ttk.Label(
            self,
            text="Homomorphic Operations",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)

        # Operation Mode Selection
        mode_frame = ttk.Frame(self)
        mode_frame.pack(pady=10)

        ttk.Label(mode_frame, text="Operation Mode:").pack(side='left', padx=10)

        mode_options = ['Homomorphic Add', 'Homomorphic Multiply']
        mode_dropdown = ttk.Combobox(
            mode_frame,
            textvariable=self.operation_mode,
            values=mode_options,
            state='readonly',
            width=20
        )
        mode_dropdown.pack(side='left')

        # First Encrypted Message Frame
        first_frame = ttk.LabelFrame(self, text="First Encrypted Message")
        first_frame.pack(pady=10, padx=20, fill='x')

        self.first_message_text = tk.Text(first_frame, height=3, width=70)
        self.first_message_text.pack(pady=10)

        # Second Encrypted Message Frame
        second_frame = ttk.LabelFrame(self, text="Second Encrypted Message")
        second_frame.pack(pady=10, padx=20, fill='x')

        self.second_message_text = tk.Text(second_frame, height=3, width=70)
        self.second_message_text.pack(pady=10)

        # Operation Buttons Frame
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(pady=10)

        load_first_btn = ttk.Button(
            buttons_frame,
            text="Load First Message",
            command=self.load_first_message
        )
        load_first_btn.pack(side='left', padx=10)

        load_second_btn = ttk.Button(
            buttons_frame,
            text="Load Second Message",
            command=self.load_second_message
        )
        load_second_btn.pack(side='left', padx=10)

        # Perform Operation Button
        perform_btn = ttk.Button(
            self,
            text="Perform Homomorphic Operation",
            command=self.perform_operation
        )
        perform_btn.pack(pady=20)

        # Result Display
        result_frame = ttk.LabelFrame(self, text="Operation Result")
        result_frame.pack(pady=10, padx=20, fill='x')

        self.result_text = tk.Text(result_frame, height=5, width=70)
        self.result_text.pack(pady=10)

    def load_first_message(self):
        # Find the parent HomomorphicEncryptionApp
        app = self.winfo_toplevel().app  # Assumes app is set on the top-level window

        if hasattr(app, 'encryption_page'):
            first_encrypted = app.encryption_page.get_encrypted_data()

            if first_encrypted:
                self.first_encrypted = first_encrypted
                self.first_message_text.delete(1.0, tk.END)
                self.first_message_text.insert(tk.END, str(first_encrypted))
            else:
                messagebox.showerror("Error", "No encrypted message available")
        else:
            messagebox.showerror("Error", "Cannot find encryption page")

    def load_second_message(self):
        # Find the parent HomomorphicEncryptionApp
        app = self.winfo_toplevel().app  # Assumes app is set on the top-level window

        if hasattr(app, 'encryption_page'):
            second_encrypted = app.encryption_page.get_encrypted_data()

            if second_encrypted:
                self.second_encrypted = second_encrypted
                self.second_message_text.delete(1.0, tk.END)
                self.second_message_text.insert(tk.END, str(second_encrypted))
            else:
                messagebox.showerror("Error", "No encrypted message available")
        else:
            messagebox.showerror("Error", "Cannot find encryption page")

    def perform_operation(self):
        try:
            start_time = time.time()
            if not self.first_encrypted or not self.second_encrypted:
                messagebox.showerror(
                    "Error",
                    "Please load both encrypted messages first"
                )
                return False

            operation = self.operation_mode.get()
            operation_type = 'Add' if 'Add' in operation else 'Multiply'

            if operation_type == 'Add':
                result = self.numeric_encryption.homomorphic_add(
                    self.first_encrypted,
                    self.second_encrypted
                )
            else:
                result = self.numeric_encryption.homomorphic_multiply(
                    self.first_encrypted,
                    self.second_encrypted
                )

            # Display result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Operation Result: {result}")

            # Store the result for later use
            self.operation_result = result

            # Notify dashboard if callback is set
            if self.on_operation_complete:
                end_time = time.time()
                self.on_operation_complete(operation_type, end_time - start_time)

            messagebox.showinfo("Success", f"Homomorphic {operation_type} Operation Complete")
            return True

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return False

    def get_operation_result(self):
        """Get the last operation result"""
        return self.operation_result