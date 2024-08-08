import sqlite3
from tkinter import messagebox

# Function to initialize the database and create the admin table
def initialize_db():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    
    # Insert default admin credentials if not already present
    cursor.execute('''
        INSERT OR IGNORE INTO admin (username, password) VALUES (?, ?)
    ''', ('admin', 'admin'))
    
    conn.commit()
    conn.close()

# Function to check login credentials
def validate_login(username, password):
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM admin WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return True
    else:
        return False

# Function to show appropriate login message
def save_admin(username, password, on_success):
    if validate_login(username, password):
        messagebox.showinfo("Login Success", "You have successfully logged in!")
        on_success()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")
