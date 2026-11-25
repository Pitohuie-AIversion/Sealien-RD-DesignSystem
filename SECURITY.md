# Security & Confidentiality Policy

## 1. Repository Visibility & Hosting Policy

- Before pushing this repository to GitHub (even as a **Private Repository** under a company Organization), confirm compliance with company information security policies.
- If company policy prohibits hosting internal visual assets or department identifiers on external cloud platforms, host exclusively on **internal GitLab** and distribute Release bundles via **internal NAS / SharePoint / Feishu**.

## 2. Prohibited Content

Never commit or attach in Releases:
- Unpublished patents, patent disclosures, or sensitive IP filing numbers
- Customer data, pricing, quotations, or commercial contracts
- Real sea-trial telemetry, raw sonar/acoustic logs, or classified CAD/engineering parameters
- Credentials, API tokens, or internal server addresses

## 3. Illustrative Placeholder Hygiene

- Sample diagrams, curves, metrics (e.g., `+25 pp`), and product ecosystem labels in `templates/powerpoint/` and `components/` are **illustrative placeholders only** (`示意图形非真实研发数据`).
- **Note on Layout 11 (`11 专业｜软件产品矩阵`)**: Sample slide 11 contains illustrative placeholder names (`DeepMatrix`, `SEAgent`). Review whether to keep or generalize these names before mirroring to an external cloud repository.

## 4. Reporting Issues

If sensitive information is accidentally committed, immediately notify the repository maintainer and R&D Center administrator to purge Git history (`git filter-repo`) and rotate any affected references.
