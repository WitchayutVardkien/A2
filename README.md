# Restaurant Queue 🍲 โปรแกรมจองคิวร้านอาหาร

งาน A2 วิชา Computer Programming (010123138)

**ผู้จัดทำ:** ชื่อ วิชยุตม์ วาดเขียน รหัส 6901012610218

---

## ฟีเจอร์

- **[1] New Queue:** รับคิวใหม่ จัดหมวดหมู่อัตโนมัติและรันเลขคิวตามจำนวนลูกค้า
  - หมวด A (Small Queue): สำหรับ 1–2 คน
  - หมวด B (Medium Queue): สำหรับ 3–4 คน
  - หมวด C (Large Queue): สำหรับ 5 คนขึ้นไป
- **[2] Next Queue:** เรียกคิวถัดไปออกมารับบริการ พร้อมอัปเดตไฟล์ข้อมูลอัตโนมัติ
- **[3] All Queue:** แสดงรายการคิวทั้งหมดที่กำลังรออยู่ในระบบ
- **[4] Cancel Queue:** ระบุหมายเลขคิวเพื่อยกเลิกคิวเฉพาะราย
- **[0] Exit:** ออกจากโปรแกรม (ข้อมูลถูกบันทึกไว้ในไฟล์แล้ว)
- **Auto Sync System:** อ่านไฟล์คิวล่าสุดตอนเปิดโปรแกรม เพื่อรันเลขคิวต่อให้อัตโนมัติ ป้องกันปัญหาเลขคิวซ้ำ

## วิธีใช้งาน

ใช้ Python 3.x.x+ ไม่ต้องติดตั้ง library เพิ่ม
ดาวน์โหลดโปรแกรม ดาวน์โหลดไฟล์โค้ด หรือดาวน์โหลดไฟล์ ZIP จาก Releases
การรันโปรแกรม:

## โครงสร้างไฟล์

```
├── restaurant_queue.py   # โค้ดหลัก
├── queue.txt             # ไฟล์เก็บคิว รูปแบบ QueueNo|name|phone|amount
├── flowchart            # รูป flowchart 3 ฟังก์ชัน(ยังไม่มี)
└── README.md
```

## ตัวอย่างการใช้งาน

```
=====Menu=====
[1] New Queue
[2] Next Queue
[3] All Queue
[4] Cancel Queue
[0] Exit
number: 1
==============
name: ต้น
phone: 0811111111
amount: 2
Queue NO: A1
```

## ลิงก์

- รายงานความคืบหน้า A2: https://docs.google.com/document/d/1z59LIuZ0Jv7cYOSEoe2weUxTGK-OC0tnAwr28qyJ0bo/edit?usp=sharing
- วิดีโอ Demo: -
