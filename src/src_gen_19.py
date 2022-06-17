from typing import List

def sat193(orig: str, target="-Hello,_world!__This_is-so-easy!-"):
    assert "_" not in orig and "-" not in orig
    new = ""
    space_count = 0
    for c in orig:
        if c == " ":
            space_count += 1
        else:
            new += ("-" if space_count > 2 else "_" * space_count)
            new += c
            space_count = 0
    new += ("-" if space_count > 2 else "_" * space_count)
    return new == target
def sol193(target="-Hello,_world!__This_is-so-easy!-"):
    """Find a string such that, when three or more spaces are compacted to a '-' and one or two spaces are
    replaced by underscores, leads to the target.

    "_o-k__?-" => "  o        k  ?     "
    """
    return target.replace("-", " " * 3).replace("_", " ")
# assert sat193(sol193())
