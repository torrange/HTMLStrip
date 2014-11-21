#!/usr/bin/env python2
from re import sub
from sys import argv

def clean_html(html):
    cleaned = sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    cleaned = sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    cleaned = sub(r"(?s)<.*?>", " ", cleaned)
    cleaned = sub(r"&nbsp;", " ", cleaned)
    cleaned = sub(r"  ", " ", cleaned)
    cleaned = sub(r"  ", " ", cleaned)
    return cleaned.strip()

def main():
    try:
        html_text = open(argv[1]).read()
        clean_html = clean_html(html_text)
        print(clean_html)

    except:
        print("Please provide a valid html file to parse.")



if __name__ == "__main":
    main()
