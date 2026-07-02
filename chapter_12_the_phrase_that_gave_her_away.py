# chapter_12_the_phrase_that_gave_her_away.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 12: The Phrase That Gave Her Away

import re

messages_file_path = "data/messages.txt"
phrase_pattern = re.compile(r"clean exit", re.IGNORECASE)

match_count = 0
matched_lines = []

print("Message phrase review")
print("File:", messages_file_path)
print("Pattern:", phrase_pattern.pattern)
print()

with open(messages_file_path, encoding="utf-8") as messages_file:
    for line_number, line in enumerate(messages_file, start=1):
        clean_line = line.strip()
        matches = phrase_pattern.findall(clean_line)

        if matches:
            match_count = match_count + len(matches)
            matched_lines.append(clean_line)
            print("Line", line_number, "match:", clean_line)

print()
print("Total 'clean exit' matches:", match_count)
print("Matched lines found:", len(matched_lines))

if match_count == 2:
    print("Clue: the phrase 'clean exit' appears in Eleanor's earlier message and Marcus's recovered note.")

if match_count != 2:
    print("Review needed: the expected phrase match count was not found.")
