# Python Code of Airplane Boarding Management System
# With implementation of Linked List, Doubly Linked List, Stacks , Queues, Singly LinkList
# Conditional statements , classes and functions used


# Passenger class to manage passengers
class Passenger:
    def __init__(self, passenger_id, name, age, seat_number):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.seat_number = seat_number
        self.next = None
        self.prev = None


# Luggage class to manage passengers luggage details

class Luggage:
    def __init__(self, luggage_id, passenger_id):
        self.luggage_id = luggage_id
        self.passenger_id = passenger_id
        self.next = None


# Doubly LinkedList implementation below

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, new_passenger):
        # Insert passenger in sorted order by seat number
        if self.head is None:
            self.head = new_passenger
        else:
            current = self.head
            while current.next and current.seat_number < new_passenger.seat_number:
                current = current.next
            if current.seat_number >= new_passenger.seat_number:
                new_passenger.next = current
                new_passenger.prev = current.prev
                if current.prev:
                    current.prev.next = new_passenger
                else:
                    self.head = new_passenger
                current.prev = new_passenger
            else:
                current.next = new_passenger
                new_passenger.prev = current

    # Remove function to remove passenger from List
    def remove(self, passenger_id):
        current = self.head
        while current:
            if current.passenger_id == passenger_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return current
            current = current.next
        return None

    # Function to display Passengers list with ID, Name and Seat Number
    def display(self):
        current = self.head
        if not current:
            print("No passengers available.")
        else:
            while current:
                print(f"Passenger ID: {current.passenger_id}, Name: {current.name}, Seat Number: {current.seat_number}")
                current = current.next

    # Seat update function
    def update_seat(self, passenger_id, new_seat_number):
        passenger = self.remove(passenger_id)
        if passenger:
            passenger.seat_number = new_seat_number
            self.insert_sorted(passenger)
            return passenger
        return None


# Another Class for implementation of SinglyLinkedList
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Below function for new Luggage
    def append(self, new_luggage):
        if self.head is None:
            self.head = new_luggage
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_luggage

    # function to remove luggage with reference of luggage id
    def remove(self, luggage_id):
        current = self.head
        prev = None
        while current:
            if current.luggage_id == luggage_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current
            prev = current
            current = current.next
        return None

    # Function to display luggage with Passenger ID

    def display(self):
        current = self.head
        if not current:
            print("No luggage available.")
        else:
            while current:
                print(f"Luggage ID: {current.luggage_id}, Passenger ID: {current.passenger_id}")
                current = current.next


# Below is the implementation of Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            for item in reversed(self.stack):
                print(item)

# Below is the implementation of Stack


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            for item in self.queue:
                print(item)

# main class of Boarding System for Lists, stacks, sets and queue


class BoardingSystem:
    def __init__(self):
        self.passenger_list = DoublyLinkedList()  # Sorted by seat number
        self.luggage_list = SinglyLinkedList()  # List of luggage items
        self.boarded_passengers = Queue()  # Queue of boarded passengers
        self.loaded_luggage = Stack()  # Stack of loaded luggage
        self.seat_numbers = set()  # Track assigned seats
        self.passenger_ids = set()  # Track passenger IDs
        self.luggage_ids = set()  # Track luggage IDs

    def add_passenger(self, passenger_id, name, age, seat_number):
        if passenger_id in self.passenger_ids:
            print(f"Error: Passenger ID {passenger_id} is already in use.")
            return
        if seat_number in self.seat_numbers:
            print(f"Error: Seat number {seat_number} is already assigned.")
            return

        # If no duplication, add passenger to the list
        new_passenger = Passenger(passenger_id, name, age, seat_number)
        self.passenger_list.insert_sorted(new_passenger)  # Insert in sorted order (by seat number)

        # Add to tracking sets
        self.passenger_ids.add(passenger_id)
        self.seat_numbers.add(seat_number)
        print(f"Passenger {name} with ID {passenger_id} added successfully.")

    def update_passenger_seat(self, passenger_id, new_seat_number):
        if new_seat_number in self.seat_numbers:
            print(f"Error: Seat number {new_seat_number} is already assigned.")
            return
        passenger = self.passenger_list.update_seat(passenger_id, new_seat_number)
        if passenger:
            self.seat_numbers.discard(passenger.seat_number)
            self.seat_numbers.add(new_seat_number)
            print(f"Seat updated for Passenger ID {passenger_id} to Seat {new_seat_number}.")
        else:
            print(f"Error: Passenger ID {passenger_id} not found.")

    def remove_passenger(self, passenger_id):
        if passenger_id not in self.passenger_ids:
            print(f"Error: Passenger with ID {passenger_id} not found.")
            return

        # Remove passenger from the list
        passenger = self.passenger_list.remove(passenger_id)

        if passenger:
            # Remove from tracking sets
            self.passenger_ids.remove(passenger.passenger_id)
            self.seat_numbers.remove(passenger.seat_number)
            print(f"Passenger {passenger_id} removed successfully.")
        else:
            print(f"Passenger with ID {passenger_id} not found in the list.")

    def add_luggage(self, luggage_id, passenger_id):
        if luggage_id in self.luggage_ids:
            print(f"Error: Luggage ID {luggage_id} is already in use.")
            return
        if passenger_id not in self.passenger_ids:
            print(f"Error: No passenger found with ID {passenger_id}.")
            return

        # If no duplication, add luggage to the list
        new_luggage = Luggage(luggage_id, passenger_id)
        self.luggage_list.append(new_luggage)

        # Add to luggage tracking set
        self.luggage_ids.add(luggage_id)
        print(f"Luggage with ID {luggage_id} added successfully for Passenger {passenger_id}.")

    def remove_luggage(self, luggage_id):
        if luggage_id not in self.luggage_ids:
            print(f"Error: Luggage with ID {luggage_id} not found.")
            return

        # Remove luggage from the list
        luggage = self.luggage_list.remove(luggage_id)

        if luggage:
            # Remove from tracking set
            self.luggage_ids.remove(luggage.luggage_id)
            print(f"Luggage with ID {luggage_id} removed successfully.")
        else:
            print(f"Luggage with ID {luggage_id} not found in the list.")

    def board_passenger(self, passenger_id):
        if passenger_id not in self.passenger_ids:
            print(f"Error: Passenger with ID {passenger_id} not found.")
            return
        self.boarded_passengers.enqueue(passenger_id)
        print(f"Passenger {passenger_id} boarded successfully.")

    def off_load_passenger(self):
        if self.boarded_passengers.is_empty():
            print("No passengers for off-Loading.")
            return
        passenger_id = self.boarded_passengers.dequeue()
        print(f"Passenger {passenger_id} off-Loading successfully.")

    def load_luggage(self, luggage_id):
        if luggage_id not in self.luggage_ids:
            print(f"Error: Luggage with ID {luggage_id} not found.")
            return
        self.loaded_luggage.push(luggage_id)
        print(f"Luggage {luggage_id} loaded successfully.")

    def unload_luggage(self):
        if self.loaded_luggage.is_empty():
            print("No luggage to unload.")
            return
        luggage_id = self.loaded_luggage.pop()
        print(f"Luggage {luggage_id} unloaded successfully.")

    def display_passengers(self):
        print("\nPassenger List (Sorted by Seat Number):")
        self.passenger_list.display()

    def display_luggage(self):
        print("\nLuggage List:")
        self.luggage_list.display()

    def display_boarded_passengers(self):
        print("\nBoarded Passengers (First to Board at the Front):")
        self.boarded_passengers.display()

    def display_loaded_luggage(self):
        print("\nLoaded Luggage (Last Loaded at the Top):")
        self.loaded_luggage.display()


