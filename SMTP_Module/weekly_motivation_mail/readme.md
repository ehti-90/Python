# Weekly Motivation Email

This project automatically sends a motivational email to yourself or anyone else on a specific day of the week. It uses Python's built-in `smtplib` module to connect to Gmail's SMTP server and send an email securely.

## Features

- Sends a motivational email automatically.
- Sends emails on a specific weekday.
- Uses Gmail SMTP.
- Uses a secure App Password instead of your Google account password.
- Stores sensitive information in a `.env` file.

## Requirements

- Python 3.x
- `python-dotenv`

Install the required package:

```bash
pip install python-dotenv
```

## How to Use

1. Clone this repository.

2. Move into the project folder.


3. Create a file named `.env` in the project directory.
4. Copy the contents of `.env.example` into your `.env` file.
5. Replace the placeholder values with your own Gmail address and App Password.
6. Open the Python file and change the recipient email address if you want to send the email to someone else.
7. Run the program.


## Automating the Script with Windows Task Scheduler

You can automate this project using **Windows Task Scheduler**, a built-in Windows tool that runs programs or scripts at scheduled times.
Instead of running the script manually every week, you can create a scheduled task that executes `main.py` every Sunday.

### Basic Steps

1. Open **Task Scheduler** from the Windows Start Menu.
2. Click **Create Basic Task**.
3. Give the task a name (for example, *Weekly Motivation Email*).
4. Choose **Weekly** as the trigger.
5. Select **Sunday** and choose the time you want the email to be sent.
6. Choose **Start a Program** as the action.
7. Set the program to your Python executable (for example, `python.exe`).
8. In the **Add arguments** field, enter the path to `main.py`.
9. Save the task.

Windows will now run the script automatically every Sunday at the scheduled time.

> **Note:** If you schedule the task to run only on Sundays, the `if weekday == 6:` check inside the script is optional and can be removed.

```bash
python main.py
```

## Gmail App Password

Google does not allow most applications to sign in with your normal Gmail password. Instead, you must create an **App Password** after enabling Two-Step Verification on your Google account.

The App Password is used only for applications like this project. It is safer than using your main Google password because it can be revoked at any time without affecting your Google account.

## `.env.example`

```text
EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_character_app_password
```

```

## Note

The `.env` file is not included in this repository because it contains sensitive information. Every user must create their own `.env` file and use their own Gmail address and App Password before running the project.

