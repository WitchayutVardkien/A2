# โปรแกรมจองคิวร้านอาหาร

FILE_NAME = "queue.txt"
ZONES = ["A", "B", "C"]      # A= 1-2 คน,B= 3-4 คน,C= 5 คนขึ้นไป

class QueueItem:
    def __init__(self, queue_no, name, phone, amount):
        self.queue_no = queue_no
        self.name = name
        self.phone = phone
        self.amount = amount

    def to_text(self):
        return f"{self.queue_no}|{self.name}|{self.phone}|{self.amount}"

    def show(self):
        print(f"Queue: {self.queue_no} | Name: {self.name} | Call: {self.phone} | Amount: {self.amount}")


class SmallQueue(QueueItem):     
    def __init__(self, no, name, phone, amount):
        super().__init__("A" + str(no), name, phone, amount)


class MediumQueue(QueueItem):   
    def __init__(self, no, name, phone, amount):
        super().__init__("B" + str(no), name, phone, amount)


class LargeQueue(QueueItem):     
    def __init__(self, no, name, phone, amount):
        super().__init__("C" + str(no), name, phone, amount)


queues = [[], [], []]   # แถว 0= หมวด A, 1= หมวด B, 2= หมวด C
count = [1, 1, 1]       # เลขคิวถัดไปของแต่ละหมวด


def get_zone(amount):
    if amount <= 2:
        return 0
    elif amount <= 4:
        return 1
    else:
        return 2


def create_queue(zone, no, name, phone, amount):
    if zone == 0:
        return SmallQueue(no, name, phone, amount)
    elif zone == 1:
        return MediumQueue(no, name, phone, amount)
    else:
        return LargeQueue(no, name, phone, amount)

def save_file():
    """เขียนคิวทั้งหมดลงไฟล์"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for row in queues:
            for q in row:
                f.write(q.to_text() + "\n")


def load_file():
    """อ่านคิวจากไฟล์ตอนเปิดโปรแกรม แล้วรันคิวต่อ"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return                     

    for line in lines:
        data = line.strip().split("|")
        if len(data) != 4 or data[0][0] not in ZONES:
            continue                
        zone = ZONES.index(data[0][0])      #A=0, B=1, C=2
        no = int(data[0][1:])               #A12=12
        queues[zone].append(create_queue(zone, no, data[1], data[2], int(data[3])))
        if no >= count[zone]:
            count[zone] = no + 1            #กันเลขคิวซ้ำ


def input_int(m):
    """รับตัวเลข ถ้าพิมพ์ผิดให้กรอกใหม่"""
    while True:
        try:
            return int(input(m))
        except ValueError:
            print("*** Please enter a number ***")