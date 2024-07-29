# Task 1: Customer Service Ticket Tracker
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket ID {ticket_id} status updated to {status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")


print("Initial Tickets:")
display_tickets()

print("\nOpening a new ticket:")
open_ticket("Ticket003", "Charlie", "Password reset")
display_tickets()

print("\nUpdating ticket status:")
update_ticket_status("Ticket001", "closed")
display_tickets()

print("\nDisplaying only open tickets:")
display_tickets(status="open")