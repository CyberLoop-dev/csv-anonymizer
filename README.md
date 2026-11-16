<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=CSV%20Anonymizer&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="CSV Anonymizer banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Pseudonymize%20selected%20CSV%20columns%20locally" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/csv-anonymizer/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/csv-anonymizer?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/csv-anonymizer/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/csv-anonymizer?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/csv-anonymizer?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="CSV Anonymizer illustration"></p>

## 🧭 Overview
Replace selected CSV fields with stable HMAC pseudonyms while keeping the original table structure.

## ✨ Features
- 🕶️ Pseudonymize selected columns without changing row order.
- 🔐 Use HMAC-SHA256 with a secret salt from an environment variable.
- 🧾 Preserve headers and unselected fields exactly.
- 🚫 Never write the salt or original selected values to logs.

## 🖥️ Demo
~~~bash
CSV_ANON_SALT=demo-only python main.py examples/people.csv output/people-anon.csv --columns email
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/csv-anonymizer.git
cd csv-anonymizer
CSV_ANON_SALT=demo-only python main.py examples/people.csv output/people-anon.csv --columns email
~~~

## 🧰 Tech Stack
- Python 3.10+
- csv, hashlib, hmac, os, argparse (standard library)

## 🗂️ Folder Structure
~~~text
csv-anonymizer/\n├── assets/icon.svg\n├── examples/people.csv\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add configurable output token length.
- [ ] Add a JSON summary of rows and columns processed.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
