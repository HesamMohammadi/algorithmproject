# Request Management System 

## 📌 Overview

The **Request Management System** is a console-based C++ application for managing user requests using two main data structures:

- **Binary Search Tree (BST)** — for storing and searching requests by ID and name.
- **Max Heap** — for organizing requests by priority and processing the highest-priority request first.

This design keeps data storage (BST) and priority management (Heap) efficient and well-separated.

---

## ⚙️ Technologies

- **Language:** C++
- **IDE:** Visual Studio 2012
- **Libraries:** `<iostream>`, `<string>`, `<vector>`

---

## 🚀 Features

| Feature                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| Insert Request            | Add a new request with ID, name, and priority                |
| Delete Request            | Remove a request using its ID                                |
| Search                    | Find a request using the BST                                 |
| Process Highest Priority  | Retrieve and remove the highest-priority request             |
| Increase Priority         | Update the priority of an existing request in the heap       |
| Print BST                 | Show all requests using pre-order traversal                  |
| Print Heap                | Show requests by level order (by priority)                   |
| Size & Empty Check        | Show number of requests and check if BST/Heap is empty       |

---

## 🧠 Data Structures

### Binary Search Tree (BST)

- Stores **(ID, Name)** pairs
- Fast insert, search, and delete by ID
- Pre-order traversal used for display

### Max Heap

- Manages **(ID, Priority)** pairs
- Always keeps the highest priority request at the root
- Supports:
  - Insert with automatic adjustment
  - Delete by ID
  - Increase priority only

> **Note:** The heap does not store request names — it only tracks priorities.

---

## 🛠 How to Run

1. Open the project in **Visual Studio 2012**
2. Make sure the compiler supports **C++11** or higher
3. Build and run the project
4. Use the interactive menu to manage requests

---

## 📋 Menu Options

- Insert
- Delete
- Search
- Process Highest Priority
- Increase Priority
- Print BST
- Print Heap
- Size Info
- Empty Check
- Exit
