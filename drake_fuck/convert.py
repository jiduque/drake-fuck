from re import sub

from drake_fuck.data import DFSource, BFSource, Source, KeywordMap

DF_TO_BF = [
    (r"I\'m on one", "+"),
    (r"it\'s not one", "-"),
    (r"left foot", "<"),
    (r"right foot", ">"),
    (r"in", ","),
    (r"out", "."),
    (r"started from the bottom", "["),
    (r"now we here", "]"),
    (r"\s", "")
]


BF_TO_DF = [
    (r"\+", "I'm on one "),
    (r"-", "it's not one "),
    (r"<", "left foot "),
    (r">", "right foot "),
    (r",", "in "),
    (r"\.", "out "),
    (r"\[", "started from the bottom "),
    (r"\]", "now we here ")
]


def convert(doc: Source, string_map: KeywordMap) -> Source:
    output = doc
    for pattern, replace in string_map:
        output = sub(pattern, replace, output)
    return output


def to_drake(doc: BFSource) -> DFSource:
    output = convert(doc, BF_TO_DF)
    return output.strip()


def to_brain(doc: DFSource) -> BFSource:
    return convert(doc, DF_TO_BF)
