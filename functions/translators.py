import functions.image_handler as ih

def process_data(name, flag):
    untranslated_text = ih.image_to_text(name)
    translated_text = translate(untranslated_text, flag)

    return translated_text

def encode_text(text):
    keywords ={
        '%': '%25',
        ",": '%2C',
        "/": '%5C%2F',
        '?': '%3F',
        ':': "%3A",
        ';': '%3B',
        "[": '%5B',
        ']': "%5D",
        '{': '%7B',
        '}': '%7D', 
        '+': '%2B',
        '=': '%3D',
        "\\": '%5C%5C',
        '|': '%5C%7C',
        '&': '%26',
        '^': '%5E',
        '$': '%24',
        '#': '%23',
        "@": '%40'
    }

    for keyword in keywords:
        if keyword in text:
            text = text.replace(keyword, keywords[keyword])

    return text



def translate(text, flag):
    if flag:
        to_language = "pl"
    else:
        to_language = "en"

    return_string = f"https://www.deepl.com/translator#de/{to_language}/{encode_text(text)}"
    return return_string