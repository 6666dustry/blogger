import sys
import html
from extracttext import extract_title_and_desc

if not (len(sys.argv) >= 2 and sys.argv[1].isdigit()):
  RuntimeError("You must input a day number")
i: int = int(sys.argv[1])
if not (len(sys.argv) >= 3):
  RuntimeError("You must input a path to svg file.")
path: str = sys.argv[2]
savePath = path
savePath = savePath.replace("\\", "/")
savePath = savePath.rsplit("/", 1)[0] + f"/1Day,1SVG-Day{i}.html"
with open(savePath, "w", encoding="utf-8") as f, open(
  path, "r", encoding="utf-8"
) as svg:
  f.writelines(
      [
        "<p>千里の道も一歩から。</p>\n<p>このシリーズは一日一枚svgのデザインをつくるというシンプルな企画です。</p>\n",
        "<p>コメントでのリクエストも受け付けています。</p>\n",
        f"<p>今日は{i}日目。</p>\n",
      ]
    )
  content=svg.read()
  title, desc = extract_title_and_desc(content)
  f.writelines(
    [f"<p>今日のSVGは{title}!</p>\n", f"<p>{desc}</p>\n"]
    )
  svg.seek(0)
  lines = svg.readlines()
  for line in lines:
    if not line.startswith("<?xml"):
      f.write(line)
  f.write("\n<p>svgの中身</p>\n")
  f.write(f'<pre class="prettyprint linenums">{html.escape(content)}</pre>')
