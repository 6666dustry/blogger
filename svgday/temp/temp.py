import sys
import html
if not (len(sys.argv) >= 2 and sys.argv[1].isdigit()):
    RuntimeError("You must input a day number")
i: int = int(sys.argv[1])
if not (len(sys.argv) >= 3 ):
    RuntimeError("You must input a path to svg file.")
path:str =sys.argv[2]
savePath=path
savePath=savePath.replace('\\','/')
savePath= savePath.rsplit('/', 1)[0] + f"/1Day,1SVG-Day{i}.html"

f = open(savePath, "w", encoding="utf-8")
f.write("<p>千里の道も一歩から。</p>\n<p>このシリーズは一日一枚svgのデザインをつくるというシンプルな企画です。</p>\n")
f.write("<p>コメントでのリクエストも受け付けています。</p>\n")
f.write(f"<p>今日は{i}日目。</p>\n")
try:
    svg =open(path, "r", encoding="utf-8")
    code=svg.read()
    f.write(code)
    f.write("\n<p>svgの中身</p>\n")
    f.write(f"<pre class=\"prettyprint linenums\">{html.escape(code)}</pre>")
    f.close()
except:
    print("svg file is not found or path is not valid.")
    f.close()
