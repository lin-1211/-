# 用來裝 英文:中文翻譯 對應關係的字典
vocabularies = {'apple':'蘋果'}
#stage 2
print('############################')
print('#####歡迎進入英文高手系統######')
print('############################')
print('*** 使用本系統，你將成為英文高手!!! ***')

while True:
    print('=>')
    print('1. 建立辭彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')

    if sel=='1':
        print('1. 建立辭彙')
        word = input('請輸入單字:')
        if(word == '0'):
            continue
        else:
            chinese = input('請輸入中文翻譯:')
            vocabularies[word] = chinese
    elif sel=='2':
        print('2. 列出所有單字')
        for k in vocabularies.keys():
            print(f"{k} 的意思是 {vocabularies[k]}")
    elif sel=='3': # 英翻中
        print('3. 英翻中')
        word = input('請輸入單字:')
        if word in vocabularies.keys():
            print(f"{word} 的意思是 {vocabularies[word]}")
        else:
            print('查無此單字')
    elif sel=='4': # 中翻英
        print('4. 中翻英')
        chinese = input('請輸入中文:')
        for k,v in vocabularies.items():
            if(v == chinese):
              None
            #腦袋秀逗，不知道怎麼做......
    elif sel=='5': # 測驗
        print('5. 測驗學習成果')
    elif sel=='6':
        print('6. 離開系統')
        break
    else:
        print('輸入錯誤，請重新輸入!')
