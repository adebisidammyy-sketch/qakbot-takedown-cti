#Did the 2023 takedown reduce Qakbot activity?

A cyber threat intelligence (CTI) project using only free, public sources. It tests whether the August 2023 law enforcement takedown of Qakbot reduced the malware's visible activity, and what else could explain the change.

Author: Adebisi Damilola Abiola | Date: October, 2026 | Marking: TLP:CLEAR (public sources only) 
Audience: a SOC team at a regional bank (hypothetical) deciding whether to keep Qakbot detection at high priority.

Start here: read executive_brief.md (one page), then report.md for the full assessment.

Key finding

I assess with low to moderate confidence that Qakbot's visible activity was already falling before the takedown, so the takedown probably did not start the decline, though it may have helped keep activity low. Behaviour-based detections stay relevant because the same phishing delivery route continued after the takedown.

Monthly Qakbot samples on MalwareBazaar

What is in this repository
Path	Contents
executive_brief.md	One-page brief for the SOC lead
report.md	Full assessment: requirements, source evaluation, data analysis, ATT&CK mapping, competing hypotheses, gaps, recommendations
analysis/	Source register, ATT&CK mapping and evidence-weighing tables (CSV)
data/	Monthly Qakbot counts and control metrics from MalwareBazaar
scripts/	Python scripts that regenerate the data from the public dump
evidence/	Screenshots showing where each source and number came from
Method in brief
Requirements. A decision question, a main question, a hypothesis and alternatives, written before collecting data.
Collection and source evaluation. Six sources (four independent origins), each typed as primary or secondary and checked for repetition.
Data analysis. Monthly Qakbot samples from the MalwareBazaar full dump, with two controls: total submissions and distinct reporters.
ATT&CK mapping. Techniques mapped only where a source describes the behaviour, marked stated or inferred, with the period observed.
Analysis of competing hypotheses. Three explanations weighed against eight pieces of evidence.
Assessment and brief. Findings with confidence levels, gaps, and recommendations at strategic, operational and tactical level.
Limitations
One long-term dataset. URLhaus and ThreatFox exports do not go back far enough (documented in the report and in evidence/).
Sample counts show what was submitted to one platform, not attacker activity.
Evidence after the takedown is thin and rests mainly on one original source.
Reproduce

Requires Python 3 and no extra packages. You need a free abuse.ch Auth-Key to download the MalwareBazaar full dump from https://bazaar.abuse.ch/export/. The raw dump and the key are not included, so please check abuse.ch's terms of use before sharing the dump.

python scripts/01_inspect_variants.py full.csv.zip
python scripts/02_monthly_counts_and_controls.py full.csv.zip --out data

A newer dump gives different numbers. This project uses the 14 October 2026 snapshot.

Skills demonstrated

Intelligence requirements, source evaluation and double-counting checks, separating fact from judgment, confidence ratings, MITRE ATT&CK mapping, analysis of competing hypotheses, basic Python data processing, and writing for a decision-maker.

How this was made

I did the hands-on collection: I registered for the free abuse.ch Auth-Key, downloaded the MalwareBazaar data, ran the Python code in Google Colab, found and read the six sources, checked each technique on the MITRE ATT&CK site, and took the screenshots in evidence/.
