class Order:
    def __init__(self, order_id, bake_time):
        self.id = order_id
        self.bake = bake_time
        self.wait = self.turn = self.done = 0

def main():
    n = int(input("Enter the number of cake orders: "))
    orders = [Order(i + 1, int(input(f"Enter Baking Time for Cake Order {i + 1}: "))) for i in range(n)]

    orders.sort(key=lambda x: x.bake)
    current_time = 0

    for order in orders:
        order.wait = current_time
        order.turn = order.wait + order.bake
        order.done = current_time + order.bake
        current_time += order.bake

    print("\nOrder ID\tBaking Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for order in orders:
        print(f"{order.id}\t\t{order.bake}\t\t{order.wait}\t\t{order.turn}\t\t{order.done}")

if __name__ == "__main__":
    main()
