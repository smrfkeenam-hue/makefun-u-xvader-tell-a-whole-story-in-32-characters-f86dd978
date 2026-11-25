import os

# One Wi-Fi name, 25 chars: a breakup in a network list.
# The ex moved out and took the router, so the network itself
# is the lament — situation, character and event in one name.
ENTRY = "MyExMovedOutTookTheRouter"

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8") as f:
    # No trailing newline: the name is exactly 25 characters.
    f.write(ENTRY)
