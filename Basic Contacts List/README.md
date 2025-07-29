# Basic Contact List

A Python-based contact management application that allows users to add, view, edit, delete, and manage their personal contacts with a user-friendly command-line interface.

The application features input validation, color-coded output, sound effects for user feedback, and persistent storage of contact information in a local file.

## 📌 How It Works

1. **Imports and Setup**: The code starts by importing necessary modules - `colorama` for colored text, `playsound` for sound effects, `os` for file operations, `time` for delays, and `threading` for background sound playback.

2. **Contact Class**: A `Contact` class is defined that contains all the contact management methods. When the program starts, it creates an instance of this class which automatically calls the `__init__` method.

3. **Main Menu Loop**: The `__init__` method displays a menu asking users to choose an action (add/view/edit/delete/delall/exit/help), validates their input, and calls the appropriate method based on their choice.

4. **Add Method**: Prompts for name and phone number, validates both inputs (name 3-20 chars, number 8-15 digits), then writes the contact to the `contact_list` file in "name : number" format.

5. **View Method**: Opens the contact file, reads all lines, and displays them numbered from 1, or shows "Contact List is Empty" if no contacts exist.

6. **Edit Method**: Asks for a phone number to search, uses `any()` to check if it exists in the file, then prompts for new name and number with full validation before updating the contact.

7. **Delete and DelAll Methods**: Delete removes a specific contact by phone number, while DelAll asks for confirmation before removing the entire contact file.

8. **Help Method**: Displays all available options and redirects back to the main menu.

9. **Program Flow**: After each operation, the program shows a success/error message with sound, waits 3 seconds, then returns to the main menu by calling `__init__` again. 