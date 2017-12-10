import re

def cleanHTML(raw_html):
    """Returns a string containing no HTML tags.
    Source: https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string

    Args:
        raw_html: Raw HTML text

    Returns:
        string
    """
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
