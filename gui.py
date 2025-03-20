import tkinter as tk
from tkinter import messagebox
from database import add_ticket, search_ticket


class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Booking System")
        self.root.geometry("600x400")

        # Configure grid layout for the main window
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create frames
        self.create_registration_frame()
        self.create_search_frame()

    def create_registration_frame(self):
        """Create the registration frame."""
        self.registration_frame = tk.Frame(
            self.root, bg="light blue", borderwidth=2, relief="groove"
        )
        self.registration_frame.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

        # Add widgets to Registration Frame
        tk.Label(
            self.registration_frame,
            text="Registration",
            font=("Helvetica", 14),
            bg="light blue",
        ).grid(row=0, column=0, columnspan=2)

        tk.Label(self.registration_frame, text="Name:", bg="light blue").grid(
            row=1, column=0, sticky="EW"
        )
        self.name_entry = tk.Entry(self.registration_frame)
        self.name_entry.grid(row=1, column=1, sticky="EW")

        tk.Label(self.registration_frame, text="Destination:", bg="light blue").grid(
            row=2, column=0, sticky="EW"
        )
        self.destination_entry = tk.Entry(self.registration_frame)
        self.destination_entry.grid(row=2, column=1, sticky="EW")

        tk.Label(self.registration_frame, text="Date:", bg="light blue").grid(
            row=3, column=0, sticky="EW"
        )
        self.date_entry = tk.Entry(self.registration_frame)
        self.date_entry.grid(row=3, column=1, sticky="EW")

        tk.Label(self.registration_frame, text="Time:", bg="light blue").grid(
            row=4, column=0, sticky="EW"
        )
        self.time_entry = tk.Entry(self.registration_frame)
        self.time_entry.grid(row=4, column=1, sticky="EW")

        save_button = tk.Button(
            self.registration_frame, text="Save", command=self.save_ticket
        )
        save_button.grid(row=5, column=0, columnspan=2, sticky="EW")

        # Configure frame grid weights
        self.registration_frame.grid_columnconfigure(0, weight=1)
        self.registration_frame.grid_columnconfigure(1, weight=1)

    def create_search_frame(self):
        """Create the search frame."""
        self.search_frame = tk.Frame(self.root, borderwidth=2, relief="groove")
        self.search_frame.grid(row=0, column=1, sticky="NSEW", padx=10, pady=10)

        # Add widgets to Search Frame
        tk.Label(self.search_frame, text="Search", font=("Helvetica", 14)).grid(
            row=0, column=0, columnspan=2
        )

        tk.Label(self.search_frame, text="Search Ticket by Name:").grid(
            row=1, column=0, sticky="EW"
        )
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=1, column=1, sticky="EW")

        search_button = tk.Button(
            self.search_frame, text="Search", command=self.perform_search
        )
        search_button.grid(row=2, column=0, columnspan=2, sticky="EW")

        # Configure frame grid weights
        self.search_frame.grid_columnconfigure(0, weight=1)
        self.search_frame.grid_columnconfigure(1, weight=1)

    def save_ticket(self):
        """Save a ticket to the database."""
        name = self.name_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if name and destination and date and time:
            add_ticket(
                name, destination, date, time
            )  # Call the function from DB
            messagebox.showinfo("Success", "Ticket saved successfully!")

            # Clear the entries
            self.name_entry.delete(0, tk.END)
            self.destination_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def perform_search(self):
        """Search for a ticket by name."""
        name = self.search_entry.get()

        if name:
            result = search_ticket(name)  # Call the function from DB
            if result:
                messagebox.showinfo(
                    "Search Result",
                    f"Destination: {result[0]}\nDate: {result[1]}\nTime: {result[2]}",
                )
            else:
                messagebox.showerror("Error", "No ticket found for the given name!")
        else:
            messagebox.showerror("Error", "Please enter a name to search!")
