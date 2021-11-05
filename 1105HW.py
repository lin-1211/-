num = 0
price = 0
sell = 0
sells = []

print("###########################")
print("###python蘋果店進出貨系統###")
print("###########################")

while True:
    print("功能 =>")
    print("1.設定")
    print("2.進貨")
    print("3.出貨")
    print("4.營業額統計")
    print("5.庫存顯示")
    print("6.離開系統")

    sel = input("輸入欲執行選項:")

    if (sel == "1"):
        print("進入設定功能")
        apple = int(input("有幾顆蘋果?"))
        money = int(input("一顆蘋果多少元?"))
        num = apple
        price = money
        print(f"現在共有{str(num)}顆蘋果。")
        print(f"一顆蘋果{str(price)}元。")

    elif (sel == "2"):
        print("進入進貨功能")
        apple = int(input("請問買了多少蘋果?"))
        num += apple
        print(f"現在共有{str(num)}顆蘋果。")
    elif (sel == "3"):
        print("進入出貨功能")
        apple = int(input("賣了幾顆蘋果?"))
        print(f"應該要付{str(apple * price)}元。")
        sell += apple * price
        sells.append(apple)
    elif (sel == "4"):
        print("進入營業額統計功能")
        for i in range(len(sells)):
            print(f"賣了{str(sells[i])}顆蘋果 共{str(sells[i]*price)}元。")
        print(f"共賺{str(sell)}元。")
    elif (sel == "5"):
        print("進入庫存顯示功能")
        print(f"現有{str(num)}顆蘋果。")
    elif (sel == "6"):
        print("Bye!")
        break 
    

