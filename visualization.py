import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class EncryptionVisualizer:
    def __init__(self, master):
        """
        Initialize visualization components

        Args:
            master (tk.Tk or tk.Frame): Parent window or frame
        """
        self.master = master
        self.figures = {}

    def create_encryption_complexity_chart(self, encryption_data):
        """
        Create a comprehensive encryption complexity chart

        Args:
            encryption_data (dict): Encryption performance data
        """
        fig, ax = plt.subplots(figsize=(10, 5))

        modes = list(encryption_data.keys())
        times = list(encryption_data.values())

        # Color gradient
        colors = plt.cm.viridis(np.linspace(0, 1, len(modes)))

        # Bar chart with gradient colors
        bars = ax.bar(modes, times, color=colors)
        ax.set_title('Encryption Time Complexity', fontsize=15)
        ax.set_xlabel('Encryption Mode', fontsize=12)
        ax.set_ylabel('Time (ms)', fontsize=12)

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontsize=10)

        return fig

    def create_key_distribution_chart(self, public_keys):
        """
        Create an enhanced key distribution visualization

        Args:
            public_keys (list): List of public keys
        """
        fig, ax = plt.subplots(figsize=(10, 5))

        # Normalize public keys
        normalized_keys = [(key - min(public_keys)) / (max(public_keys) - min(public_keys)) for key in public_keys]

        # Scatter plot with additional information
        scatter = ax.scatter(
            range(len(public_keys)),
            normalized_keys,
            c=public_keys,
            cmap='plasma',
            s=100  # Marker size
        )

        ax.set_title('Public Key Distribution', fontsize=15)
        ax.set_xlabel('Key Index', fontsize=12)
        ax.set_ylabel('Normalized Key Value', fontsize=12)

        # Colorbar to show actual key values
        plt.colorbar(scatter, label='Actual Key Value')

        return fig

    def create_operations_performance_chart(self, operation_times):
        """
        Create a line chart showing performance of different operations

        Args:
            operation_times (dict): Dictionary of operation times
        """
        fig, ax = plt.subplots(figsize=(10, 5))

        operations = list(operation_times.keys())
        times = list(operation_times.values())

        ax.plot(operations, times, marker='o', linestyle='-', linewidth=2, markersize=10)
        ax.set_title('Homomorphic Operations Performance', fontsize=15)
        ax.set_xlabel('Operation Type', fontsize=12)
        ax.set_ylabel('Time (ms)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)

        # Add value labels
        for i, txt in enumerate(times):
            ax.annotate(f'{txt:.2f}',
                        (operations[i], times[i]),
                        xytext=(10, 10),
                        textcoords='offset points')

        return fig

    def embed_matplotlib_chart(self, fig, frame):
        """
        Embed a matplotlib figure in a Tkinter frame

        Args:
            fig (matplotlib.figure.Figure): Matplotlib figure
            frame (tk.Frame): Frame to embed the chart

        Returns:
            FigureCanvasTkAgg: Canvas containing the plot
        """
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        return canvas

    def update_visualization(self, visualization_type, data):
        """
        Update or create a specific visualization

        Args:
            visualization_type (str): Type of visualization
            data (any): Data for visualization
        """
        visualization_methods = {
            'complexity': self.create_encryption_complexity_chart,
            'key_distribution': self.create_key_distribution_chart,
            'operations_performance': self.create_operations_performance_chart
        }

        method = visualization_methods.get(visualization_type)
        if method:
            return method(data)
        else:
            raise ValueError(f"Unknown visualization type: {visualization_type}")