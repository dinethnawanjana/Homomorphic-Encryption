import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import numpy as np
from tkinter import messagebox

class Dashboard(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg='white')

        # Initialize tracking variables
        self.total_encryptions = tk.IntVar(value=0)
        self.total_operations = tk.IntVar(value=0)
        self.encryption_times = []
        self.operation_types = []
        self.mode_counts = {
            'Numeric': tk.IntVar(value=0),
            'Text': tk.IntVar(value=0),
            'Add': tk.IntVar(value=0),
            'Multiply': tk.IntVar(value=0)
        }
        
        # Performance tracking
        self.avg_encryption_time = tk.DoubleVar(value=0.0)
        self.avg_operation_time = tk.DoubleVar(value=0.0)
        self.success_rate = tk.DoubleVar(value=100.0)
        self.total_errors = tk.IntVar(value=0)
        
        # Auto-refresh settings
        self.refresh_interval = 1000  # 1 second
        self.auto_refresh = True

        # Create figure with style settings
        plt.style.use('default')  # Use default style instead of seaborn
        self.fig = plt.figure(figsize=(10, 6), dpi=100)
        self.fig.patch.set_facecolor('#f0f0f0')
        
        # Create canvas with proper sizing
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().configure(bg='white')
        
        # Create dashboard layout
        self.create_dashboard()
        
        # Bind to page events
        self.bind_page_events()
        
        # Initialize plots
        self._initialize_plots()
        
        # Start the auto-refresh cycle
        self.start_auto_refresh()

    def bind_page_events(self):
        """Bind to events from other pages to capture data"""
        try:
            # Get references to other pages
            encryption_page = self.app.get_page('Encryption')
            operations_page = self.app.get_page('Operations')

            if encryption_page:
                encryption_page.on_encryption_complete = self.track_encryption_event

            if operations_page:
                operations_page.on_operation_complete = self.track_operation_event

        except Exception as e:
            print(f"Error binding page events: {e}")
            self.total_errors.set(self.total_errors.get() + 1)

    def track_encryption_event(self, mode, duration_secs):
        """Track encryption operations"""
        try:
            # Convert duration to milliseconds
            duration_ms = duration_secs * 1000
            
            # Update counts
            self.mode_counts[mode].set(self.mode_counts[mode].get() + 1)
            self.total_encryptions.set(self.total_encryptions.get() + 1)
            
            # Record timing
            self.encryption_times.append(duration_ms)
            self.operation_types.append(f'{mode} Encryption')
            
            # Update averages
            encryption_times = [t for t, op in zip(self.encryption_times, self.operation_types) 
                              if 'Encryption' in op]
            if encryption_times:
                self.avg_encryption_time.set(round(sum(encryption_times) / len(encryption_times), 2))
            
            # Update success rate and refresh
            self.update_success_rate()
            self.update_dashboard_stats()

        except Exception as e:
            print(f"Error in encryption tracking: {e}")
            self.total_errors.set(self.total_errors.get() + 1)
            self.update_success_rate()

    def track_operation_event(self, operation_type, duration_secs):
        """Track homomorphic operations"""
        try:
            # Convert duration to milliseconds
            duration_ms = duration_secs * 1000
            
            # Update counts
            self.mode_counts[operation_type].set(self.mode_counts[operation_type].get() + 1)
            self.total_operations.set(self.total_operations.get() + 1)
            
            # Record timing
            self.encryption_times.append(duration_ms)
            self.operation_types.append(f'{operation_type} Operation')
            
            # Update averages
            operation_times = [t for t, op in zip(self.encryption_times, self.operation_types) 
                             if 'Operation' in op]
            if operation_times:
                self.avg_operation_time.set(round(sum(operation_times) / len(operation_times), 2))
            
            # Update success rate and refresh
            self.update_success_rate()
            self.update_dashboard_stats()

        except Exception as e:
            print(f"Error in operation tracking: {e}")
            self.total_errors.set(self.total_errors.get() + 1)
            self.update_success_rate()

    def update_success_rate(self):
        """Update the success rate based on total operations and errors"""
        total_ops = self.total_encryptions.get() + self.total_operations.get()
        if total_ops > 0:
            success_rate = ((total_ops - self.total_errors.get()) / total_ops) * 100
            self.success_rate.set(round(success_rate, 1))
        else:
            self.success_rate.set(100.0)

    def start_auto_refresh(self):
        """Start the auto-refresh cycle"""
        if self.auto_refresh:
            self.update_dashboard_stats()
            self.after(self.refresh_interval, self.start_auto_refresh)

    def create_dashboard(self):
        # Main container with grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        # Title with real-time indicator
        title_frame = ttk.Frame(self)
        title_frame.grid(row=0, column=0, columnspan=2, sticky='ew', pady=10)
        
        title_label = ttk.Label(
            title_frame,
            text="Homomorphic Encryption Dashboard",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, padx=5, sticky='w')
        
        self.status_label = ttk.Label(
            title_frame,
            text="● Live",
            font=('Arial', 10),
            foreground='green'
        )
        self.status_label.grid(row=0, column=1, padx=5, sticky='w')

        # Left panel for statistics
        stats_frame = ttk.Frame(self)
        stats_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
        
        # Configure grid weights for stats sections
        stats_frame.grid_rowconfigure(0, weight=1)
        stats_frame.grid_rowconfigure(1, weight=1)
        stats_frame.grid_rowconfigure(2, weight=1)
        stats_frame.grid_columnconfigure(0, weight=1)

        # 1. Encryption Stats Section
        encryption_frame = ttk.LabelFrame(stats_frame, text="Encryption Statistics")
        encryption_frame.grid(row=0, column=0, sticky='nsew', pady=5)
        
        self.encryption_stats = {
            'total': ttk.Label(encryption_frame, text="Total: 0"),
            'numeric': ttk.Label(encryption_frame, text="Numeric: 0"),
            'text': ttk.Label(encryption_frame, text="Text: 0")
        }
        for i, (key, label) in enumerate(self.encryption_stats.items()):
            label.grid(row=i, column=0, pady=5, padx=10, sticky='w')

        # 2. Operation Stats Section
        operations_frame = ttk.LabelFrame(stats_frame, text="Operation Statistics")
        operations_frame.grid(row=1, column=0, sticky='nsew', pady=5)
        
        self.operation_stats = {
            'total': ttk.Label(operations_frame, text="Total: 0"),
            'add': ttk.Label(operations_frame, text="Add: 0"),
            'multiply': ttk.Label(operations_frame, text="Multiply: 0")
        }
        for i, (key, label) in enumerate(self.operation_stats.items()):
            label.grid(row=i, column=0, pady=5, padx=10, sticky='w')

        # 3. Performance Stats Section
        performance_frame = ttk.LabelFrame(stats_frame, text="Performance Metrics")
        performance_frame.grid(row=2, column=0, sticky='nsew', pady=5)
        
        self.performance_stats = {
            'encryption_time': ttk.Label(performance_frame, text="Avg Encryption: 0.0ms"),
            'operation_time': ttk.Label(performance_frame, text="Avg Operation: 0.0ms"),
            'success_rate': ttk.Label(performance_frame, text="Success Rate: 100%"),
            'errors': ttk.Label(performance_frame, text="Total Errors: 0")
        }
        for i, (key, label) in enumerate(self.performance_stats.items()):
            label.grid(row=i, column=0, pady=5, padx=10, sticky='w')

        # Right panel for visualizations
        viz_frame = ttk.LabelFrame(self, text="Performance Visualization")
        viz_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=5)
        viz_frame.grid_columnconfigure(0, weight=1)
        viz_frame.grid_rowconfigure(0, weight=1)
        
        # Add matplotlib canvas to visualization frame
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        # Bottom control panel
        control_frame = ttk.Frame(self)
        control_frame.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10, padx=10)

        # Auto-refresh toggle
        self.refresh_var = tk.BooleanVar(value=True)
        refresh_check = ttk.Checkbutton(
            control_frame,
            text="Auto Refresh",
            variable=self.refresh_var,
            command=self.toggle_auto_refresh
        )
        refresh_check.grid(row=0, column=0, padx=5)

        # Manual refresh button
        refresh_btn = ttk.Button(
            control_frame,
            text="Refresh Now",
            command=self.manual_refresh
        )
        refresh_btn.grid(row=0, column=1, padx=5)

        # Reset stats button
        reset_btn = ttk.Button(
            control_frame,
            text="Reset Stats",
            command=self.reset_stats
        )
        reset_btn.grid(row=0, column=2, padx=5)

    def update_statistics(self):
        """Update all statistics labels"""
        try:
            # Update encryption stats
            self.encryption_stats['total'].configure(text=f"Total: {self.total_encryptions.get()}")
            self.encryption_stats['numeric'].configure(text=f"Numeric: {self.mode_counts['Numeric'].get()}")
            self.encryption_stats['text'].configure(text=f"Text: {self.mode_counts['Text'].get()}")

            # Update operation stats
            self.operation_stats['total'].configure(text=f"Total: {self.total_operations.get()}")
            self.operation_stats['add'].configure(text=f"Add: {self.mode_counts['Add'].get()}")
            self.operation_stats['multiply'].configure(text=f"Multiply: {self.mode_counts['Multiply'].get()}")

            # Update performance stats
            self.performance_stats['encryption_time'].configure(
                text=f"Avg Encryption: {self.avg_encryption_time.get():.1f}ms"
            )
            self.performance_stats['operation_time'].configure(
                text=f"Avg Operation: {self.avg_operation_time.get():.1f}ms"
            )
            self.performance_stats['success_rate'].configure(
                text=f"Success Rate: {self.success_rate.get():.1f}%"
            )
            self.performance_stats['errors'].configure(
                text=f"Total Errors: {self.total_errors.get()}"
            )
        except Exception as e:
            print(f"Error updating statistics: {e}")
            self.total_errors.set(self.total_errors.get() + 1)

    def update_dashboard_stats(self):
        """Update all dashboard statistics and visualizations"""
        try:
            # Update statistics
            self.update_statistics()

            # Blink the live status indicator
            self.status_label.configure(foreground='red')
            self.after(100, lambda: self.status_label.configure(foreground='green'))

            # Update visualizations if we have data
            if self.encryption_times:
                # Clear previous plots
                self.fig.clear()
                
                # Create subplots with proper spacing
                gs = self.fig.add_gridspec(2, 1, height_ratios=[2, 1], hspace=0.4)
                self.fig.subplots_adjust(right=0.9, left=0.1, top=0.95, bottom=0.1)
                
                # Performance Timeline (top)
                ax1 = self.fig.add_subplot(gs[0])
                self._update_performance_timeline(ax1)
                
                # Operation Distribution (bottom)
                ax2 = self.fig.add_subplot(gs[1])
                self._update_operation_distribution(ax2)
                
                # Draw the updated figure
                self.canvas.draw()
            
            # Limit operation history
            if len(self.encryption_times) > 20:
                self.encryption_times = self.encryption_times[-20:]
                self.operation_types = self.operation_types[-20:]

        except Exception as e:
            print(f"Error updating dashboard stats: {e}")
            self.total_errors.set(self.total_errors.get() + 1)

    def toggle_auto_refresh(self):
        """Toggle auto-refresh on/off"""
        self.auto_refresh = self.refresh_var.get()
        if self.auto_refresh:
            self.status_label.configure(foreground='green', text="● Live")
            self.start_auto_refresh()
        else:
            self.status_label.configure(foreground='gray', text="○ Paused")

    def manual_refresh(self):
        """Manually refresh the dashboard"""
        self.status_label.configure(foreground='blue', text="↻ Refreshing")
        self.update_dashboard_stats()
        self.after(500, lambda: self.status_label.configure(
            foreground='green' if self.auto_refresh else 'gray',
            text="● Live" if self.auto_refresh else "○ Paused"
        ))

    def reset_stats(self):
        """Reset all statistics to initial values"""
        if tk.messagebox.askyesno("Reset Stats", "Are you sure you want to reset all statistics?"):
            self.total_encryptions.set(0)
            self.total_operations.set(0)
            self.encryption_times.clear()
            self.operation_types.clear()
            for var in self.mode_counts.values():
                var.set(0)
            self.avg_encryption_time.set(0.0)
            self.avg_operation_time.set(0.0)
            self.success_rate.set(100.0)
            self.total_errors.set(0)
            self.update_dashboard_stats()

    def show_detailed_stats(self):
        """Show detailed statistics in a new window"""
        stats_window = tk.Toplevel(self)
        stats_window.title("Detailed Statistics")
        stats_window.geometry("400x600")

        # Create scrollable frame
        canvas = tk.Canvas(stats_window)
        scrollbar = ttk.Scrollbar(stats_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add detailed statistics
        sections = [
            ("Encryption Statistics", [
                ("Total Encryptions", self.total_encryptions),
                ("Numeric Encryptions", self.mode_counts['Numeric']),
                ("Text Encryptions", self.mode_counts['Text']),
                ("Average Encryption Time", self.avg_encryption_time, "ms")
            ]),
            ("Operation Statistics", [
                ("Total Operations", self.total_operations),
                ("Add Operations", self.mode_counts['Add']),
                ("Multiply Operations", self.mode_counts['Multiply']),
                ("Average Operation Time", self.avg_operation_time, "ms")
            ]),
            ("Performance Metrics", [
                ("Success Rate", self.success_rate, "%"),
                ("Total Errors", self.total_errors),
                ("Last Update", lambda: time.strftime("%H:%M:%S"))
            ])
        ]

        row = 0
        for section_title, stats in sections:
            ttk.Label(
                scrollable_frame,
                text=section_title,
                font=('Arial', 12, 'bold')
            ).grid(row=row, column=0, columnspan=2, pady=10)
            row += 1

            for stat_name, stat_var, *extra in stats:
                ttk.Label(
                    scrollable_frame,
                    text=f"{stat_name}:",
                    font=('Arial', 10)
                ).grid(row=row, column=0, padx=5, pady=2, sticky='e')

                if callable(stat_var):
                    value = stat_var()
                else:
                    value = f"{stat_var.get()}{extra[0] if extra else ''}"

                ttk.Label(
                    scrollable_frame,
                    text=value,
                    font=('Arial', 10, 'bold')
                ).grid(row=row, column=1, padx=5, pady=2, sticky='w')
                row += 1

        # Add operation history
        ttk.Label(
            scrollable_frame,
            text="Recent Operations",
            font=('Arial', 12, 'bold')
        ).grid(row=row, column=0, columnspan=2, pady=10)
        row += 1

        for i, (op_type, time_taken) in enumerate(zip(self.operation_types[-10:], self.encryption_times[-10:])):
            ttk.Label(
                scrollable_frame,
                text=f"{op_type}:",
                font=('Arial', 10)
            ).grid(row=row, column=0, padx=5, pady=2, sticky='e')
            ttk.Label(
                scrollable_frame,
                text=f"{time_taken:.2f} ms",
                font=('Arial', 10, 'bold')
            ).grid(row=row, column=1, padx=5, pady=2, sticky='w')
            row += 1

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _initialize_plots(self):
        """Initialize the plots with empty data"""
        self.fig.clear()
        
        # Create subplots with proper spacing
        gs = self.fig.add_gridspec(2, 1, height_ratios=[2, 1], hspace=0.4)
        self.fig.subplots_adjust(right=0.9, left=0.1, top=0.95, bottom=0.1)
        
        # Performance Timeline (top)
        ax1 = self.fig.add_subplot(gs[0])
        ax1.set_title('Performance Timeline', fontsize=10, pad=10)
        ax1.set_xlabel('Operation Number', fontsize=8)
        ax1.set_ylabel('Time (ms)', fontsize=8)
        ax1.tick_params(labelsize=8)
        ax1.grid(True, linestyle='--', alpha=0.7)
        
        # Operation Distribution (bottom)
        ax2 = self.fig.add_subplot(gs[1])
        ax2.set_title('Operation Distribution', fontsize=10, pad=10)
        ax2.tick_params(labelsize=8)
        
        # Draw empty plots
        self.canvas.draw()

    def _update_performance_timeline(self, ax):
        """Update the performance timeline chart"""
        if not self.encryption_times:
            return

        # Clear previous plot
        ax.clear()

        # Create x-axis points
        x = range(1, len(self.encryption_times) + 1)
        
        # Create scatter plot with different markers and colors
        for i, (time, op_type) in enumerate(zip(self.encryption_times, self.operation_types)):
            if 'Encryption' in op_type:
                color = '#3498db'  # Blue
                marker = 'o'
                label = 'Encryption' if i == 0 else None
            elif 'Add' in op_type:
                color = '#2ecc71'  # Green
                marker = 's'
                label = 'Add Operation' if i == 0 else None
            else:  # Multiply
                color = '#e74c3c'  # Red
                marker = '^'
                label = 'Multiply Operation' if i == 0 else None
            
            ax.scatter(i + 1, time, c=color, marker=marker, s=50, alpha=0.6, label=label)

        # Add trend line if we have more than one point
        if len(x) > 1:
            z = np.polyfit(x, self.encryption_times, 1)
            p = np.poly1d(z)
            ax.plot(x, p(x), "--", color='#95a5a6', alpha=0.8, label='Trend')

        # Customize plot
        ax.set_title('Performance Timeline', fontsize=10, pad=10)
        ax.set_xlabel('Operation Number', fontsize=8)
        ax.set_ylabel('Time (ms)', fontsize=8)
        ax.tick_params(labelsize=8)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Add legend with smaller font
        if self.encryption_times:
            ax.legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5))

        # Set y-axis to start from 0
        ax.set_ylim(bottom=0)

    def _update_operation_distribution(self, ax):
        """Update the operation distribution pie chart"""
        if not self.operation_types:
            return

        # Clear previous plot
        ax.clear()

        # Count operation types
        op_counts = {
            'Numeric\nEncryption': len([op for op in self.operation_types if 'Numeric' in op]),
            'Text\nEncryption': len([op for op in self.operation_types if 'Text' in op]),
            'Add\nOperations': len([op for op in self.operation_types if 'Add' in op]),
            'Multiply\nOperations': len([op for op in self.operation_types if 'Multiply' in op])
        }

        # Remove empty categories
        op_counts = {k: v for k, v in op_counts.items() if v > 0}

        if not op_counts:
            ax.set_title('No Operations Yet', fontsize=10, pad=10)
            return

        # Create pie chart with custom colors
        colors = ['#3498db', '#9b59b6', '#2ecc71', '#e74c3c']
        wedges, texts, autotexts = ax.pie(
            op_counts.values(),
            labels=op_counts.keys(),
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            pctdistance=0.85,
            explode=[0.05] * len(op_counts)
        )

        # Customize plot
        ax.set_title('Operation Distribution', fontsize=10, pad=10)
        
        # Style the labels and percentages
        plt.setp(autotexts, size=8, weight="bold")
        plt.setp(texts, size=8)
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')