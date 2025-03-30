import tkinter as tk
from tkinter import ttk
from core.encryption import HomomorphicEncryption
from core.text_encryption import TextHomomorphicEncryption
from ui.encryption_page import EncryptionPage
from ui.operations_page import OperationsPage
from ui.results_page import ResultsPage
from ui.dashboard import Dashboard

class HomomorphicEncryptionApp(tk.Tk):
    def __init__(self, numeric_encryption, text_encryption):
        super().__init__()

        # Set window title and size
        self.title("Homomorphic Encryption Toolkit")
        self.geometry("800x700")

        # Store encryption utilities
        self.numeric_encryption = numeric_encryption
        self.text_encryption = text_encryption

        # Create notebook for multiple pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Initialize page attributes to None
        self.dashboard = None
        self.encryption_page = None
        self.operations_page = None
        self.results_page = None

        # Create pages
        self.encryption_page = EncryptionPage(
            self.notebook,
            self.numeric_encryption,
            self.text_encryption
        )
        self.operations_page = OperationsPage(
            self.notebook,
            self.numeric_encryption,
            self.text_encryption
        )
        self.results_page = ResultsPage(
            self.notebook,
            self.numeric_encryption,
            self.text_encryption
        )
        self.dashboard = Dashboard(self.notebook, self)

        # Add pages to notebook
        self.notebook.add(self.dashboard, text="Dashboard")
        self.notebook.add(self.encryption_page, text="Encryption")
        self.notebook.add(self.operations_page, text="Operations")
        self.notebook.add(self.results_page, text="Results")

        # Set reference to app on top-level window
        self.app = self

    def switch_to_page(self, page_name):
        page_map = {
            'Dashboard': self.dashboard,
            'Encryption': self.encryption_page,
            'Operations': self.operations_page,
            'Results': self.results_page
        }

        page = page_map.get(page_name)
        if page:
            page_index = self.notebook.index(page)
            self.notebook.select(page_index)

    def get_page(self, page_name):
        """Get a reference to a specific page by name"""
        page_map = {
            'Dashboard': self.dashboard,
            'Encryption': self.encryption_page,
            'Operations': self.operations_page,
            'Results': self.results_page
        }
        return page_map.get(page_name)