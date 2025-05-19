# Request Management System | سامانه مدیریت درخواست‌ها

---

English Description

Overview
The <Request Management System> is a simple console-based application written in C++. It manages user requests using two data structures:

- Binary Search Tree (BST) for storing and searching requests by ID and name.
- Max Heap for organizing requests by priority and processing the highest priority first.

This design separates data storage (BST) and priority queue management (Heap) for efficient retrieval and processing.

Technologies
- Language: C++
- IDE Compatibility: Visual Studio 2012
- Libraries Used: `<iostream>`, `<string>`, `<vector>`

---

Features

| Feature | Description |
|--------|-------------|
| **Insert Request** | Add a new request with an ID, name, and priority |
| **Delete Request** | Remove a request using its ID |
| **Search** | Search for a request using the BST |
| **Process Highest Priority** | Remove and return the request with the highest priority |
| **Increase Priority** | Update the priority of a request in the heap |
| **Print BST** | Pre-order traversal of all stored requests |
| **Print Heap** | Level-order display of requests by priority |
| **Size & Empty Check** | Show number of requests and empty status of BST and heap |

---

Data Structures

Binary Search Tree (BST)
- Stores `(ID, Name)` pairs.
- Enables fast **search**, **insert**, and **delete** by ID.
- Pre-order traversal is used for display.

Max Heap
- Manages `(ID, Priority)` pairs.
- Highest priority request is always at the root.
- Supports:
  - Insert with automatic heap-up adjustment
  - Delete by ID
  - Update priority (only increase supported)

 Note: The heap does **not** store request names. It only manages priorities.

---

How to Run

1. Open the project in **Visual Studio 2012**
2. Make sure the compiler supports C++11 (minimum)
3. Build and run the project
4. Use the interactive menu to perform actions

The menu

Insert

Delete

Search

Highest priority

Increase priority

Print BST

Print Heap

Size info

Empty check

Exit