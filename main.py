"""
main.py - Interactive Citizen Complaint System.

Run:  python main.py          (citizen types in complaints)
      python main.py --demo   (automatic demo with sample data)

Privacy note: complaints live ONLY in memory (a dictionary). Nothing is
written to a file or database, so everything is erased when the program closes.
"""

import sys
from complaint_system import (Citizen, Complaint, CATEGORIES, STATUS_FLOW,
                              add_complaint, display_complaints)


# ---------- helpers for safe, friendly input ----------

def ask_text(prompt):
    """Keep asking until the user types something."""
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("  Please type something.")


def ask_choice(title, options):
    """Show a numbered list and return the option the user picked."""
    if title:
        print(title)
    for number, option in enumerate(options, start=1):
        print(f"  {number}) {option}")
    while True:
        answer = input(f"Choose 1-{len(options)}: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"  Please enter a number from 1 to {len(options)}.")


# ---------- menu actions ----------

def file_complaint(registry, citizen):
    category = ask_choice("\nWhat is the complaint about?", CATEGORIES)
    description = ask_text("Describe the problem: ")
    complaint = citizen.submit_complaint(category, description)
    add_complaint(registry, complaint)
    print(f"Thank you. Your complaint ID is {complaint.complaint_id}.")


def update_complaint(registry):
    if not registry:
        print("There are no complaints to update.")
        return
    complaint_id = ask_text("Complaint ID (e.g. CMP-0001): ").upper()
    if complaint_id not in registry:
        print("Complaint not found.")
        return
    complaint = registry[complaint_id]
    print(f"Current status: {complaint.status}")
    new_status = ask_choice("Choose the new status:", STATUS_FLOW)
    note = input("Add a short note (optional): ").strip()
    try:
        complaint.update_status(new_status, note)
        print(f"{complaint_id} is now '{complaint.status}'.")
    except ValueError as error:
        print("Error:", error)


def interactive():
    registry = {}  # the single data structure: a dictionary (in memory only)
    print("=== Citizen Complaint System ===")
    print("Your complaints are kept in memory only and are erased when you quit.")
    print("No personal details (name, phone, address) are asked for or stored.\n")

    citizen = Citizen(ask_text("Enter your district: "))
    print(f"Your anonymous reference code is {citizen.citizen_ref}.")

    while True:
        print("\n--- Menu ---")
        choice = ask_choice("", ("File a complaint", "View all complaints",
                                 "View complaints by status",
                                 "Update a complaint's status", "Quit"))
        if choice == "File a complaint":
            file_complaint(registry, citizen)
        elif choice == "View all complaints":
            print()
            display_complaints(registry)
        elif choice == "View complaints by status":
            display_complaints(registry, ask_choice("\nWhich status?", STATUS_FLOW))
        elif choice == "Update a complaint's status":
            update_complaint(registry)
        else:
            print("Goodbye. All complaints have been erased from memory.")
            break


# ---------- automatic demo ----------

def demo():
    registry = {}
    c1, c2 = Citizen("Western Area Urban"), Citizen("Bo")
    add_complaint(registry, c1.submit_complaint("Water", "No running water for 5 days."))
    add_complaint(registry, c2.submit_complaint("Roads", "Large potholes near the market."))
    add_complaint(registry, Complaint.from_text(c1, "Sanitation: Drain blocked near the school."))
    registry["CMP-0001"].update_status("Under Review", "Assigned to Water Dept.")
    display_complaints(registry)
    print("Citizens:", Citizen.total_registered(), "| Complaints:", Complaint.total_filed())


if __name__ == "__main__":
    demo() if "--demo" in sys.argv else interactive()
