This C++ code implements a simple Library Management System that interacts with a MySQL database. It allows for basic administrative tasks like adding books and students, and user functions such as checking out books.

Features
MySQL Database Integration: Connects to a MySQL database to store and retrieve library and student data.
Book Management:
Add Books: Administrators can add new books with their names and quantities to the library table.
Display Books: Shows all available books and their quantities from the database.
Book Availability Check: Checks if a specific book exists and its quantity.
Student Management:
Add Students: Administrators can register new students with their ID, name, and number to the student table.
Book Borrowing (User Functionality):
Users can enter their student ID to check if they are registered.
If registered, they can request a book. The system checks availability and decrements the book's quantity in the database upon successful "borrowing."
User Interface: A simple console-based interface for interaction.
Prerequisites
To compile and run this code, you'll need the following:

C++ Compiler: A C++ compiler (e.g., MinGW/GCC or MSVC).
MySQL Server: A running MySQL server instance.
MySQL C API Connector: The development libraries for connecting C++ to MySQL.
For Windows (using MinGW/GCC): You'll typically need to download the MySQL Connector/C and include its lib and include directories during compilation.
For Windows (using MSVC): The MySQL Connector/C++ provides the necessary libraries and headers.
Database Setup: You need a database named Manage and two tables: library and student.
Database Setup Steps:
Create Database:
SQL

CREATE DATABASE Manage;
USE Manage;
Create library table:
SQL

CREATE TABLE library (
    Name VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL
);
Create student table:
SQL

CREATE TABLE student (
    Id VARCHAR(255) PRIMARY KEY,
    Student_Name VARCHAR(255) NOT NULL,
    Student_Number VARCHAR(255)
);
MySQL User Credentials: The code uses root as the user and Vibhor123# as the password. Ensure these credentials are correct for your MySQL setup and that the user has appropriate permissions to access the Manage database. If your root user has a different password, or if you prefer to use a different user, modify the const char* USER and const char* PW variables in the C++ code.
How to Compile and Run
Save the Code: Save the provided C++ code as library_management.cpp.

Compile:
This step varies depending on your compiler and how you've set up the MySQL Connector/C.

Using MinGW (GCC):
You'll need to specify the include and library paths for your MySQL Connector/C installation. Replace C:\path\to\mysql\connector with your actual path.

Bash

g++ library_management.cpp -o library_management.exe -I"C:\path\to\mysql\connector\include" -L"C:\path\to\mysql\connector\lib" -lmysqlclient
Using Visual Studio (MSVC):
It's recommended to set up a Visual Studio project. Go to Project > Properties > VC++ Directories and add the include and library paths for MySQL Connector/C++. Then, under Linker > Input, add libmysql.lib (or mysqlclient.lib). Alternatively, compile from the Developer Command Prompt:

Bash

cl library_management.cpp /I"C:\path\to\mysql\connector\include" /link /LIBPATH:"C:\path\to\mysql\connector\lib" libmysql.lib
Run:
Execute the compiled program:

Bash

./library_management.exe
or simply

Bash

library_management.exe
Usage
Initial Connection: When you run the program, it will attempt to connect to the MySQL database. You should see "Logged In!" upon success.
Main Menu:
1. Administration: Access administrative functions (Add Book, Add Student).
2. User: Access user functions (Borrow Book).
0. Exit: Close the application.
Administration (Choice 1)
1. Add Book:
Enter the book name.
Enter the quantity of the book.
The book details will be added to the library table.
2. Add Student:
Enter the student's ID.
Enter the student's name.
Enter the student's number.
The student details will be added to the student table.
0. Exit: Return to the main menu.
User (Choice 2)
The system first displays all available books.
Enter Your ID: Input your student ID. The system checks if the ID exists in the student table.
Enter Book Name: If the ID is found, enter the name of the book you wish to borrow.
If the book is available, its quantity in the database will be decremented, and a "Borrowing Book...." message will appear. If not, it will indicate "Book is not Available."
Important Considerations
Security: The database credentials are hardcoded. For a production environment, this is a significant security risk. Consider using configuration files or environment variables to store credentials securely.
Error Handling: Basic error handling for MySQL queries is present, but more robust error management and user input validation would improve the application's resilience.
Input Validation: The current code doesn't perform extensive input validation (e.g., checking for non-numeric input for quantity, or special characters in names that could lead to SQL injection vulnerabilities). This should be improved for a production system.
bits/stdc++.h: This header is GCC-specific and includes most standard library headers. For better portability and to only include necessary headers, consider replacing it with specific includes like <string>, <vector>, etc.
SQL Injection: The code is vulnerable to SQL injection because it directly concatenates user input into SQL queries. For example, if a user enters ' OR '1'='1 as a book name, it could lead to unexpected behavior. Always use prepared statements to prevent SQL injection in production applications. The MySQL C API supports prepared statements.
system("cls") and Sleep(): These are Windows-specific functions. For cross-platform compatibility, you might use alternative methods for clearing the console and pausing execution.
Book Quantity Logic: In the book function, if multiple books with the same name exist (though unlikely in a typical library setup, given the "Name" column), the logic might not behave as expected. It assumes Name is unique or that only the first match is relevant.