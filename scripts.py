import csv
import itertools

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# csvからの取得
f = open("キャラクター.csv", "r")
reader = csv.reader(f)
data = list(itertools.chain.from_iterable([ e for e in reader ]))
f.close()
source.extend(data)

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{0}が見つかりました".format(word))
    else:
        print("{0}は見つかりませんでした、登場人物リストに追加します。".format(word))
        source.append(word)

        # 見つからなかった場合、追加出来たか確認のためもう一度同じ処理を通す
        word =input("もう一度鬼滅の登場人物の名前を入力してください >>> ")
        if word in source:
            print("{0}が見つかりました".format(word))
        else:
            print("キャラクターの追加に失敗しました。")


    

if __name__ == "__main__":
    search()