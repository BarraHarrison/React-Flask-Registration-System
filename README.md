# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh


## Project Overview: React/Flask Registration System

## Introduction
This project is a user registration system built using a React frontend and a Flask backend.
The user information, including a username, password (hashed for security),
and email, is stored in a MySQL database (userDB) hosted in phpMyAdmin. This system performs the following functions:

## Registering new users.
Validating the uniqueness of the username and email.
Displaying relevant messages for both successful and failed registration attempts.

## Key Technologies
Frontend: React with Axios for handling HTTP requests.
Backend: Flask with Flask-Bcrypt for password hashing, Flask-SQLAlchemy for database handling, and Flask-JWT-Extended for authentication (if needed later).
Database: MySQL (via phpMyAdmin) with userDB containing a users table.

## Conclusion:
This system successfully handles user registration with validation and secure password hashing,
leveraging React for the frontend and Flask for the backend, and MySQL for data storage.
This setup ensures proper user management while providing relevant feedback to the user during the registration process.
