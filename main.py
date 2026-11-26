#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun bounty entry.

Writes one funny one-line review, in the dog's voice, to /output/entry.txt.
The review is a single line under 200 characters: a grievance (the daily
sneak-up and paper shoved through the door), a suspicion (he flees before
he can be sniffed), and a small triumph — the treats are the only thing
standing between him and a formal complaint filed with the squirrels.
"""

import os

ENTRY = (
    "One star. He creeps up daily, shoves paper through my door, "
    "then flees before I can sniff him. The treats are the only "
    "reason I haven't filed a formal complaint with the squirrels."
)


def main() -> None:
    # Validation gate: the entry must stay a single line within the
    # competition's 1-200 character limit before it is written out.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise ValueError(f"entry must be 1-200 chars, one line; got {len(ENTRY)}")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
