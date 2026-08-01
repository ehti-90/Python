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

