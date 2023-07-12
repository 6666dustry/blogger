import sys
import datetime
# TODO:月をまたいだ時の処理
# TODO:起点の日付を設定する引数の追加
date = datetime.date.today()
i: int = int(sys.argv[1]) if sys.argv[1].isdigit() else 1
if not sys.argv[1].isdigit():
    print("You must input a start position (int).This time,start from 1")

rangeNum: int = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else 9

f = open(f"summary{i}-{i+rangeNum}.txt", "w", encoding="utf-8")
f.write("<h2>10日間のまとめ</h2>\n")
f.write("<ul>\n")
for i in range(i, i + rangeNum):
    
    f.write(
        f'  <li>\n    <a href="https://kindnessforme.blogspot.com/{date.strftime("%Y/%m")}/day{i}.html">{i}日目</a>\n  </li>\n'
    )
f.write("</ul>\n")
f.close()
