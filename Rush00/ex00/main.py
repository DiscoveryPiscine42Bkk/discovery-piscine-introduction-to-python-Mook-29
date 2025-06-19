import json
import os
from datetime import datetime

tasks = []

def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def main_menu():
    print("\n====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. แก้ไขงาน")
    print("6. ค้นหางาน")
    print("7. ออกจากโปรแกรม")

def main():
    load_tasks()
    while True:
        main_menu()
        choice = input("เลือกเมนู (1-7): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            search_task()
        elif choice == '7':
            save_tasks()
            print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

def add_task():
    task_name = input("ป้อนชื่องาน: ")
    task_date = input("ป้อนวันที่ (dd/mm/yyyy): ")
    task_type = input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ")
    
    tasks.append({"name": task_name, "date": task_date, "type": task_type})
    print("✅ เพิ่มงานสำเร็จ")

def display_tasks():
    if not tasks:
        print("❗ ยังไม่มีงานในรายการ")
        return
    
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["date"], "%d/%m/%Y"))
    
    print("📋 รายการงานทั้งหมด:")
    for i, task in enumerate(sorted_tasks):
        print(f"{i + 1}. {task['date']} - {task['name']} ({task['type']})")

def delete_task():
    if not tasks:
        print("❗ ยังไม่มีงานในรายการ")
        return
    
    display_tasks()
    try:
        task_number = int(input("ลำดับของงานที่ต้องการลบ: ")) - 1
        if 0 <= task_number < len(tasks):
            confirm = input(f"ยืนยันลบงาน '{tasks[task_number]['name']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = tasks.pop(task_number)
                print(f"🗑️ ลบงาน: {deleted['name']} แล้ว")
        else:
            print("❌ ไม่พบงานตามลำดับที่ระบุ")
    except ValueError:
        print("❌ กรุณาป้อนตัวเลขสำหรับลำดับงาน")

def summarize_tasks():
    if not tasks:
        print("❗ ยังไม่มีงานในรายการ")
        return

    summary = {}
    for task in tasks:
        summary[task['type']] = summary.get(task['type'], 0) + 1

    print("\n📊 สรุปจำนวนงานแต่ละประเภท:")
    for ttype, count in summary.items():
        print(f"- {ttype}: {count} งาน")

def edit_task():
    if not tasks:
        print("❗ ยังไม่มีงานในรายการ")
        return
    
    display_tasks()
    try:
        task_number = int(input("ลำดับของงานที่ต้องการแก้ไข: ")) - 1
        if 0 <= task_number < len(tasks):
            task = tasks[task_number]
            print(f"🔧 แก้ไขงานเดิม: {task['name']} ({task['type']}) วันที่ {task['date']}")
            task['name'] = input("ชื่องานใหม่ (เว้นว่างหากไม่เปลี่ยน): ") or task['name']
            task['date'] = input("วันที่ใหม่ (dd/mm/yyyy) (เว้นว่างหากไม่เปลี่ยน): ") or task['date']
            task['type'] = input("ประเภทใหม่ (เว้นว่างหากไม่เปลี่ยน): ") or task['type']
            print("✅ แก้ไขงานเรียบร้อยแล้ว")
        else:
            print("❌ ไม่พบงานตามลำดับที่ระบุ")
    except ValueError:
        print("❌ กรุณาป้อนตัวเลขสำหรับลำดับงาน")

def search_task():
    if not tasks:
        print("❗ ยังไม่มีงานในรายการ")
        return
    
    criteria = input("ค้นหาตาม (type/date): ").lower()
    keyword = input("ป้อนคำค้นหา: ")
    
    results = []
    for task in tasks:
        if criteria == "type" and keyword.lower() in task['type'].lower():
            results.append(task)
        elif criteria == "date" and keyword == task['date']:
            results.append(task)

    if results:
        print("🔍 ผลการค้นหา:")
        for i, task in enumerate(results):
            print(f"{i + 1}. {task['date']} - {task['name']} ({task['type']})")
    else:
        print("❌ ไม่พบงานที่ตรงกับการค้นหา")

if __name__ == "__main__":
    main()