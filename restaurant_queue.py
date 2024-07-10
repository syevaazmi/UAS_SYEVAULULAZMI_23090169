class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if not self.is_empty():
            order = self.queue.pop(0)
            print(f"Pesanan '{order}' telah selesai diproses dan dihapus dari antrian.")
        else:
            print("Antrian kosong. Tidak ada pesanan untuk dihapus.")

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        if not self.is_empty():
            print("Antrian pesanan saat ini:")
            for order in self.queue:
                print(f"- {order}")
        else:
            print("Antrian kosong.")
