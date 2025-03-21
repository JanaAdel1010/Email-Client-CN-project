import imaplib  # Import IMAP library to fetch emails from the mail server
import email  # Import email module to parse email messages
from tkinter import messagebox  # Import messagebox from tkinter to display alerts
from plyer import notification  # Import plyer to display system notifications

def receive_email(email_address, app_password):
    """
    Fetches the latest email using IMAP with error handling.

    Parameters:
    email_address (str): The email address to log in to.
    app_password (str): The app-specific password for authentication.
    """

    # Validate input: Ensure email and password are provided
    if not email_address or not app_password:
        messagebox.showwarning("Warning", "Email and App Password are required!")  # Show warning if fields are empty
        return  # Exit the function early

    try:
        # Establish connection with Gmail's IMAP server
        mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Connect securely to Gmail's IMAP server
        mail.login(email_address, app_password)  # Log in using the provided email and app password
        mail.select('inbox')  # Select the "inbox" to fetch emails

        # Search for all emails in the inbox
        status, data = mail.search(None, 'ALL')  # 'ALL' fetches all emails
        if status != 'OK':
            messagebox.showerror("Error", "Failed to retrieve emails.")  # Show error if the search fails
            return

        # Convert the email ID list from bytes to a list of individual email IDs
        email_ids = data[0].split()  
        if not email_ids:
            messagebox.showinfo("Inbox Empty", "No new emails found.")  # Show info if no emails are found
            return

        # Fetch the latest email by selecting the last ID in the list
        latest_email_id = email_ids[-1]
        status, data = mail.fetch(latest_email_id, '(RFC822)')  # Retrieve the full email
        if status != 'OK':
            messagebox.showerror("Error", "Failed to fetch email content.")  # Show error if fetch fails
            return

        # Extract raw email content
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)  # Parse the email content

        # Extract email details
        from_email = msg.get("From", "Unknown Sender")  # Get sender's email
        to_email = msg.get("To", "Unknown Recipient")  # Get recipient's email
        subject = msg.get("Subject", "No Subject")  # Get email subject

        # Extract email body content
        body = "No message content"
        if msg.is_multipart():  # If the email has multiple parts 
            for part in msg.walk():  # Loop through each part of the email
                if part.get_content_type() == "text/plain":  # Look for plain text content
                    try:
                        body = part.get_payload(decode=True).decode()  # Decode the email content
                    except UnicodeDecodeError:
                        body = "Cannot decode email content."  # Handle decoding errors
                    break  # Stop after finding the first text/plain part
        else:  # If the email is not multipart, process it as a single part
            try:
                body = msg.get_payload(decode=True).decode()
            except UnicodeDecodeError:
                body = "Cannot decode email content."

        # Display a desktop notification with sender, subject, and a preview of the body
        notification.notify(
            title=f"New Email from {from_email}",
            message=f"Subject: {subject}\n{body[:100]}...",  # Show the first 100 characters of the body
            timeout=10  # Notification disappears after 10 seconds
        )

        mail.logout()  # Logout from the mail server to close the session

    # Handle authentication errors 
    except imaplib.IMAP4.error:
        messagebox.showerror("Authentication Error", "Invalid email or app password.")

    # Handle any other unexpected errors
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch emails: {e}")
