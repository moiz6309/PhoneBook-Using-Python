# Phonebook Application 📱

This repository contains a **Phonebook Application** built using **Python** and **Tkinter**. The application allows users to add, search, and store contact details (name and phone number). The data is saved to a file for persistent storage, and users can search contacts by either name or phone number.

---

## 🚀 Features

- **Add Contact**: Add new contacts with name and phone number.  
- **Search Contact**: Search for contacts by name or phone number.  
- **Persistent Storage**: Contacts are saved in a text file (`phonebook1.txt`) for persistence.  
- **Data Validation**: Ensures that all contact entries are valid and properly formatted.  

---

## 🛠️ Technologies Used

- **Programming Language**: Python  
- **GUI Framework**: Tkinter  
- **File Handling**: Store phonebook data in a text file (`phonebook1.txt`)  

---

## 📂 Project Structure

```plaintext
PhoneBook-Using-Python/
├── phonebook1.txt        # File that stores phonebook data
├── phonebook_app.py      # Main Python program for the phonebook application
├── README.md             # Project documentation
```
## 📖 How to Use
-**Add Contact**:

Enter the name and phone number in the "Add Contact" section and click "Add Contact".
The contact will be saved to phonebook1.txt.
- **Search Contact**:

Enter either a name or phone number in the "Search Contact" section and click "Search".
The result will display the contact’s details (if found).
## 📝 Example Usage
Adding a Contact
Input:
```plaintext

Name: John Doe
Phone: 123-456-7890
```
Output:
```plaintext
Contact 'John Doe' added successfully!
```
Searching for a Contact
Input:
```plaintext
   John Doe
```
Output:
```plaintext
Name: John Doe
Phone: 123-456-7890
```
## 🚧 Limitations
- **No Update or Delete Functionality**: Currently, you can only add and search contacts. There is no functionality to update or delete contacts.
- **Basic Validation**: The program currently only checks for empty fields but could be improved with more advanced validation for phone numbers.
## 🚀 Future Enhancements
- **Update/Delete Contact**: Add functionality to update or delete contacts.
- **Advanced Validation**: Implement better validation for phone numbers and names.
