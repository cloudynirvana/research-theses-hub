# Publish packages (fallback)

The dedicated landing repos refused `git push` (HTTP 403, `cursor[bot]`).
Local commits exist on those clones but are **not** on GitHub `main`:

| Package | Intended landing repo | Local commit (unpushed) |
| --- | --- | --- |
| `thesis-01-confluence-onco/` | https://github.com/cloudynirvana/thesis-01-confluence-onco | `7f1390d` |
| `thesis-02-complexity-nstg/` | https://github.com/cloudynirvana/thesis-02-complexity-nstg | `a950413` |
| `thesis-03-disease-profile/` | https://github.com/cloudynirvana/thesis-03-disease-profile | `24f47ed` |

Each folder is the Nile University B.Sc. chapter-structure package
(`THESIS.md`, `THESIS.pdf`, `README.md`, `DISCLAIMER.md`, `CITATION.cff`).

These computational theses are **not** the 2022 wet-lab Carica papaya AgNP
antidiabetic B.Sc. That work is Thesis 0:
https://github.com/cloudynirvana/thesis-bsc-carica-papaya-agnp
