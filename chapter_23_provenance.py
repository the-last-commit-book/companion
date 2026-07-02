# chapter_23_provenance.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 23: Provenance, or Garbage In

provenance_weights = {
    "physical": 1.0,
    "independent_system": 1.0,
    "mainland_records": 1.0,
    "witness": 1.0,
    "suspect_supplied": 0.5,
    "forged_repo": 0.0,
}

murder_findings = [
    {"suspect": "Mikhail Volkov", "label": "SVC-KIOSK session blinded CAM-EAST-02 at 00:10", "points": 3, "provenance": "independent_system"},
    {"suspect": "Mikhail Volkov", "label": "scripted 0.38s alert acknowledgment as alibi", "points": 2, "provenance": "independent_system"},
    {"suspect": "Mikhail Volkov", "label": "forged history pushed from RAVENHOUSE-SEC01 at 02:09", "points": 3, "provenance": "independent_system"},
    {"suspect": "Mikhail Volkov", "label": "manager of record for Seahook Holdings", "points": 3, "provenance": "mainland_records"},
    {"suspect": "Mikhail Volkov", "label": "custody of retired handset matching planted device", "points": 2, "provenance": "physical"},
    {"suspect": "Mikhail Volkov", "label": "knew OLD-ADMIN-000 still worked", "points": 1, "provenance": "independent_system"},
    {"suspect": "Mikhail Volkov", "label": "large man seen descending service stair ~00:11", "points": 1, "provenance": "witness"},
    {"suspect": "Eleanor Hartley", "label": "knew OLD-ADMIN-000 still worked", "points": 1, "provenance": "independent_system"},
    {"suspect": "Eleanor Hartley", "label": "deleted private meeting with Marcus", "points": 1, "provenance": "independent_system"},
    {"suspect": "Eleanor Hartley", "label": "library alibi collapse (report supplied by security export)", "points": 2, "provenance": "suspect_supplied"},
    {"suspect": "Eleanor Hartley", "label": "HARTLEY-PRIVATE device near east wing", "points": 2, "provenance": "forged_repo"},
    {"suspect": "Daniel Thorne", "label": "east-wing visit 00:10:52 to 00:12:31", "points": 1, "provenance": "witness"},
]

fraud_findings = [
    {"suspect": "Eleanor Hartley", "label": "approved four under-threshold Northstar payments", "points": 3, "provenance": "mainland_records"},
    {"suspect": "Eleanor Hartley", "label": "'clean exit' pressure on Marcus before announcement", "points": 2, "provenance": "independent_system"},
    {"suspect": "Eleanor Hartley", "label": "deleted meeting and denial before discovery", "points": 1, "provenance": "independent_system"},
    {"suspect": "Mikhail Volkov", "label": "Seahook received $146,750 of Northstar funds", "points": 3, "provenance": "mainland_records"},
]


def weighted_scores(findings):
    scores = {}

    for finding in findings:
        suspect = finding["suspect"]
        weight = provenance_weights[finding["provenance"]]
        value = finding["points"] * weight

        if suspect not in scores:
            scores[suspect] = 0

        scores[suspect] = scores[suspect] + value

    return scores


def print_model(title, findings):
    print(title)

    scores = weighted_scores(findings)

    for finding in findings:
        weight = provenance_weights[finding["provenance"]]
        value = finding["points"] * weight
        print(" ", finding["suspect"], "|", finding["label"])
        print("    provenance:", finding["provenance"], "| points:", finding["points"], "| weighted:", value)

    print()
    for suspect in scores:
        print("  TOTAL", suspect + ":", scores[suspect])
    print()


print("Provenance-weighted case model")
print("Rule: a finding is only as honest as its source.")
print()
print_model("MURDER MODEL", murder_findings)
print_model("FRAUD MODEL", fraud_findings)
print("Conclusion: the murder model converges on Mikhail Volkov.")
print("The fraud model remains Eleanor Hartley's to answer.")
print("The forged findings now weigh what they always weighed: nothing.")
