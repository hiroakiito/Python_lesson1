import csv
import itertools

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# csvからの取得
with open('character.csv', 'r', newline = '') as f:
    reader = csv.reader(f)
    source = list(itertools.chain.from_iterable([ e for e in reader ]))

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{0}が見つかりました".format(word))
    else:
        print("{0}は見つかりませんでした、登場人物リストに追加します。".format(word))
        # リストへの追加
        source.append(word)
        # CSVファイルへの追加
        with open('character.csv', 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow([word])


        # 見つからなかった場合、追加出来たか確認のためもう一度同じ処理を通す
        word =input("もう一度鬼滅の登場人物の名前を入力してください >>> ")
        if word in source:
            print("{0}が見つかりました".format(word))
        else:
            print("キャラクターの追加に失敗しました。")


    

if __name__ == "__main__":
    search()