import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar, BooleanVar
import time

class EncryptionPage(tk.Frame):
    def __init__(self, master, numeric_encryption, text_encryption):
        super().__init__(master)
        self.numeric_encryption = numeric_encryption
        self.text_encryption = text_encryption

        # Encryption state
        self.encrypted_data = None
        self.encryption_mode = StringVar(value='Numeric')
        self.use_text_mode = BooleanVar(value=False)

        # Callback for dashboard tracking
        self.on_encryption_complete = None

        # Create page layout
        self.create_encryption_page()

    def create_encryption_page(self):
        # Title
        title_label = ttk.Label(
            self,
            text="Encryption Setup",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)

        # Encryption Mode Selection
        mode_frame = ttk.Frame(self)
        mode_frame.pack(pady=10)

        ttk.Label(mode_frame, text="Encryption Mode:").pack(side='left', padx=10)

        mode_options = ['Numeric', 'Text']
        mode_dropdown = ttk.Combobox(
            mode_frame,
            textvariable=self.encryption_mode,
            values=mode_options,
            state='readonly',
            width=15
        )
        mode_dropdown.pack(side='left')

        # Input Frame
        input_frame = ttk.LabelFrame(self, text="Encryption Input")
        input_frame.pack(pady=10, padx=20, fill='x')

        # Message Input
        ttk.Label(input_frame, text="Message to Encrypt:").pack(pady=5)
        self.message_entry = ttk.Entry(input_frame, width=50)
        self.message_entry.pack(pady=5)

        # Advanced Options
        advanced_frame = ttk.LabelFrame(self, text="Advanced Options")
        advanced_frame.pack(pady=10, padx=20, fill='x')

        # Prime and Generator inputs
        ttk.Label(advanced_frame, text="Prime Number (p):").pack()
        self.prime_entry = ttk.Entry(advanced_frame, width=20)
        self.prime_entry.insert(0, "17")
        self.prime_entry.pack()

        ttk.Label(advanced_frame, text="Generator (g):").pack()
        self.generator_entry = ttk.Entry(advanced_frame, width=20)
        self.generator_entry.insert(0, "3")
        self.generator_entry.pack()

        # Encrypt Button
        encrypt_button = ttk.Button(
            self,
            text="Encrypt Message",
            command=self.encrypt_message
        )
        encrypt_button.pack(pady=20)

        # Result Display
        result_frame = ttk.LabelFrame(self, text="Encryption Result")
        result_frame.pack(pady=10, padx=20, fill='x')

        self.result_text = tk.Text(result_frame, height=5, width=70)
        self.result_text.pack(pady=10)

    def encrypt_message(self):
        try:
            start_time = time.time()
            message = self.message_entry.get()
            mode = self.encryption_mode.get()

            if not message:
                messagebox.showerror("Error", "Please enter a message")
                return

            # Update encryption parameters
            p = int(self.prime_entry.get())
            g = int(self.generator_entry.get())
            self.numeric_encryption = self.numeric_encryption.__class__(p, g)

            if mode == 'Numeric':
                # Numeric encryption
                message_int = int(message)
                encrypted = self.numeric_encryption.encrypt(message_int)
                self.encrypted_data = encrypted
                result_text = f"Encrypted value: {encrypted}"
            else:
                # Text encryption
                encrypted = self.text_encryption.encrypt_text(message)
                self.encrypted_data = encrypted
                result_text = f"Encrypted text: {encrypted}"

            # Display result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_text)

            # Notify dashboard if callback is set
            if self.on_encryption_complete:
                end_time = time.time()
                self.on_encryption_complete(mode, end_time - start_time)

            messagebox.showinfo("Success", f"Message Encrypted in {mode} Mode")
            return True

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return False

    def get_encrypted_data(self):
        """Get the last encrypted data"""
        return self.encrypted_data