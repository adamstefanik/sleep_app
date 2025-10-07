# NightNest

Modern desktop application for sleep tracking and analysis, featuring a clear interface and concise tips.

![Alt text](assets/ui-screenshot.png)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Functions

-Sleep Analysis – Displays key sleep quality metrics
-Sleep Index – Sleep quality rating on a scale from 1 to 100
-Sleep Details – Bedtime, sleep duration, and number of sleep cycles
-Health Metrics – Resting heart rate and heart rate variability (HRV)
-Expert Advice – Personalized tips based on sleep quality
-Motivational Quotes – Random quotes displayed during data loading
-Modern Interface – Intuitive GUI inspired by Ultrahuman

## How to Run

```bash
git clone https://github.com/adamstefanik/sleep_app.git
cd sleep_app
```
```
pip install -r requirements.txt
```
```
python main.py
```

## Structure

```
sleep_app/
├── pycache/
│ ├── data_generator.cpython-313.pyc
│ └── gui.cpython-313.pyc
├── assets/
│ └── ui-screenshot.png
├── bg/
│ ├── bg_fetch_data.jpg
│ ├── bg.jpg
│ ├── btn.jpg
│ ├── green.jpg
│ ├── red.jpg 
│ └── yellow.jpg 
├── .gitignore
├── data_generator.py # Generátor testovacích dát
├── gui.py # Grafické rozhranie
├── LICENSE
├── main.py # Hlavný vstupný bod
├── quotes.json # Databáza motivačných citátov
├── README.md
└── requirements.txt
```

## Dependencies

- Python 3.8+
- Tkinter
- Standart library (json, random, time, datetime)

## License

This project was developed as part of my studies in software engineering during my junior year at Univerzita Tomáše Bati v Zlíne and is intended for educational purposes.

