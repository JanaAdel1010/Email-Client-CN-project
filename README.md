# **Python Email Client**

## **Overview**
This is a simple GUI-based email client built using Python and Tkinter. It allows users to send and receive emails using **SMTP** and **IMAP** protocols. The application supports Gmail and includes error handling for authentication and network issues.

## **Features**
✅ Send emails using **SMTP** (Gmail support)  
✅ Receive emails via **IMAP** (fetch latest email)  
✅ Secure login with **App Passwords**  
✅ **GUI built using Tkinter** for easy interaction  
✅ Error handling for authentication and network failures  

---

## **Installation**

### **1. Install Python Dependencies**
Ensure you have Python installed, then install the required dependencies:

```sh
pip install plyer
```

> Note: `smtplib`, `imaplib`, `email`, and `tkinter` are included in Python’s standard library.

---

## **Usage**

### **Run the application**
To start the GUI interface, run:

```sh
python gui.py
```

### **Send an Email**
1. Open the application and click **"Send Email"**.
2. Enter your Gmail **email address** and **app password**.
3. Fill in the recipient's email, subject, and message.
4. Click **"Send Email"**.

### **Receive the Latest Email**
1. Click **"Receive Email"** in the main menu.
2. Enter your Gmail **email address** and **app password**.
3. The subject of the latest email will be displayed.

---

## **File Structure**
```
📂 email-client
│-- 📄 gui.py             # Main GUI application
│-- 📄 send_email.py       # Handles sending emails
│-- 📄 receive_email.py    # Handles receiving emails
│-- 📄 README.md           # Project documentation
```

---

## **Code Overview**

### **`send_email.py`**
- Uses **SMTP** to send emails via **Gmail's SMTP server**.
- Requires **app passwords** for authentication.
- Uses **MIME** to structure email content.
- Error handling for **invalid credentials** and **network issues**.

### **`receive_email.py`**
- Uses **IMAP** to fetch the latest email.
- Retrieves the **email subject** and displays it.
- Handles errors like **invalid login** or **disabled IMAP access**.

### **`gui.py`**
- Provides a **Tkinter GUI** for sending and receiving emails.
- Uses `send_email.py` and `receive_email.py` for functionality.
- Includes **error handling** and a simple **user-friendly interface**.

---

## **Requirements**
- **Python 3.x**
- A **Gmail account** with **App Passwords** enabled.
- **IMAP access enabled** in your Gmail settings.

### **Enable IMAP in Gmail**
1. Go to [Gmail Settings](https://mail.google.com/).
2. Click on **See all settings** → **Forwarding and POP/IMAP**.
3. Enable **IMAP Access**.

### **Get a Gmail App Password**
1. Go to [Google Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification**.
3. Under **App Passwords**, generate a new password for this application.
4. Use the generated password instead of your Gmail password.

---

## **Author**
📌 **Jana Adel**  
📌 **Email:** Janaadel2000@gmail.com  

