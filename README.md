<div align="center">
  <img alt="trees-of-secrets" height="200px" src="https://github.com/agarwalkrish26/Tree-of-Secrets/blob/main/static/logo.png">
</div>

# Tree of Secrets 🎄

A festive web application that allows users to log in and receive personalized secret messages in a magical Christmas-themed environment.

Note: 
- Currently, the application is not hosted anywhere. It is only available locally.
- The application is only functional for mobile devices and is not fully functional for PC yet.

## Features

- Secure user authentication system
- Animated Christmas-themed login page with falling snow effect
- Interactive gift box interface
- Stylized scroll message display
- Responsive design for mobile and desktop
- Custom scrollbar styling
- Session management
- Error handling and user feedback

## Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3
- JSON (for data storage)

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `config.json` file with the following structure:
   ```json
   {
     "users": {
       "username": "password"
     },
     "messages": {
       "username": "Your secret message here"
     }
   }
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Configuration

The application uses a `config.json` file for user management and message storage. This file should be kept secure and is included in `.gitignore`.

## Security Features

- Random session key generation
- Password-protected access
- Session management
- Login required decorator for protected routes

## Routes

- `/` - Login page
- `/auth` - Authentication endpoint
- `/main` - Main interface with gift box
- `/message` - Secret message display
- `/logout` - Session termination

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

<div align="center">
Developed with ❤️ by Krish Agarwal 🎄
</div>