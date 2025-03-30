import tkinter as tk
from tkinter import ttk, messagebox
import ast

class ResultsPage(tk.Frame):
    def __init__(self, master, numeric_encryption, text_encryption):
        super().__init__(master)
        self.master = master
        self.numeric_encryption = numeric_encryption
        self.text_encryption = text_encryption

        # Decryption state
        self.decryption_result = None

        # Create page layout
        self.create_results_page()

    def create_results_page(self):
        # Title
        title_label = ttk.Label(
            self,
            text="Decryption & Results",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)

        # Operation Result Frame
        operation_frame = ttk.LabelFrame(self, text="Homomorphic Operation Result")
        operation_frame.pack(pady=10, padx=20, fill='x')

        self.operation_result_text = tk.Text(operation_frame, height=3, width=70)
        self.operation_result_text.pack(pady=10)

        # Decryption Frame
        decrypt_frame = ttk.LabelFrame(self, text="Decryption")
        decrypt_frame.pack(pady=10, padx=20, fill='x')

        # Load Operation Result Button
        load_btn = ttk.Button(
            decrypt_frame,
            text="Load Operation Result",
            command=self.load_operation_result
        )
        load_btn.pack(pady=10)

        # Decrypt Button
        decrypt_btn = ttk.Button(
            decrypt_frame,
            text="Decrypt Result",
            command=self.decrypt_result
        )
        decrypt_btn.pack(pady=10)

        # Decryption Result Frame
        result_frame = ttk.LabelFrame(self, text="Decryption Result")
        result_frame.pack(pady=10, padx=20, fill='x')

        self.result_text = tk.Text(result_frame, height=5, width=70)
        self.result_text.pack(pady=10)

    def load_operation_result(self):
        try:
            # Get the main application instance
            app = self.winfo_toplevel()

            # Get the operations page through the parent application
            operations_page = app.get_page('Operations')
            if operations_page:
                operation_result = operations_page.get_operation_result()
                if operation_result:
                    self.operation_result_text.delete(1.0, tk.END)
                    self.operation_result_text.insert(tk.END, str(operation_result))
                    messagebox.showinfo("Success", "Operation result loaded")
                else:
                    messagebox.showerror("Error", "No operation result available")
            else:
                messagebox.showerror("Error", "Cannot find operations page")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load operation result: {str(e)}")

    def decrypt_result(self):
        try:
            # Get the operation result
            result_str = self.operation_result_text.get(1.0, tk.END).strip()
            
            if not result_str:
                messagebox.showerror("Error", "No operation result to decrypt")
                return

            # Parse the result tuple from the string
            try:
                if ': ' in result_str:
                    result_str = result_str.split(': ')[1]
                result = ast.literal_eval(result_str)
            except:
                messagebox.showerror("Error", "Invalid operation result format")
                return

            # Ensure numeric_encryption has a valid key
            if self.numeric_encryption.private_key is None:
                # Regenerate keys if needed
                self.numeric_encryption.generate_key()

            # Decrypt the result
            decrypted = self.numeric_encryption.decrypt(result)

            # Display decryption result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Decrypted Result: {decrypted}")
            
            # Store the result
            self.decryption_result = decrypted
            
            messagebox.showinfo("Success", "Result decrypted successfully")

        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

    def get_decryption_result(self):
        return self.decryption_result