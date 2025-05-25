# Password Manager

A secure and user-friendly password management application built with Python and Tkinter. This application helps you store, generate, and manage your passwords in a safe and organized way.

## Features

- Generate strong, random passwords
- Store website credentials securely
- Search for saved passwords
- Automatic password copying to clipboard
- User-friendly graphical interface
- JSON-based secure storage
- Input validation and error handling

## Requirements

- Python 3.x
- pyperclip==1.9.0

## Installation

1. Clone this repository:
```bash
git clone https://github.com/momed-ali01/password_manager.git
cd password_manager
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Features in Detail

1. **Password Generation**
   - Generates 12-character strong passwords
   - Includes uppercase letters, lowercase letters, numbers, and special characters
   - Automatically copies generated password to clipboard

2. **Password Storage**
   - Securely stores website credentials
   - Saves data in JSON format
   - Includes website name, email/username, and password

3. **Password Search**
   - Quick search functionality for saved passwords
   - Displays email and password for the requested website
   - Case-insensitive search

4. **User Interface**
   - Clean and intuitive GUI
   - Input validation
   - Error messages for invalid inputs
   - Default email field for convenience

## Data Storage

The application stores all passwords and credentials in a `data.json` file. The data is stored in the following format:

```json
{
    "Website": {
        "email": "user@example.com",
        "password": "generated_password"
    }
}
```

## Security Features

- Input validation to prevent empty submissions
- Secure JSON storage
- Strong password generation
- No plain text password display in the interface

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
