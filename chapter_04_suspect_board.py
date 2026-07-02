# chapter_04_suspect_board.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 4: The Suspect Board

suspect_roles = {
    "Eleanor Hartley": "Cofounder",
    "Julian Cross": "Investor",
    "Imogen Wells": "Former lead designer / ex-wife",
    "Mikhail Volkov": "Head of security",
    "Priya Anand": "Journalist",
    "Daniel Thorne": "Younger brother",
}

motive_categories = {
    "Eleanor Hartley": "direct financial: Marcus found the Northstar payments",
    "Julian Cross": "direct financial: Marcus planned to reject the buyout",
    "Imogen Wells": "personal reputation: Marcus damaged her career",
    "Mikhail Volkov": "professional risk: his security system was used",
    "Priya Anand": "story pressure: Marcus was the subject of her exposé",
    "Daniel Thorne": "family money: inheritance and old resentment",
}

declared_alibis = {
    "Eleanor Hartley": "Library",
    "Julian Cross": "Wine Cellar",
    "Imogen Wells": "West Gallery",
    "Mikhail Volkov": "Security Office",
    "Priya Anand": "Conservatory",
    "Daniel Thorne": "Billiard Room",
}

primary_financial_suspect = "Eleanor Hartley"
secondary_financial_suspect = "Julian Cross"

print("Suspect board opened.")
print()

print("Eleanor Hartley")
print("Role:", suspect_roles["Eleanor Hartley"])
print("Motive category:", motive_categories["Eleanor Hartley"])
print("Claimed alibi:", declared_alibis["Eleanor Hartley"])
print()

print("Julian Cross")
print("Role:", suspect_roles["Julian Cross"])
print("Motive category:", motive_categories["Julian Cross"])
print("Claimed alibi:", declared_alibis["Julian Cross"])
print()

print("Imogen Wells")
print("Motive category:", motive_categories["Imogen Wells"])
print()

print("Mikhail Volkov")
print("Motive category:", motive_categories["Mikhail Volkov"])
print()

print("Priya Anand")
print("Motive category:", motive_categories["Priya Anand"])
print()

print("Daniel Thorne")
print("Motive category:", motive_categories["Daniel Thorne"])
print()

print("Direct financial thread:", primary_financial_suspect, "and", secondary_financial_suspect)
print("Clue: the money trail currently points hardest at Eleanor and Julian.")
