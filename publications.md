---
layout: page
title: Publications
permalink: /publications/
---

{% assign sorted_pubs = site.data.publications %}
{% for pub in sorted_pubs %}
- **{{ pub.authors }}** ({{ pub.year }}). *{{ pub.title }}*. _{{ pub.journal }}_. {% if pub.url %}[PDF]({{ pub.url }}){% endif %}
{% endfor %}




## Some papers straight out of EDoN

- Wilson, S., Beswick, E., Morrell, R. et al. Acceptability of wearable technology for the early detection of dementia-causing diseases: perspectives from the CODEC II cohort. BMC Digit Health 3, 55 (2025). https://doi.org/10.1186/s44247-025-00191-3
- Wilson, S., Beswick, E., Popp, Z. et al. Acceptability of technologies to support early dementia detection: Qualitative insights from the Boston University Alzheimer’s Disease Centre Cohort. (Journal article manuscript submitted on 4 December 2025).
- Whitfield, T, Walker Z, et al. The Early Detection of Neurodegenerative diseases (EDoN) Initiative: protocol for a meta-cohort study (Journal article manuscript in preparation, plan to submit in February 2026).



## Data Stewardship: UCL
At UCL we're preparing the digital data and documentation for wider sharing with the research community. The goal is to facilitate future research projects through making data access and analysis straightforward, including examples of code for analyses.

## Research
We have various internal research projects in mind and look forward to sharing the results at upcoming scientific meetings.