from googlesearch import search
from urllib.parse import unquote
import wikipedia


def find(str=None, lang='ar', wiki_alone=False):

    if str == None:
        return None

    wikipedia.set_lang(lang)

    if not wiki_alone:

        re = search(str, lang=lang)
        res = None
        for x in re:
            if 'wikipedia' in x:
                title = unquote(x.split('/')[4])
                res = wikipedia.WikipediaPage(title=title)
                break
        if res:
            return res.content

    else:
        re = wikipedia.search(str)
        res = wikipedia.WikipediaPage(title=re[0])

        if res:
            return res.content

    return None
