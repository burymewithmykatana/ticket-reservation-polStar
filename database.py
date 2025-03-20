import sqlite3


class Database:
    def __init__(self, db_name="tickets.db"):
        """Initialize the database connection."""
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.setup_table()

    def setup_table(self):
        """Create the tickets table if it doesn't exist."""
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        """
        )
        self.connection.commit()

    def add_ticket(self, name, destination, date, time):
        """Add a new ticket to the database."""
        self.cursor.execute(
            """
        INSERT INTO tickets (name, destination, date, time)
        VALUES (?, ?, ?, ?)
        """,
            (name, destination, date, time),
        )
        self.connection.commit()

    def search_ticket(self, name):
        """Search for a ticket by name."""
        self.cursor.execute(
            """
        SELECT destination, date, time FROM tickets WHERE name = ?
        """,
            (name,),
        )
        return self.cursor.fetchone()

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()


# Helper functions to interact with the Database class
def setup_database():
    """Sets up the database"""
    db = Database()
    db.close_connection()


def add_ticket(name, destination, date, time):
    """Adds a ticket to the database."""
    db = Database()
    db.add_ticket(name, destination, date, time)
    db.close_connection()


def search_ticket(name):
    """Search for a ticket in the database."""
    db = Database()
    result = db.search_ticket(name)
    db.close_connection()
    return result
