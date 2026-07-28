# A.P.E.I.C. — Île de Cavallo

<p align="center">
  <strong>Association pour la Protection de l’Environnement de l’Île de Cavallo</strong><br>
  <em>Santuario dell'Arcipelago di Lavezzi • Corsica del Sud</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Complete-emerald?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Stack-HTML5%20%7C%20JS%20%7C%20TailwindCSS-0D9488?style=for-the-badge" alt="Stack">
  <img src="https://img.shields.io/badge/Languages-FR%20%7C%20EN%20%7C%20IT-D4AF37?style=for-the-badge" alt="Languages">
</p>

---

## 🌿 Cos'è APEIC?

**A.P.E.I.C.** (Association pour la Protection de l’Environnement de l’Île de Cavallo) è l'organizzazione fondata nel 1989 dedicata alla tutela, conservazione e valorizzazione dell'eccezionale patrimonio naturale dell'Isola di Cavallo, situata nelle Bocche di Bonifacio (Corsica del Sud).

Questo sito web istituzionale unisce un'estetica **Eco-Luxury** moderna ed elegante con il rigore dei dati scientifici prodotti e co-finanziati dall'associazione in collaborazione con il *Conservatoire Botanique National Corse (CBNC)*, *Biotope* e università partner.

---

## ✨ Caratteristiche Principali

- **🏛️ Il Manifesto & Archivio Storico**: Presentazione della storia dell'associazione dal 1989 a oggi, con un modal dedicato per la consultazione dello statuto integrale e del consiglio direttivo.
- **🌊 I Tre Pilastri (Mare, Terra, Aria)**:
  - **Mare**: Tutela delle praterie di *Posidonia oceanica* e regolamentazione degli ormeggi.
  - **Terra**: Conservazione di 426 specie floristiche (tra cui la rara *Gennaria diphylla* e il *Limonium bonifaciense*).
  - **Aria**: Protezione dell'avifauna marina (*Sterna di Dougall*, *Gabbiano corso*).
  - **Caroselli Pop-up**: Cliccando su ciascun pilastro si apre una scheda informativa arricchita con citazioni scientifiche e galleria fotografica ad alta risoluzione.
- **🔬 Centro di Ricerca Scientifico**: Modal dedicato con accesso diretto e download dei 4 report scientifici e atlanti cartografici in PDF:
  1. *Notes sur la valeur naturaliste de l’île de Cavallo* (Prof. Leonardo Filesi, 2025)
  2. *Cartographie des habitats naturels de l’île de Cavallo* (Biotope, 2017)
  3. *Atlas Cartographique des habitats naturels* (Biotope / APEIC, 2017)
  4. *Prospections sur l’île de Cavallo - Bilan Stationnel* (CBNC, 2023)
- **🌐 Support Multi-Lingua**: Traduzione istantanea senza ricaricamento in **Francese (FR)**, **Inglese (EN)** e **Italiano (IT)**.
- **💳 Modulo di Raccolta Fondi**: Form integrato con preset di donazione (25 €, 50 €, 100 €, personalizzato) per sostenere le azioni botaniche sul campo.
- **📱 Responsive & Accessibility First**: Perfetta adattabilità su desktop, tablet e dispositivi mobili.

---

## 🛠️ Architettura del Progetto

```
apeic/
├── index.html              # Landing page principale e logica JS/i18n
├── server.py               # Server locale di sviluppo Python (porte 8000)
├── README.md               # Documentazione del progetto
├── .gitignore              # Esclusioni per Git / GitHub
├── .gitattributes          # Configurazione codifica e fine riga Git
├── Documenti/              # Report e studi scientifici in formato PDF
│   ├── 03_CR_Cavallo_CBNC_12102023.pdf
│   ├── AtlasCartoCavalloFinal.pdf
│   ├── CartoCavallo_Final3.pdf
│   └── valeur naturaliste de l'Ile de Cavallo_Ci joint LF 18 11 2024.pdf
└── assets/                 # Risorse grafiche ad alta risoluzione (PNG/JPEG)
    ├── hero_background.png
    ├── marine_life.png
    ├── posidonia_meadow.png
    ├── marine_reserve_bonifacio.png
    ├── terrestrial_flora.jpeg
    ├── limonium_bonifaciense.png
    ├── juniper_maquis.png
    ├── sea_swallow.png
    ├── audouins_gull.png
    └── dougalls_tern.png
```

---

## 🚀 Come Eseguire in Locale

Il sito è costruito in **HTML5, Vanilla JavaScript** e **Tailwind CSS**. Non richiede compilazione Node.js ed è pronto all'uso.

### Avvio rapido con Python:
```bash
python server.py
```
Apri il browser su: **`http://localhost:8000/`**

---

## 📤 Come Caricare su GitHub

### Opzione 1: Da Terminale (Git CLI)
Se hai Git installato, esegui i seguenti comandi nella cartella `apeic`:

```bash
git init
git add .
git commit -m "Initial commit: APEIC website release"
git branch -M main
git remote add origin https://github.com/IL_TUO_USERNAME/apeic.git
git push -u origin main
```

### Opzione 2: Con GitHub Desktop
1. Apri **GitHub Desktop**.
2. Clicca su **File > Add local repository...** e seleziona la cartella `c:\Users\giobo\Desktop\apeic`.
3. Clicca su **Publish repository** per caricarlo direttamente sul tuo account GitHub.

---

## 📄 Licenza & Diritti

© A.P.E.I.C. — Association pour la Protection de l’Environnement de l’Île de Cavallo. Tutti i diritti riservati sui documenti scientifici e sui marchi ufficiali.
