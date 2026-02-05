LANG = "zh"

def init(lang):
    global LANG
    LANG = lang

def t(zh, en):
    return en if LANG == "en" else zh
