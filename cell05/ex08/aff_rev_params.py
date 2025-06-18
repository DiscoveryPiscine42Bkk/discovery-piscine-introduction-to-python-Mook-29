import sys

def main():
    params = sys.argv[1:]
    if len(params) < 2:
        print("none")
    else:
        # แสดงพารามิเตอร์ย้อนกลับทีละบรรทัด
        for param in reversed(params):
            print(param)
main()