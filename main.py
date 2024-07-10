from restaurant_queue import RestaurantQueue

def main():
    queue = RestaurantQueue()

    queue.enqueue("Nasi Goreng")
    queue.enqueue("Sate Ayam")
    queue.enqueue("Es Teh")

    queue.display_queue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue() 

if __name__ == "__main__":
    main()
