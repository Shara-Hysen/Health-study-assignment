# Health Study Analysis

## Beskrivning

Detta projekt analyserar ett dataset från en hälsostudie med 800 personer. Syftet är att undersöka samband mellan variabler som ålder, vikt, blodtryck och kolesterol samt att utföra statistiska tester och simuleringar, bland annat för att analysera skillnader mellan rökare och icke-rökare.

## Innehåll

- Dataöversikt – Grundläggande information om datasetet.
- Beskrivande statistik – Medelvärden, spridningar och visualiseringar (histogram, boxplot, stapeldiagram).
- Simulering – Sjukdomsfördelning baserat på observerade proportioner.
- Konfidensintervall – Jämförelse mellan normalapproximation och bootstrap.
- Hypotesprövning – T-test och bootstrap-test för skillnader i blodtryck mellan rökare och icke-rökare.
- Poweranalys – Uppskattad sannolikhet att upptäcka en faktisk effekt.
- Linjär regression – Samband mellan ålder/vikt och blodtryck/kolesterol, inklusive residualanalys.

## Filstruktur

- data/health_study_dataset.csv – Dataset med hälsodata
- Hälsostudie.ipynb – Notebook med analys och diagram
- health_analysis.py – Modul med analysfunktioner och visualisering
- .gitignore – Ignorerade filer för Git
- requirements.txt – Pythonberoenden

## Miljö

Python version 3.13.7

## Installation och körning

1. **Klona repo:**
git clone https://github.com/Shara-Hysen/Health-study-assignment.git  
cd HEALTH-STUDY

2. **Skapa och aktivera virtuell miljö:**
python -m venv .venv  
.venv\Scripts\activate      # Windows  
source .venv/bin/activate   # Linux/macOS  

3. **Installera beroenden:**
pip install -r requirements.txt

4. **Kör Jupyter Notebook:**
jupyter notebook Hälsostudie.ipynb


## Källor

All kod är tagen från videolektionerna i samråd med ChatGPT.

