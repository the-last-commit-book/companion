# chapter_17_the_final_program.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 17: The Final Program

from case_solver import build_case_report


case_report = build_case_report()
ranked_suspects = case_report["ranked_suspects"]
top_suspect = case_report["top_suspect"]
method_findings = case_report["method_findings"]

print("Final case solver")
print("The program ranks suspects by surfaced evidence, not by certainty.")
print()

print("Ranked suspects:")
for suspect in ranked_suspects:
    print(suspect.name, "score:", suspect.score)

print()
print("Top evidence convergence:", top_suspect.name)
print("Top score:", top_suspect.score)
print()

print("Findings attached to top suspect:")
for finding in top_suspect.findings:
    print("-", finding)

print()
print("Method findings:")
for finding in method_findings:
    print("-", finding)

print()
print("Motive:", case_report["motive"])
print("Opportunity:", case_report["opportunity"])
print("Method:", case_report["method"])
print()
print("Conclusion: the final program points to Eleanor Hartley as the strongest evidence convergence.")
print("Reminder: Python organizes the truth. Whitmore still has to prove what happened in the room.")
