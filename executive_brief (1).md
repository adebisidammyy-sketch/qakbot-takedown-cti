# Executive Intelligence Brief
## Qakbot after the 2023 takedown: should we keep it as a high-priority detection?

**Audience:** SOC team, regional bank (hypothetical audience for a portfolio project)
**Date:** October 2026 | **Data snapshot:** MalwareBazaar, 14 October 2026
**Marking:** TLP:CLEAR (public sources only)

### Bottom line
I assess with **low to moderate confidence** that Qakbot's visible activity was already falling before the takedown in late August 2023. The takedown probably did not start the decline, though it may have helped keep activity low. We recommend lowering the priority of Qakbot-specific indicators while keeping behaviour-based detections.

### Key findings
- **The fall began before the takedown.** MalwareBazaar Qakbot samples dropped from 309 in June 2023 to 5 in July 2023. They averaged about 166 a month before and about 4 a month after.
- **It was Qakbot, not the whole platform.** Total submissions stayed in a similar range, while Qakbot's share fell from about 1.3% to about 0.04%.
- **A second source agrees on timing.** Zscaler reported a drop after June 2023, with the cause unclear.
- **The operators did not disappear.** Cisco Talos reported a phishing campaign delivering ransomware and a backdoor from early August 2023, tied to Qakbot affiliates with moderate confidence. Microsoft reported a low-volume Qakbot campaign in December 2023.
- **The entry route stayed the same.** Phishing emails with attachments or links appear before and after the takedown.

### Why it matters to a bank
The DOJ lists financial services organisations among victims of ransomware delivered through Qakbot. Even with Qakbot quiet, the same initial access route works for other malware.

### Recommendations
1. **Strategic:** lower Qakbot-specific indicators, but do not retire them, and keep ransomware readiness high.
2. **Operational:** check MalwareBazaar's monthly Qakbot count each quarter, and review if it passes your set threshold.
3. **Tactical:** keep detections for phishing attachments and links, LNK files fetching remote files, scheduled task creation, indirect command execution and DLL side-loading.

### What we don't know
We cannot separate less Qakbot from fewer researchers reporting it. The analysis rests mainly on one dataset, and evidence after the takedown is thin. We did not assess activity in the bank's own region.

*Full analysis, sources and data: see `report.md`.*
