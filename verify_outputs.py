from pathlib import Path
import subprocess, sys, json

BASE = Path(__file__).resolve().parent
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)
SCRIPTS = [f"chapter_{i:02d}_" for i in range(1, 25)]
paths = []
for prefix in SCRIPTS:
    matches = sorted(BASE.glob(prefix + "*.py"))
    if matches:
        paths.append(matches[0])
paths.append(BASE / "solutions" / "if_i_die_run_this_repaired.py")
paths.append(BASE / "verify_dataset.py")

results = []
for script in paths:
    completed = subprocess.run([sys.executable, str(script.relative_to(BASE))], cwd=BASE, capture_output=True, text=True)
    output_path = OUT / (script.stem + ".out.txt")
    output_path.write_text(completed.stdout, encoding="utf-8")
    results.append({"script": script.name, "returncode": completed.returncode, "stdout_file": str(output_path.relative_to(BASE)), "stderr": completed.stderr})
    print(script.name, "OK" if completed.returncode == 0 else "FAILED")

failures = [r for r in results if r["returncode"] != 0]
(OUT / "verification_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
if failures:
    raise SystemExit(1)
print("All companion scripts completed successfully.")
