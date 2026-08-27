"""
Problem 5: Simulation of Service Desk Queuing Problem
Linked Queue Implementation - Bank Teller Simulation
"""
import random


class Customer:
    """Represents a customer with arrival time and service time."""
    def __init__(self, arrival, service):
        self.arrival_time = arrival
        self.service_time = service


class QNode:
    """Node of the linked queue."""
    def __init__(self, customer):
        self.data = customer
        self.next = None


class LinkedQueue:
    """Linked queue with front and rear pointers."""
    def __init__(self):
        # Dummy head node
        self.front = QNode(None)
        self.rear = self.front

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, customer):
        """Enqueue a customer at the rear."""
        new_node = QNode(customer)
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        """Dequeue a customer from the front."""
        if self.is_empty():
            raise IndexError("Queue is empty.")
        node = self.front.next
        self.front.next = node.next
        if self.front.next is None:
            self.rear = self.front
        return node.data


def simulate_from_data(customers):
    """
    Simulate the bank teller service using a linked queue.
    customers: list of Customer objects sorted by arrival time.
    Returns (total_idle_time, average_waiting_time, total_customers).
    """
    queue = LinkedQueue()
    clock = 0
    total_idle = 0
    total_wait = 0
    total_customers = 0
    idx = 0  # Index into customers list

    # Read first customer
    if not customers:
        return 0, 0, 0

    temp = customers[idx]
    idx += 1

    while True:
        # If queue is empty and there are remaining customers
        if queue.is_empty():
            if temp is None:
                break
            # Teller is idle until next customer arrives
            if clock < temp.arrival_time:
                total_idle += temp.arrival_time - clock
            clock = temp.arrival_time
            queue.enqueue(temp)
            # Read next customer
            temp = customers[idx] if idx < len(customers) else None
            idx += 1

        # Dequeue one customer and serve
        customer = queue.dequeue()
        total_customers += 1

        # Customer's waiting time = current clock - arrival time
        wait = max(0, clock - customer.arrival_time)
        total_wait += wait

        # Service end time
        service_end = clock + customer.service_time

        # Enqueue all customers arriving before service_end
        while temp is not None and temp.arrival_time < service_end:
            queue.enqueue(temp)
            temp = customers[idx] if idx < len(customers) else None
            idx += 1

        clock = service_end

        # If queue is now empty and no more customers, done
        if queue.is_empty() and temp is None:
            break

    avg_wait = total_wait / total_customers if total_customers > 0 else 0
    return total_idle, avg_wait, total_customers


def simulate_random(duration=100, max_service=10):
    """
    Generate random customer data and simulate.
    duration: simulation period
    max_service: maximum service time
    """
    customers = []
    t = 0
    cid = 1
    while t < duration:
        inter_arrival = random.randint(1, 8)
        t += inter_arrival
        if t >= duration:
            break
        service = random.randint(1, max_service)
        customers.append(Customer(t, service))
        cid += 1
    return customers


def load_from_string(data_str):
    """
    Load customer data from a comma-separated string.
    Format: arrival1, service1, arrival2, service2, ...
    """
    values = [int(x.strip()) for x in data_str.split(',')]
    customers = []
    for i in range(0, len(values) - 1, 2):
        customers.append(Customer(values[i], values[i + 1]))
    customers.sort(key=lambda c: c.arrival_time)
    return customers


def main():
    print("=== Bank Service Desk Queuing Simulation ===\n")

    # Test 1: Example data from the problem statement
    print("--- Test 1: Sample Data (10, 6, 13, 8) ---")
    customers1 = load_from_string("10, 6, 13, 8")
    print(f"{'Customer':>10} | {'Arrival':>8} | {'Service':>8}")
    print("-" * 34)
    for i, c in enumerate(customers1):
        print(f"{i+1:>10} | {c.arrival_time:>8} | {c.service_time:>8}")
    idle, avg_wait, total = simulate_from_data(customers1)
    print(f"\nTotal customers:       {total}")
    print(f"Total teller idle time: {idle} units")
    print(f"Average waiting time:   {avg_wait:.2f} units\n")

    # Test 2: More customers
    print("--- Test 2: Extended Sample Data ---")
    customers2 = load_from_string("1, 4, 3, 2, 5, 7, 9, 3, 12, 5, 15, 6")
    print(f"{'Customer':>10} | {'Arrival':>8} | {'Service':>8}")
    print("-" * 34)
    for i, c in enumerate(customers2):
        print(f"{i+1:>10} | {c.arrival_time:>8} | {c.service_time:>8}")
    idle, avg_wait, total = simulate_from_data(customers2)
    print(f"\nTotal customers:       {total}")
    print(f"Total teller idle time: {idle} units")
    print(f"Average waiting time:   {avg_wait:.2f} units\n")

    # Test 3: Random simulation
    print("--- Test 3: Random Simulation (100 time units) ---")
    random.seed(42)
    customers3 = simulate_random(duration=100, max_service=8)
    print(f"Generated {len(customers3)} customers randomly.")
    idle, avg_wait, total = simulate_from_data(customers3)
    print(f"Total customers:       {total}")
    print(f"Total teller idle time: {idle} units")
    print(f"Average waiting time:   {avg_wait:.2f} units")


if __name__ == "__main__":
    main()
