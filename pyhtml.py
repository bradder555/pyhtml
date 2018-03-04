from functools import reduce, partial as curry
from functional import foldl, compose as compose2

# n-composition, reduce expects a list, so the arguments are list-ified
compose = curry(lambda f,*x: f(x), curry(reduce, compose2))

# wraps an empty string up in a function
null = lambda : ""
nulliter = ([null])

# wraps a string up in a function
t = lambda x: lambda: x

# nicer way to run the function
render = lambda f: f()

no_content = lambda: AttributeError("For this function, content should be None")
no_at = lambda: AttributeError("For this function, at should be None")
missing_type = lambda: AttributeError("The type can't be None; something bad has happened...")


def element_only(type, content, at):
    if content != null: raise no_content()
    if at != null: raise no_at()
    return lambda: ''.join(("<", type, ">"))


def only_at(type, content, at):
    if content != null: raise no_content()
    return lambda: ''.join(("<",type," ",at(), "/>"))


def content_only(type, content, at):
    if at != null: raise no_at()
    # i don't think such a case exists...
    return lambda: ''.join(("<",type,">",content(),"</",type,">"))


def content_and_at(type, content, at):
    return lambda: ''.join(("<", type, " ", at(), ">", content(), "</", type, ">"))

def generic_element(behaviour, type, content=null, at=null):
    if type == None: raise missing_type()
    """
    this is the template function, all other elements or curried from this element
    :param type:
    :param content:
    :param at:
    :return:
    """
    if hasattr(content, '__iter__'):
        t = lambda: "".join(map(lambda x: x(), content))
    else:
        t = content

    return behaviour(
        type,
        t,
        at)

# save some keystrokes
naoc = curry(curry,generic_element, element_only)
ao = curry(curry,generic_element, only_at)
co = curry(curry,generic_element, content_only)
ac = curry(curry,generic_element, content_and_at)

# todo: put in alphabetical order to prevent duplication
a = ac("a")
abbr = ac("abbr")
acronym = ac("acronym")
address = ac("address")
applet = ac("applet")
area = ac("area")
article = ac("article")
aside = ac("aside")
audio = ac("audio")

b = ac("b")
base = ac("base")
basefont = ac("basefont")
bdi = ac("bdi")
bdo = ac("bdo")
big = ac("big")
blockquote = ac("blockquote")
body = ac("body")
br = naoc("br")
button = ac("button")

canvas = ac("canvas")
caption = ac("caption")
center = ac("cetner")
cite = ac("cite")
code = ac("code")
col = ac("col")
colgroup = ac("colgroup")

data = ac("data")
datalist = ac("datalist")
dd = ac("dd")
dell = ac("del")
details = ac("details")
dfn = ac("dfn")
dialog = ac("dialog")
dir = ac("dir")
div = ac("div")
dl = ac("dl")
dt = ac("dt")

em = ac("em")
embed = ao("embed")

fieldset = ac("fieldset")
figcaption = ac("figcaption")
figure = ac("figure")
footer = ac("footer")
form = ac("form")
font = ac("font")
frame = ao("frame")
frameset = ac("frameset")

h1 = ac("h1")
h2 = ac("h2")
h3 = ac("h3")
h4 = ac("h4")
h5 = ac("h5")
h6 = ac("h6")
head = ac("head")
header = ac("header")
hr = naoc("hr")
html = ac("html")

i = ac("i")
iframe = ac("iframe")
img = ao("img")
input = ao("input")
ins = ac("ins")

kbd = ac("kbd")

label = ac("label")
legend = ac("legend")
li = ac("li")
link = ao("link")

main = ac("main")
mapp = ac("map")
mark = ac("mark")
menu = ac("menu")
menuitem = ao("menuitem")
meta = ao("meta")
meter = ac("meter")

nav = ac("nav")
noframes = ac("noframes")
noscript = ac("noscript")

object = ao("object")
ol = ac("ol")
optgroup = ac("optgroup")
option = ac("option")
output = ao("output")

p = ac("p")
param = ao("param")
picture = ac("picture")
pre = ac("pre")
progress = ac("progress")

q = ac("q")

s = ac("s")
samp = ac("samp")
script = ac("script")
section = ac("section")
select = ac("select")
small = ac("small")
source = ao("source")
span = ac("span")
# strike not supported in html5
strong = ac("strong")
style = ac("style")
sub = ac("sub")
summary = ac("summary")
sup = ac("sup")

table = ac("table")
tbody = ac("tbody")
td = ac("td")
template = ac("template")
textarea = ac("textarea")
tfoot = ac("tfoot")
th = ac("th")
thead = ac("thead")
time = ac("time")
title = ac("title")
tr = ac("tr")
track = ao("track")
tt = ac("tt")

u = ac("u")
ul = ac("ul")

var = ac("var")
video = ac("video")

def at(d):
    """
    maps a dict into an at string
    :param d: dictionary of hash
    :return: string in the at format()
    """
    f = lambda x: "".join((x[0], "=", x[1]))
    return lambda: "".join(map(f, d.items()))


if __name__ == "__main__":
    print(body()())
    print(body(t("hello"))())
    print(body([p([t("hello")])])())
    print(body([])())
    print(body([p([t("hello")])])())
    print(body([p([t("hello")]), p([t("hello")])])())
    print(body([p([t("hello")]), br(), p([t("hello")])])())
    fruit = ["apples", "oranges", "bananas", "lemons"]

    sub_block_demo = table(
        [
        tr(
            [
                th([t("heading 1")]),
                th([t("heading 1")])
            ]
        ),
        tr(
            [
                td([t("row 1 col 1")]),
                td([t("row 1 col 2")])
            ]
        ),
        tr(
            [
                td([t("row 2 col 1")]),
                td([t("row 2 col 2")])
            ]
        )
        ]
    )

    doc = render(
        html(
            [
            head([
                title([t("Awesome Page!")])
            ]),
            body(
                [
                 h1([t("Fun trucks")]),
                 p([t("This is a website about trucks")]),
                 br(),
                 p([t("paragraph after a break")], at({"id": "paragraph_2"})),
                 ul(
                    [
                        li([t("first in list")]),
                        li([t("second in list")])
                    ]
                 ),
                 ul(
                    map(lambda x: li([t(x)]), fruit)
                 ),
                 sub_block_demo
                ]
            )
        ])
    )

    import tempfile
    import os

    tf_h, tf_p = tempfile.mkstemp(".html")
    tf_p = tf_p.replace('\\', '/' )

    with os.fdopen(tf_h, mode='wb') as fp:
        fp.write(doc.encode('utf-8'))

    from selenium import webdriver as wd
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    chrome = wd.Chrome() # chromedriver needs to be on the PATH
    chrome.get("file:///"+tf_p)
    WebDriverWait(chrome,3).until(EC.title_is, 'Awesome Page!')
    os.remove(tf_p)

    import time
    time.sleep(60)

    chrome.quit()