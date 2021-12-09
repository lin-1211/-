import os.path
contect = ""
dwc = {}

while True:
    print('====================')
    print('*  Word Counter    *')
    print('====================')
    print('(1). 輸入檔案')
    print('(2). 單字統計表')
    print('(3). 查詢檔案中單字')
    print('(4). 替換檔案中單字')
    print('(5). 離開系統')

    sel = input("請輸入執行選項:")

    if sel == "1":
        fn = input("請輸入檔名:")
        if os.path.isfile(fn):
            fo = open(fn,"r")
            contect = fo.read()
            print("檔案內容如下:\n",contect)
        else:
            print("沒有這個檔案!!!")
    elif sel == "2":
        if (contect != ""):
            words = contect.split()
            for word in words:
                if word in dwc:
                    dwc[word] = dwc[word]+1
                else:
                    dwc[word] = 1
            print(dwc)
            print("There are",len(words),"word in the file")
        else:
                print("no contect!")
    elif sel == "3":
            word = input("請輸入要查詢的字:")
            if word in dwc:
                print(word,"在檔案中出現",dwc[word],"次")
            else:
                print("檔案中沒有這個字!!!")
    elif sel == "4":
        old = input("請輸入要被替換的字")
        new = input("請輸入取代的單字:")
        if old in dwc:
            contect = contect.replace(old,new)
        else:
            print("檔案中沒有舊單字:")
        print(contect)
        fo = open(fn,"w")
        fo.write(contect)
        fo.close()
    elif sel == "5":
        break
    else:
        print("輸入錯誤，請重新輸入!")
        




