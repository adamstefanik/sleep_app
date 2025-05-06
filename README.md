# NightNest🌙

Moderná desktopová aplikácia na sledovanie a analýzu spánku s prehľadným rozhraním a krátkymi radami.

![Alt text](assets/ui-screenshot.png)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Funkcie

- **Analýza spánku** - Zobrazuje kľúčové metriky kvality spánku
- **Spánkový index** - Hodnotenie kvality spánku v rozsahu 1-100
- **Detaily spánku** - Čas zaspania, dĺžka spánku a počet cyklov
- **Zdravotné metriky** - Pokojový pulz a variabilita srdcového rytmu (HRV)
- **Odborné rady** - Personalizované tipy na základe kvality spánku
- **Motivačné citáty** - Náhodné citáty počas načítavania dát 
- **Moderné rozhranie** - Intuitívne GUI inšpirované Ultrahuman

## Inštalácia 🔨

```bash
git clone https://github.com/adamstefanik/sleep_app.git
cd sleep_app
```
```
pip install -r requirements.txt
```

## Spustenie aplikácie

```
python main.py
```

## Štruktúra projektu

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

## Závislosti

- Python 3.8+
- Tkinter
- Standardné knižnice (json, random, time, datetime)
