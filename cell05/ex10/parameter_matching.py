import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    param = sys.argv[1]
    # รับ input จากผู้ใช้
    answer = input("What was the parameter? ")

    if answer == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
main()