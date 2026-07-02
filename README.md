# The Last Commit — Companion Project

Runnable code and evidence files for the book
**_The Last Commit: Learn Python by Solving a Murder Mystery_** by Kailash Iyer.

Standard library only. Python 3.11+. Every chapter script here matches the printed
output in the book. Start with the chapter you are reading, or run `verify_outputs.py`
to execute them all.

---

This folder is the canonical companion project for *The Last Commit*. Run scripts from inside this folder.

```bash
python chapter_01_guest_list.py
python chapter_10_the_vendor_file.py
python chapter_17_the_final_program.py
python chapter_20_two_clocks.py
python chapter_23_provenance.py
python chapter_24_the_mainland_copy.py
```

The file `if_i_die_run_this.py` is broken on purpose -- it is Marcus's dead-man script, exactly as recovered. Chapter 24 walks you through repairing it (one character). The repaired version is in `solutions/if_i_die_run_this_repaired.py` if you want to check your work.

The scripts use Python 3.11+ and only the standard library. On Windows, if you see `ZoneInfoNotFoundError: 'No time zone found with key America/New_York'`, run `pip install tzdata` once; it supplies the timezone database the standard library expects. The book's printed outputs still let you keep reading either way.

## Folder layout

```text
murder_by_python/
    data/
    solutions/
    chapter_01_guest_list.py
    ...
    chapter_23_provenance.py
    chapter_24_the_mainland_copy.py
    audit_api_server.py
    if_i_die_run_this.py      (broken on purpose; see Chapter 24)
    case_solver.py
    verify_outputs.py
```

## Verification

Run:

```bash
python verify_outputs.py
```

This runs every chapter script and stores actual stdout under `outputs/`.

## The cloud audit API (Chapter 24)

`chapter_24_the_mainland_copy.py` starts a small mock service in the background and queries it, so it runs on one machine. To see the real client/server split, run the server yourself in one terminal:

```bash
python audit_api_server.py
```

then query `http://127.0.0.1:8080/audit` with header `Authorization: Bearer READONLY-EVIDENCE-TOKEN` from another terminal. It uses only `http.server` and `urllib` from the standard library. No Flask, no installs.