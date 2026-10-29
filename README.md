# Citizen Complaint System

**Module:** PROG211 Object-Oriented Programming 1 | **Domain:** Government | **Standard:** Digital Public Goods (DPG)

A small Python program that lets citizens file complaints about public services (water, roads, sanitation, etc.) and lets officials track each complaint from *Submitted* to *Resolved*.

## Files
| File | Purpose |
|---|---|
| `complaint_system.py` | Classes (`Citizen`, `Complaint`) and record functions |
| `main.py` | Interactive menu (user inputs complaints) and optional demo |
| `sample_output.txt` | Example program output |

## How to run
Requires Python 3.8+ and nothing else (no external libraries).
```
python main.py          # interactive: the user types in complaints
python main.py --demo   # automatic demo with sample data
```

## How it works
The user enters a district, then uses a numbered menu to **file a complaint** (pick a category, type the description), **view** all complaints or filter by status, and **update a status**. **Nothing is saved permanently:** complaints are kept only in a dictionary in memory and are erased when the program closes. No file or database is written.

## OOP concepts used
- **Classes and objects (Task 1):** `Citizen` and `Complaint`, each with attributes and methods. A `Citizen` object creates `Complaint` objects (`citizen.submit_complaint(...)`), showing interaction between objects.
- **Data structure (Task 2):** one **dictionary** `{complaint_id: Complaint}`. Functions `add_complaint()` and `display_complaints()` add and show records. *(Bonus)* **Tuples** are used for fixed data: `CATEGORIES`, `STATUS_FLOW`, and each complaint's status `history`.
- **Methods (Task 3):**
  - Instance: `submit_complaint()`, `update_status()`, `display_info()`
  - Class (`@classmethod`): `Citizen.total_registered()`, `Complaint.total_filed()`, `Complaint.from_text()`
  - Static (`@staticmethod`): `Citizen.generate_reference()`, `Complaint.is_valid_category()`

## How this meets DPG standards
| DPG principle | How the solution meets it |
|---|---|
| **Open source** | Published on GitHub with all source code and this documentation. Uses only the Python standard library. |
| **Inclusive and accessible** | Plain-language prompts and error messages; text-only interface that works on low-spec computers and without internet; clear numbered menu; categories cover everyday services. |
| **Privacy-respecting** | No names, phone numbers, emails or addresses are collected. A citizen is only a random anonymous code (e.g. `CIT-8B591F`) and a district. Complaints are held in memory only and erased on exit. |
| **Modular and reusable** | Logic (`complaint_system.py`) is separate from the interface (`main.py`). Other agencies can reuse the classes or change `CATEGORIES` for their own services. |

## Example usage (sample input/output)
```
=== Citizen Complaint System ===
Your complaints are kept in memory only and are erased when you quit.
No personal details (name, phone, address) are asked for or stored.

Enter your district: 
  Please type something.
Enter your district: Western Area Urban
Your anonymous reference code is CIT-688CBE.

--- Menu ---
  1) File a complaint
  2) View all complaints
  3) View complaints by status
  4) Update a complaint's status
  5) Quit
Choose 1-5: 1

What is the complaint about?
  1) Water
  2) Electricity
  3) Roads
  4) Health Services
  5) Education
  6) Sanitation
  7) Other
Choose 1-7: 1
Describe the problem: 
  Please type something.
Describe the problem: No running water in our ward for 5 days.
Saved complaint CMP-0001.
Thank you. Your complaint ID is CMP-0001.

--- Menu ---
  1) File a complaint
  2) View all complaints
```
See `sample_output.txt` for the full session.

## Author
Student: _Abibatu Bintu Jabbie and ID_ | Lecturer: Julius Lagah
