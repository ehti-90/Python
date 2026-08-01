# Python Email Automation with smtplib

A collection of Python projects built using the `smtplib` module to learn email automation and implement real-world use cases.

The goal of this repository is to understand how SMTP works, gain hands-on experience with Python's email libraries, and build practical applications that automate email-related tasks.

## Objectives

- Learn the SMTP protocol
- Understand how email clients communicate with mail servers
- Use Python's built-in `smtplib` module
- Work with secure SMTP connections (TLS/SSL)
- Send plain text and HTML emails
- Handle authentication using Gmail App Passwords
- Build practical automation projects

## Technologies

- Python 3
- smtplib
- email package
- SSL/TLS
- SMTP

## Authentication with Gmail App Passwords

Google no longer allows most applications to authenticate to Gmail's SMTP server using your regular account password. Instead, you should use an **App Password** by going into security page in your google account and search app password from their you generate your app password, which is a unique 16-character password generated after enabling Two-Step Verification on your Google account.

An App Password allows applications such as Python scripts to securely access Gmail over SMTP without exposing your primary Google account password. It is limited to mail protocols (SMTP, IMAP, and POP), can be revoked at any time, and does not grant access to your Google Account through a web browser.


> **Security Tip:** Never hard-code your App Password in production code or upload it to GitHub. Store it in environment variables or a `.env` file, and add `.env` to your `.gitignore` to prevent accidentally exposing your credentials.

