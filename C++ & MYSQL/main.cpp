#include <bits/stdc++.h> 
#include <iostream> 
#include <mysql.h> 
#include <mysqld_error.h> 
#include <windows.h> 
#include <sstream> 
#include <cstdlib> 
using namespace std; 
const char* HOST = "localhost"; 
const char* USER = "root"; 
const char* PW = "Vibhor123#"; 
const char* DB = "Manage"; 
// Class definition for Student 
class Student{ 
private: 
string Id; 
string Name; 
string No; 
public: 
Student() : Id(""), Name(""), No("") {} 
// Setter functions for Student attributes 
void setId(string id) { 
Id = id; 
} 
void setName(string name) 
{ 
Name=name;
} 
void setNo(string no) 
{ 
No=no; 
} 
// Getter functions for Student attributes 
string getName() 
{ 
return Name; 
} 
string getNo() 
{ 
return No; 
} 
string getId() { 
return Id; 
} 
}; 
// Class definition for Library 
class Library{ 
private: 
string Name; 
int Quantity; 
public: 
Library() : Name(""), Quantity(0) {} 
// Setter functions for Library attributes 
void setName(string name) { 
Name = name; 
} 
void setQuantity(int quantity) { 
Quantity = quantity; 
} 
// Getter functions for Library attributes 
int getQuantity() { 
return Quantity; 
} 
string getName() { 
return Name;
} 
}; 
// Function for administration tasks 
void admin(MYSQL* conn, Library l, Student s){ 
bool closed = false; 
while(!closed){ 
int choice; 
cout << "1. Add Book." << endl; 
cout << "2. Add Student." << endl; 
cout << "0. Exit." << endl; 
cout << "Enter Choice: "; 
cin >> choice; 
if(choice==1){ 
system("cls"); 
string name; 
int quantity; 
cout<<"Enter the name of the book: "; 
cin>>name; 
l.setName(name); 
cout<<"Enter the Quantity of the book: "; 
cin>>quantity; 
l.setQuantity(quantity); 
int Iq = l.getQuantity(); 
stringstream ss; 
ss<<Iq; 
string Sq = ss.str(); 
// Insert book into the database 
string book = "INSERT INTO library (Name,Quantity) VALUES('"+l.getName()+"', 
'"+Sq+"') "; 
if(mysql_query(conn,book.c_str())){ 
cout<<"Error: "<<mysql_error(conn)<<endl; 
} 
else{ 
cout<<"Book is Inserted Successfully"<<endl; 
} 
}
else if(choice==2){ 
system("cls"); 
string id; 
string name; 
string no; 
cout << "Enter the ID of Student: "; 
cin >> id; 
s.setId(id); 
cout<<"Enter the name of the Student"; 
cin>>name; 
s.setName(name); 
cout<<"Enter the number of the Student: "; 
cin>>no; 
s.setNo(no); 
// Insert student into the database 
string st = "INSERT INTO student (Id,Student_Name,Student_Number) VALUES('" 
+ s.getId() + "','"+s.getName()+"','"+s.getNo()+"')"; 
if (mysql_query(conn, st.c_str())) { 
cout << "Error: " << mysql_error(conn) << endl; 
} 
else { 
cout << "Student Inserted Successfully" << endl;  
} 
} 
else if(choice ==0){ 
closed = true; 
cout<<"System is closing"<<endl; 
} 
} 
Sleep(3000); 
} 
// Function to display available books 
void display(MYSQL* conn){ 
system("cls"); 
cout<<"Available Books"<<endl; 
cout<<"***************"<<endl; 
string disp= "SELECT * FROM library"; 
if (mysql_query(conn, disp.c_str())) { 
cout << "Error: " << mysql_error(conn) << endl; 
}
else{ 
MYSQL_RES* res; 
res= mysql_store_result(conn); 
if(res){ 
int num= mysql_num_fields(res); 
MYSQL_ROW row; 
while(row=mysql_fetch_row(res)){ 
for(int i=0; i< num; i++){ 
cout<<" "<<row[i]; 
} 
cout<<endl; 
} 
mysql_free_result(res); 
} 
} 
} 
// Function to check if a book exists in the library 
int book(MYSQL* conn, string Bname){ 
string exist = "SELECT Name, Quantity FROM library WHERE Name = '" + Bname 
+ "'"; 
if (mysql_query(conn, exist.c_str())) { 
cout << "Error: " << mysql_error(conn) << endl; 
} 
else{ 
MYSQL_RES* res; 
res = mysql_store_result(conn); 
if(res){ 
int num = mysql_num_fields(res); 
MYSQL_ROW row; 
while(row=mysql_fetch_row(res)){ 
for(int i=0; i< num; i++){ 
if(Bname == row[i]){ 
int quantity = atoi(row[i+1]); 
return quantity;  
} 
else{ 
cout<<"Book Not Found."<<endl; 
} 
} 
}  
mysql_free_result(res); 
} 
}//else if exist 
return 0; 
Sleep(5000); 
} 
// Function for user actions 
void user(MYSQL* conn, Library l, Student s){ 
system("cls"); 
display(conn); 
string Sid; 
cout<<"Enter Your ID: "; 
cin>>Sid; 
string com = "SELECT * FROM student WHERE Id = '"+Sid+"'"; 
if (mysql_query(conn, com.c_str())) { 
cout << "Error: " << mysql_error(conn) << endl; 
} 
else{ 
MYSQL_RES* res; 
res=mysql_store_result(conn); 
if(res){ 
int num= mysql_num_rows(res); 
if(num==1){ 
cout<<"Student ID Found."<<endl; 
string Bname; 
cout<<"Enter Book Name: "; 
cin>>Bname; 
if(book(conn,Bname) > 0){ 
int bookQuantity = book(conn,Bname)-1; 
stringstream ss; 
ss<<bookQuantity; 
string Sq = ss.str(); 
string upd ="UPDATE library SET Quantity ='"+Sq+"' WHERE Name = '"+Bname+"' 
"; 
if(mysql_query(conn,upd.c_str())){ 
cout<<"Error: "<<mysql_error(conn)<<endl; 
} 
else{ 
cout<<"Book is available. Borrowing Book...."<<endl; 
} 
}
else{ 
cout<<"Book is not Available."<<endl; 
} 
} 
else if(num==0){ 
cout<<"This Student is Not Registered."<<endl; 
} 
} 
mysql_free_result(res); 
}  
} 
// Main function 
int main() { 
Student s; 
Library l; 
MYSQL* conn; 
conn = mysql_init(NULL); 
if(!mysql_real_connect(conn,HOST, USER, PW,DB,3306,NULL,0)){ 
cout<<"Error: "<<mysql_error(conn)<<endl; 
} 
else{ 
cout<<"Logged In!"<<endl; 
} 
Sleep(3000); 
bool exit = false; 
while(!exit){ 
system("cls"); 
int val; 
cout << "Welcome To Library Management System" << endl; 
cout << "************************************" << endl; 
cout << "1. Administration." << endl; 
cout << "2. User." << endl; 
cout<< "0. Exit." << endl; 
cout<<"Enter Choice: "; 
cin>>val; 
if(val==1){ 
system("cls"); 
admin(conn,l,s);  
}
else if(val==2){ 
user(conn,l,s); 
Sleep(5000);  
} 
else if(val==0){ 
exit= true; 
cout<<"Good Luck!"<<endl; 
Sleep(3000); 
} 
} 
mysql_close(conn); 
return 0; 
}
