class Book:
    def __init__(self, title, author, year_published): # title คือ argument 
        self.title = title
        self.author = author
        self.year_published = year_published
    # def __init__(self, title, author, year_published): คือ เมธอดตัวสร้าง (Constructor) ที่ใช้ในการกำหนดค่าเริ่มต้นให้กับวัตถุ (Object) ของคลาส Bookเร
    
    def get_summary(self):
        # self: ตัวแทนของวัตถุที่ถูกสร้างขึ้นจากคลาส Book เช่น book1, book2, book3
        return f"'{self.title}' by {self.author}, published in {self.year_published}."
        # self.title: การเข้าถึงคุณสมบัติ title ของวัตถุปัจจุบัน นั่นคือ ชื่อหนังสือ
book1 = Book("จุลสารความมั่นคง", "สุรชาติ บำรุงสุข ", 2020)
print(book1.get_summary())

book2 = Book("การเมืองในประเทศไทย", "สมชาย แสวงการ", 2018)
print(book2.get_summary())

book3 = Book("เศรษฐศาสตร์เบื้องต้น", "วิชัย ศรีวัฒนประภา", 2019)
print(book3.get_summary())

# สรุป : โค้ดนี้สร้างคลาส Book ที่มีคุณสมบัติ title, author, year_published และเมธอด get_summary() เพื่อแสดงข้อมูลหนังสือในรูปแบบที่อ่านง่าย โดยสร้างวัตถุ book1, book2, book3 จากคลาส Book และเรียกใช้เมธอด get_summary() เพื่อแสดงข้อมูลของแต่ละหนังสือ
# attribute: คุณสมบัติของวัตถุ (Object) ที่ถูกสร้างขึ้นจากคลาส (Class) เช่น title, author, year_published
    # self.author: การเข้าถึงคุณสมบัติ author ของวัตถุปัจจุบัน นั่นคือ ชื่อผู้เขียน
    # self.year_published: การเข้าถึงคุณสมบัติ year_published ของวัตถุปัจจุบัน นั่นคือ ปีที่ตีพิมพ์    
# self: ตัวแทนของวัตถุที่ถูกสร้างขึ้นจากคลาส Book เช่น book1, book2, book3

    # def get_summary(self): คือ เมธอดที่ใช้ในการดึงข้อมูลสรุปของหนังสือในรูปแบบที่อ่านง่าย


