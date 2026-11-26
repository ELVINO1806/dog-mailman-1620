import os

ENTRY = "Two stars. He comes every day, smells of other dogs, and never once brings the stick. I have filed a formal bark with the fence."

def check_length(text):
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")


check_length(ENTRY)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
