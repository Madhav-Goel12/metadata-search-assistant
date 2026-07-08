import re


def extract_search_terms(user_query: str):
    """
    Extract possible database column names from a natural language query.
    """

    # Convert to lowercase
    query = user_query.lower()

    # Remove punctuation
    query = re.sub(r"[^\w\s]", " ", query)

    # Words that don't help in searching
    stop_words = {
        "where",
        "what",
        "which",
        "find",
        "show",
        "give",
        "display",
        "list",
        "get",
        "fetch",
        "column",
        "columns",
        "field",
        "fields",
        "contains",
        "contain",
        "having",
        "with",
        "is",
        "are",
        "the",
        "a",
        "an",
        "of",
        "for",
        "me",
        "can",
        "you",
        "please",
        "stored",
        "store",
        "in",
        "from",
        "to"
    }

    # Split using common separators
    phrases = re.split(r"\band\b|,|&", query)

    search_terms = []

    for phrase in phrases:

        words = []

        for word in phrase.strip().split():

            if word not in stop_words:
                words.append(word)

        if words:
            column = "_".join(words)
            search_terms.append(column)

    # Remove duplicates while preserving order
    unique_terms = []

    for term in search_terms:
        if term not in unique_terms:
            unique_terms.append(term)

    # If nothing extracted, use original query
    if not unique_terms:
        unique_terms.append(user_query.lower())

    return unique_terms