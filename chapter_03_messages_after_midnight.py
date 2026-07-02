# chapter_03_messages_after_midnight.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 3: Messages After Midnight

vendor_message = "[2025-10-12 18:44 local] Marcus Thorne -> Eleanor Hartley: I found the Northstar payments. We will discuss this before any announcement."
whitmore_message = "[2025-10-13 23:42 local] Marcus Thorne -> Detective Claire Whitmore: If this weekend turns ugly, check the old vendor file."

vendor_message_body = vendor_message.replace(
    "[2025-10-12 18:44 local] Marcus Thorne -> Eleanor Hartley: ",
    "",
)

whitmore_message_body = whitmore_message.replace(
    "[2025-10-13 23:42 local] Marcus Thorne -> Detective Claire Whitmore: ",
    "",
)

lowercase_vendor_message = vendor_message_body.lower()
northstar_position = lowercase_vendor_message.find("northstar")

instruction_start = whitmore_message_body.find("check")
instruction = whitmore_message_body[instruction_start:]
file_to_check = instruction.replace("check ", "").replace(".", "")

print("Recovered message to Eleanor:", vendor_message_body)
print("Keyword position for 'northstar':", northstar_position)
print("Recovered instruction to Whitmore:", instruction)
print("File Marcus wanted checked:", file_to_check)
print("Clue: Marcus was investigating Northstar payments and pointed Whitmore to the old vendor file.")
