# Automatic Birthday Email Sender 🎉

## Overview

Automatic Birthday Email Sender is a Python project that sends personalized birthday emails to friends automatically. The program reads birthday information from a CSV file, checks if today matches any stored birthdays, personalizes an email template by replacing the recipient's name, and sends the email using Gmail's SMTP server.

The project is designed to be used with Windows Task Scheduler so that it runs automatically every day without requiring any manual interaction.

---

## CSV Format

The `birthdays.csv` file should contain the following columns:

```csv
name,email,year,month,day
John,john@example.com,2002,8,3
Jane,jane@example.com,2001,12,15
```

Only the **month** and **day** columns are used to determine whether today is someone's birthday.

---

## Environment Variables

Create a `.env` file in the project directory.

```env
my_email=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

> **Note:** Do **not** use your normal Gmail password. You must generate a Gmail App Password after enabling Two-Factor Authentication on your Google account.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/auto_Birthday_Wisher_mail.git
```

Move into the project directory:

```bash
cd auto_Birthday_Wisher_mail
```

Install the required packages:

```bash
pip install pandas python-dotenv
```

---

# Automating with Windows Task Scheduler

You can configure Windows Task Scheduler to execute the script automatically every day.

### Step 1

Open **Task Scheduler** from the Windows Start Menu.

### Step 2

Click **Create Basic Task**.

### Step 3

Give the task a name, for example:

```
Automatic Birthday Email Sender
```

Click **Next**.

### Step 4

Choose the trigger:

```
Daily
```

Click **Next**.

### Step 5

Select the time you want the script to run every day (for example, 9:00 AM).

Click **Next**.

### Step 6

Choose:

```
Start a Program
```

Click **Next**.

### Step 7

For **Program/script**, enter the full path to your Python executable.

Example:

```
C:\Users\YourName\AppData\Local\Programs\Python\Python313\python.exe
```

### Step 8

For **Add arguments**, enter the full path to your Python script.

Example:

```
"C:\Users\YourName\Projects\auto_Birthday_Wisher_mail\birthday_sender.py"
```

### Step 9

(Optional)

For **Start in**, enter the folder containing your project.

Example:

```
C:\Users\YourName\Projects\auto_Birthday_Wisher_mail
```

This ensures that relative file paths work correctly.

### Step 10

Click **Finish**.

The task will now run automatically every day at the specified time.

---

## Technologies Used

- Python
- Pandas
- smtplib
- python-dotenv
- Windows Task Scheduler

---

## Notes

- Keep your `.env` file private and never upload it to GitHub.
- Add `.env` to your `.gitignore` file.
- Make sure your computer is powered on at the scheduled time.
- If your computer is asleep or shut down, the task will not run until the computer is available.

---