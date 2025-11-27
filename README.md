# Health Study Analysis

## Beskrivning

Detta projekt analyserar ett dataset från en hälsostudie med cirka 800 personer. Syftet är att undersöka samband mellan variabler som ålder, vikt, blodtryck och kolesterol samt att utföra statistiska tester och simuleringar för att belysa skillnader mellan grupper, t.ex. rökare och icke-rökare.

## Filstruktur

- data/health_study_dataset.csv – Dataset med hälsodata.
- Hälsostudie.ipynb – Jupyter Notebook där hela analysen körs steg för steg med kommentarer och visualiseringar.
- health_analysis.py – Pythonmodul med klasser och funktioner för dataanalys och visualisering.
- .gitignore – Git ignore-fil.
- requirements.txt – Lista över Pythonpaket som behövs för att köra projektet.

## Miljö

Python version 3.13.7

## Installation och körning

1. Klona repo:
git clone https://github.com/Shara-Hysen/Health-study-assignment.git
cd HEALTH-STUDY

2. Skapa och aktivera virtuell miljö:
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS  

3. Installera beroenden:
pip install -r requirements.txt

4. Kör Jupyter Notebook:
jupyter notebook Hälsostudie.ipynb


## Funktioner och innehåll

- Dataöversikt: Läser in och visar grundläggande info om datasetet.
- Beskrivande statistik: Sammanfattar variabler och skapar visualiseringar (histogram, boxplot, stapeldiagram).
- Simulering: Simulerar sjukdomsfördelning baserat på data.
- Konfidensintervall: Beräknar och jämför konfidensintervall med normalapproximation och bootstrap.
- Hypotesprövning: Jämför blodtryck mellan rökare och icke-rökare med t-test och bootstrap.
- Poweranalys: Uppskattar styrkan i hypotesprövningen via simulering.
- Linjär regression: Analyserar samband mellan ålder, vikt och blodtryck/kolesterol med regression och residualanalys.


