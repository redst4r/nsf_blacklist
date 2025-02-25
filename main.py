"""
export
"""

import toolz
from nsf_blacklist import load_blacklist
import json


def export():
    bdict = load_blacklist()

    with open("./nsf_blacklist.json", "w") as fh:
        json.dump(bdict, fh, indent=6)

    # single term per line
    with open("./nsf_blacklist.txt", "w") as fh:
        joined = toolz.valmap(lambda terms: "\n".join(terms), bdict)
        s = "\n".join([term_string for topic, term_string in joined.items()])
        fh.write(s)


if __name__ == "__main__":
    export()
