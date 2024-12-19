import sys

digital = ["social","history","language","literacy"]
bigdata =["bigdata","public","society"]

txt = "".join(sys.stdin.readline().rstrip().split())

for i in digital:
    if i in txt:
        print("digital humanities")
        exit(0)


for i in bigdata:
    if i in txt:
        print("public bigdata")
        exit(0)