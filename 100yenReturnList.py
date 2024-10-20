user_list = []
stock = 400
ret = 0

while True:
    user = int(input()) #IDは1000以上9999以下
    if(ret == stock): #アイスの在庫分と同じ量の100円玉を返却
        break
    elif(user == 0): #0を打ち込んだら時系列順に配列を表示
        print("時系列順に100円を渡した人のIDを表示します。")
        print(user_list)
    elif(user == -1): #-1を打ち込んだらIDの昇順に配列を表示
        print("IDの昇順に100円を渡した人のIDを表示します。")
        user_list_sorted = sorted(user_list)
        print(user_list_sorted)
    elif(user == -2): #-2を打ち込んだら何回返却したか表示
        print(str(ret * 100) + "円分の返却を行いました。")
    elif(user == -3): #-3を打ち込んだら、ミスタイプして登録したユーザのデータを消去
        d = int(input("何番のユーザーを消しますか？"))
        if(d in user_list):
            user_list.remove(d)
            print(str(d) + "番のユーザーを消しました。")
        else:
            print("該当するIDはまだ登録されていません。")
    elif(user in user_list):
        print("注意!" + str(user) + "番の人には既に100円を渡しています。")
    else:
        user_list.append(user)
        print(str(user) + "番のユーザーを登録しました。100円玉を渡してください。")
        ret += 1

print("全てのお客様に100円をお渡ししました。完売!")

#コーディング制作、橋本です。何かエラーが出たら呼んでください。
#注意！ このプログラミングは1日中起動しておいてください。1度閉じるとデータが全部消えます。ログを見てもっかい打ち直すことになるので、お気をつけて。