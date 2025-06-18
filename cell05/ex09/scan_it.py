import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)
main()