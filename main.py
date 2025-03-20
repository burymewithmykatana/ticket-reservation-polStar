from tkinter import Tk
from gui import TicketBookingApp
from database import setup_database

if __name__ == "__main__":
    setup_database()
    root = Tk()
    app = TicketBookingApp(root)
    root.mainloop()
