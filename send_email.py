import smtplib  # Import the smtplib module to handle email sending via SMTP
from email.mime.text import MIMEText  # Import MIMEText to create plain text email content
from email.mime.multipart import MIMEMultipart  # Import MIMEMultipart to handle multiple email parts
from tkinter import messagebox  # Import messagebox from tkinter to display alerts and messages

def send_email(sender_email, app_password, recipient_email, subject, body):
    """
    Sends an email using SMTP with error handling.

    Parameters:
    sender_email (str): The email address sending the email.
    app_password (str): The app-specific password for SMTP authentication.
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The content of the email.
    """

    # Validate input: Ensure all fields are provided and not empty
    if not sender_email or not app_password or not recipient_email or not subject or not body.strip():
        messagebox.showwarning("Warning", "All fields are required!")  # Show warning if any field is missing
        return  # Exit the function early if validation fails

    try:
        # Establish connection with Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server on port 587
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, app_password)  # Log in using the sender's email and app password

        # Create the email message using MIMEMultipart
        msg = MIMEMultipart()  # Initialize a MIMEMultipart object to create the email
        msg['From'] = sender_email  # Set the sender's email address
        msg['To'] = recipient_email  # Set the recipient's email address
        msg['Subject'] = subject  # Set the subject of the email
        msg.attach(MIMEText(body, 'plain'))  # Attach the email body as plain text

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())  # Convert the email to a string and send it
        server.quit()  # Close the SMTP server connection

        # Show a success message upon successful email delivery
        messagebox.showinfo("Success", "Email sent successfully!")

    # Handle authentication errors 
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Invalid email or app password.")

    # Handle other SMTP-related errors 
    except smtplib.SMTPException as e:
        messagebox.showerror("SMTP Error", f"Failed to send email: {e}")

    # Handle any other unexpected exceptions
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
