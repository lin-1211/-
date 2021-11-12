data = {"A001":["小熊軟糖",20],"A002":["冰棒",25],"A004":["王子麵",10],"A006":["汽水",25]}
num = input("請輸入貨號:")
if num not in data:
    print(f"貨號:{num}不存在")
    new = input("是否新增商品?(y or n)")
    if new == "y":
        name = input("輸入品項:")
        money = int(input("輸入售價:"))
        data[num] = [name,money]
        d = data[num]
        print(f"貨號:{num}品項:{d[0]}價格:{d[1]}元。")
    else:
        print(f"品項:{data[num][0]}價格:{data[num][1]}元。")
