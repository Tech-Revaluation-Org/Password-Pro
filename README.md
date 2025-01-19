# Password-Pro

#### Overview
Password-Pro is a Python-based all-in-one password manager application built with PyQt5. This software provides functionalities to save, generate, view, and manage passwords efficiently. It also includes features like theme customization and data backup.


# Features
#### Password Keeper: Store passwords securely with associated website and username details.
#### Password Generator: Generate strong passwords with customizable length and strength levels.
#### View Passwords: Easily view saved passwords in a tabular format.
#### Settings: Each task includes "Set Timer" and "Delete" buttons for individual management.
#### Estimated Crack Time: Displays the estimated time required to crack a password, enhancing user awareness of password strength.

# Code Structure
## Main Window
The MainWindow class sets up the application's main interface and manages sidebar navigation.

## Database Management

create_table: Creates a SQLite database table for storing passwords.

save_password: Saves a password to the database.

refresh_table: Retrieves and displays all saved passwords.

## Password Management

create_password: Generates a password based on the selected strength and length.

generate_password: Generates and displays a new password, with an estimated crack time.

## Settings and Themes

change_theme: Changes the application's theme based on user selection.

Individual methods for each theme, e.g., set_dark_theme, set_elegant_blue_theme, etc.
