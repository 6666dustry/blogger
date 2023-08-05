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
        "<p>非商用、商用利用ともに自由です。Webページのデザインに組み込んだり、このデザインを改良して自分だけのデザインを作ってみてください！</p>"
        "<p>もちろんコメントでのリクエストも受け付けています！コメントはこの記事の一番下にあります。ぜひ何かリクエストしてみてください！</p>\n",
        f"<p>今日は{i}日目！</p>\n",
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
  f.write("\n<h2>svgの中身</h2>\n")
  f.write(f'<pre class="prettyprint linenums">{html.escape(content)}</pre>')
