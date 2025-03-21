import tkinter as tk  # Import Tkinter for GUI functionality
from tkinter import scrolledtext  # Import scrolled text for multi-line input
from send_email import send_email  # Import send_email function from send_email.py
from receive_email import receive_email  # Import receive_email function from receive_email.py

def open_send_email_window():
    """
    Opens a new window for sending emails. 
    Users can enter sender email, recipient email, subject, and message body.
    """
    send_root = tk.Toplevel()  # Create a new top-level window
    send_root.title("Send Email")  # Set window title
    send_root.geometry("400x300")  # Set window size

    # Label and input field for the sender's email
    tk.Label(send_root, text="Sender Email:").pack()
    sender_email_entry = tk.Entry(send_root, width=40)
    sender_email_entry.pack()

    # Label and input field for the app password
    tk.Label(send_root, text="App Password:").pack()
    app_password_entry = tk.Entry(send_root, width=40, show='*')  # Mask input for security
    app_password_entry.pack()

    # Label and input field for the recipient's email
    tk.Label(send_root, text="Recipient Email:").pack()
    recipient_email_entry = tk.Entry(send_root, width=40)
    recipient_email_entry.pack()

    # Label and input field for the email subject
    tk.Label(send_root, text="Subject:").pack()
    subject_entry = tk.Entry(send_root, width=40)
    subject_entry.pack()

    # Label and input field for the email body (multi-line text)
    tk.Label(send_root, text="Body:").pack()
    body_entry = tk.Text(send_root, height=5, width=40)
    body_entry.pack()

    # Button to send the email
    tk.Button(send_root, text="Send Email", command=lambda: send_email(
        sender_email_entry.get(), app_password_entry.get(), recipient_email_entry.get(),
        subject_entry.get(), body_entry.get("1.0", tk.END))  # Extract multi-line text
    ).pack()

    # Button to close the send email window
    tk.Button(send_root, text="Back", command=send_root.destroy).pack()

def open_receive_email_window():
    """
    Opens a new window for receiving emails.
    Users enter their email and app password to fetch their latest emails.
    """
    receive_root = tk.Toplevel()  # Create a new top-level window
    receive_root.title("Receive Email")  # Set window title
    receive_root.geometry("400x200")  # Set window size

    # Label and input field for the email address
    tk.Label(receive_root, text="Email Address:").pack()
    email_address_entry = tk.Entry(receive_root, width=40)
    email_address_entry.pack()

    # Label and input field for the app password
    tk.Label(receive_root, text="App Password:").pack()
    app_password_entry = tk.Entry(receive_root, width=40, show='*')  # Mask input for security
    app_password_entry.pack()

    # Button to receive emails
    tk.Button(receive_root, text="Receive Email", command=lambda: receive_email(
        email_address_entry.get(), app_password_entry.get())).pack()

    # Button to close the receive email window
    tk.Button(receive_root, text="Back", command=receive_root.destroy).pack()

def main_menu():
    """
    Creates the main menu window with options to send or receive emails.
    """
    root = tk.Tk()  # Create the main application window
    root.title("Email System")  # Set window title
    root.geometry("500x300")  # Set window size

    # Label for the main menu
    tk.Label(root, text="Email System", font=("Arial", 16, "bold")).pack(pady=10)

    # Button to open the send email window
    tk.Button(root, text="Send Email", width=20, command=open_send_email_window).pack(pady=10)

    # Button to open the receive email window
    tk.Button(root, text="Receive Email", width=20, command=open_receive_email_window).pack(pady=10)

    # Button to exit the application
    tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

    root.mainloop()  # Start the Tkinter event loop

# Run the main menu when the script is executed
if __name__ == "__main__":
    main_menu()
