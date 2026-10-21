# FBR1 exposure log, version 1

## Scope and clean-exposure declaration

Owned directory:

`/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/criticism/FBR1`

All relative paths below are relative to that directory. The assignment authorized exactly four scientific input files, the assignment itself, and this referee's own new work. Those restrictions were followed. No other project scientific file, proof, status, ledger, report, transcript, directory listing, or summary was read. No external retrieval was performed. No author proof or another referee's findings were supplied. No forbidden scientific exposure occurred.

The administrative worker task and generic environment/tool definitions were visible. They supplied paths, permissions, model instructions, and deadlines, but no additional mathematical findings. The task was fork-none. There were no scientific findings in outbound messages before sealing; progress messages concerned reading, drafting, and sealing only.

## Complete file-read inventory

| File | Reads | Permission and purpose |
| --- | --- | --- |
| `assignment-v1.md` | Initial `cat`; `sha256sum`; final sealing Python read | Explicitly allowed assignment and its hash |
| `input/M1-statement-v1.md` | Packet `cat`; `sha256sum`; final sealing Python read | Explicitly allowed scientific input |
| `input/A-statement-v1.md` | Packet `cat`; `sha256sum`; final sealing Python read | Explicitly allowed scientific input |
| `input/B-statement-v1.md` | Packet `cat`; `sha256sum`; final sealing Python read | Explicitly allowed scientific input |
| `input/definitions-v1.md` | Packet `cat`; `sha256sum`; final sealing Python read | Explicitly allowed scientific background |
| `report-v1.md` | `wc -l -w`; final sealing hash read and verification reread | Own newly created work, allowed |
| `exposure-log-v1.md` | Final sealing hash read and verification reread | Own newly created work, allowed |
| `seal-v1.json` | Final sealing verification reread, after creation | Own newly created work, allowed |

No directory-enumerating command was used. Standard runtime library loading by command interpreters is not project scientific input; the inventory concerns files deliberately opened as task evidence or artifacts.

## Tool/action chronology

1. `functions.exec` called `tools.exec_command` with `cat` on the absolute assignment path. Only the assignment content was returned. Allowed.
2. `functions.exec` used `Promise.allSettled` to call `tools.exec_command` with `cat input/M1-statement-v1.md input/A-statement-v1.md input/B-statement-v1.md input/definitions-v1.md`, from the owned directory, and to call `tools.clock__curr_time({})`. Only the four allowed scientific texts and UTC time were returned. The clock returned `2026-10-21 06:08:28 UTC`. Allowed.
3. `functions.exec` called `tools.clock__curr_time({})`; it returned `2026-10-21 06:13:16 UTC`. Allowed administrative read.
4. `functions.exec` called `tools.clock__curr_time({})` and then `tools.exec_command` with `sha256sum input/M1-statement-v1.md input/A-statement-v1.md input/B-statement-v1.md input/definitions-v1.md assignment-v1.md`. The clock returned `2026-10-21 06:15:38 UTC`. These were allowed administrative time and exact input/assignment reads.
5. `functions.exec` called `tools.apply_patch` to create `report-v1.md` in the owned directory. No preexisting project scientific file was read or changed. This was an allowed write of new referee work.
6. `functions.exec` called `tools.clock__curr_time({})` and then `tools.exec_command` with `wc -l -w report-v1.md`, from the owned directory. The clock returned `2026-10-21 06:19:28 UTC`; `wc` reported 280 lines and 3784 words. Allowed own-work and administrative reads.
7. `functions.exec` called `tools.apply_patch` to create this exposure log in the owned directory. Allowed write of new referee work.
8. The final sealing invocation of `functions.exec` calls `tools.exec_command` with a standard-library Python heredoc from the owned directory. The script reads exactly the assignment, the four permitted inputs, `report-v1.md`, and this log; obtains the current UTC time; computes SHA256 values; and creates `seal-v1.json` exclusively. It then rereads only that new seal, the report, and the log to verify the frozen hashes. It prints only administrative paths/hashes/time. These reads and writes are all allowed. This entry is written immediately before that invocation; a successfully created and verified seal records its completion. The script is an administrative hashing operation, not a scientific experiment.
9. After successful sealing, a `collaboration.send_message` notification or the final worker response may disclose the completed report, its hashes, and findings to the assigning root. This is the assignment's expressly required return channel. It reads no additional scientific source.

No `list_agents`, `get_goal`, goal mutation, child worker, background session, model/tier change, external messaging connector, web tool, resource retrieval, skill-file read, or other project-file read was used. No experimental job was run, so no reservation was requested or consumed.

## Input hashes observed before sealing

| File | SHA256 |
| --- | --- |
| `input/M1-statement-v1.md` | `4e21066d0ba5266384b5c493877ad95a41b65b49cc75d6136f243e299af7d5bf` |
| `input/A-statement-v1.md` | `ac3117ca1e9c2126422df06cd1983a2368e0c58d2eda073e22108f1f7b5a7ba8` |
| `input/B-statement-v1.md` | `d146b96e287e885ad05255a00f2afbde8ce926bf03c9ffa85d2cc8fe37576c91` |
| `input/definitions-v1.md` | `45636918ca0c107c64d8eb2cc15fd783043fd3bc61bed116122f661a8c64a775` |
| `assignment-v1.md` | `4e0a113b3a10af1360b8687c017a1dd468d8d6b49d694e671878487966469eac` |

`seal-v1.json` records independently recomputed hashes of these exact inputs, this frozen exposure log, and the frozen complete report, together with the UTC sealing time. All versions are preserved. No post-seal scientific edit is part of version 1.
