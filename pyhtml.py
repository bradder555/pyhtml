from functools import reduce, partial as curry
from functional import foldl, compose as compose2

# n-composition, reduce expects a list, so the arguments are list-ified
compose = curry(lambda f,*x: f(list(x)), curry(reduce, compose2))

# wraps an empty string up in a function
null = lambda : ""

# wraps a string up in a function
t = lambda x: lambda: x

# nicer way to run the function
render = lambda f: f()

def attr(d):
    """
    maps a dict into an attribute string
    :param d: dictionary of hash
    :return: string in the attribute format()
    """
    t = map(lambda x: '{}="{}"'.format(*x),d.items())
    return lambda : reduce(lambda x,y: "{} {}".format(x, y), t)


def generic_element(type,content=null,attr=null):
    """
    this is the template function, all other elements or curried from this element
    :param type:
    :param content:
    :param attr:
    :return:
    """
    if hasattr(content, '__iter__'):
        t = reduce(lambda x, y: lambda: "{}{}".format(x(), y()), content)
    else:
        t = content

    return lambda: "<{} {}>{}</{}>".format(type, attr(), t(), type)

# save some keystrokes
_c = curry(curry, generic_element)

# todo: put in alphabetical order to prevent duplication
a = _c("a")

p = _c("p")
h1 = _c("h1")
h2 = _c("h2")
h3 = _c("h3")
h4 = _c("h4")

html = _c("html")
head = _c("head")
img = _c("img")
body = _c("body")
div = _c("div")
span = _c("span")
table = _c("table")
form = _c("form")
article = _c("article")
aside = _c("aside")
details = _c("details")
figcaption = _c("figcaption")
figure = _c("figure")
footer = _c("footer")
header = _c("header")
main = _c("main")
nav = _c("nav")
section = _c("section")
summary = _c("summary")
time = _c("time")
ol = _c("ol")
ul = _c("ul")
li = _c("li")
dl = _c("dl")
dt = _c("dt")
dd = _c("dd")
style = _c("style")
br = _c("br")
hr = _c("hr")
b = _c("b")
strong = _c("strong")
i = _c("i")
em = _c("em")
mark = _c("mark")
small = _c("small")
dell = _c("del")
ins = _c("ins")
sub = _c("sub")
sup = _c("sup")
q = _c("q")
blockquote = _c("blockquote")
address = _c("address")
cite = _c("cite")
bdo = _c("bdo")
tr = _c("tr")
th = _c("th")
td = _c("td")
caption = _c("caption")
tfoot = _c("tfoot")
video = _c("video")
pre = _c("pre")
canvas = _c("canvas")
main = _c("main")
acronym = _c("acronym")
big = _c("big")
button = _c("button")
em = _c("em")
input = _c("input")
label = _c("label")
script = _c("script")
select = _c("select")
small = _c("small")
span = _c("span")
textarea = _c("textarea")
tt = _c("tt")
var = _c("var")
meta = _c("meta")
source = _c("source")
picture = _c("picture")
ul = _c("ul")

if __name__ == "__main__":
    """
    For Now the testing consists of writing html to an output file
    todo: build a nice looking test page
    """

    fruit = ["apples", "oranges", "bananas", "lemons"]

    sub_block_demo = table(
        [
        tr(
            [
                th(t("heading 1")),
                th(t("heading 1"))
            ]
        ),
        tr(
            [
                td(t("row 1 col 1")),
                td(t("row 1 col 2"))
            ]
        ),
        tr(
            [
                td(t("row 2 col 1")),
                td(t("row 2 col 2"))
            ]
        )
        ]
    )

    import sys
    OUT_FILE = sys.argv[1]
    with open(OUT_FILE, 'w') as f:
        f.write(
            render(
                html(
                    body(
                        [
                         h1(t("Fun trucks")),
                         p(t("This is a website about trucks"), attr=attr({"style": 'color:blue;'})),
                         ul(
                            [
                                li(t("first in list")),
                                li(t("second in list"))
                            ], attr=attr({"id": "list"})
                         ),
                         ul(
                            map(lambda x: li(t(x)), fruit), attr=attr({"id": "list"})
                         ),
                         sub_block_demo
                        ]
                    )
                )
            )
        )