def main():
    system = BoardingSystem()
    # Try-Except Block for handling invalid input
    try:
        while True:
            print("\n \033[1m***✈️***_Airplane Boarding Management System_***✈️***\033[0m ")
            # \033[1m for making text bold and bold ending \033[0m
            print("              \033[1m ==>Passengers<==\033[0m")
            print("──────────────────────────────────────────────────────")
            print("1. Add Passenger ==> 2. Update Passenger Seat ==> 3. Remove Passenger ==> 4. Display Passenger List")
            print("───────────────────────────────────────────────────────────────────────────────────────────────────")
            print("               \033[1m==>Luggage<==\033[0m")
            print("──────────────────────────────────────────────────────")
            print("5. Add Luggage ==> 6. Remove Luggage ==> 7. Display Luggage List ")
            print("────────────────────────────────────────────────────────────────")
            print("               \033[1m==>Boarding<==\033[0m")
            print("──────────────────────────────────────────────────────")
            print("8. Board Passenger ==> 9. off-Load Passenger ==> 10. Display Boarded Passengers ")
            print("───────────────────────────────────────────────────────────────────────────────")
            print("               \033[1m==>Luggage Management<==\033[0m")
            print("──────────────────────────────────────────────────────")
            print("11. Load Luggage ==> 12. off-load Luggage ==> 13. Display Loaded Luggage ")
            print("────────────────────────────────────────────────────────────────────────")

            print("0. Exit")

            choice = int(input("\033[1m Enter a number from above Menu (1-13): \033[0m"))

            if choice == 1:
                passenger_id = int(input("Enter Passenger ID: "))
                name = input("Enter Passenger Name: ")
                age = int(input("Enter Passenger Age: "))
                seat_number = int(input("Enter Seat Number: "))
                if age > 60 and seat_number > 20:
                    print(f"Passenger with age {age} fall in elderly category.Please assign seat between 1-21")
                    seat_number = int(input("\033[1m Enter Seat Number: \033[0m"))
                if age < 60 and seat_number < 21:
                    print("Please assign seat between 20-101.")
                    seat_number = int(input("\033[1m Enter Seat Number: \033[0m"))

                system.add_passenger(passenger_id, name, age, seat_number)

            elif choice == 2:
                passenger_id = int(input("Enter Passenger ID to update seat: "))
                new_seat_number = int(input("Enter new Seat Number: "))
                system.update_passenger_seat(passenger_id, new_seat_number)

            elif choice == 3:
                passenger_id = int(input("Enter Passenger ID to remove: "))
                system.remove_passenger(passenger_id)

            elif choice == 4:
                system.display_passengers()

            elif choice == 5:
                luggage_id = int(input("Enter Luggage ID: "))
                passenger_id = int(input("Enter Passenger ID: "))
                system.add_luggage(luggage_id, passenger_id)

            elif choice == 6:
                luggage_id = int(input("Enter Luggage ID to remove: "))
                system.remove_luggage(luggage_id)

            elif choice == 7:
                system.display_luggage()

            elif choice == 8:
                system.display_passengers()
                passenger_id = int(input("Enter Passenger ID to board: "))
                system.board_passenger(passenger_id)

            elif choice == 9:
                system.off_load_passenger()

            elif choice == 10:
                system.display_boarded_passengers()

            elif choice == 11:
                luggage_id = int(input("Enter Luggage ID to load: "))
                system.load_luggage(luggage_id)

            elif choice == 12:
                system.unload_luggage()

            elif choice == 13:
                system.display_loaded_luggage()

            elif choice == 0:
                print("Thank You!\nYou are exiting from Program now...")
                break

            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")


if __name__ == "__main__":
    main()

