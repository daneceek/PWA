## Bootstrap

Bootstrap je open-source framework pro vývoj webových aplikací. Obsahuje HTML a CSS šablony pro formuláře, tlačítka, navigace a další komponenty. Bootstrap je vyvíjen a udržován na platformě GitHub.
 https://getbootstrap.com/docs/5.3/getting-started/introduction/

#### Použití

Přidejte tyto řádky do vašeho HTML souboru.

###### CSS


```
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
```

###### JS
```JS
 <!-- Bootstrap JS a jQuery -->
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
```


## Grid systém
### Struktura grid systému
Grid systém se skládá z řádků (.row) a sloupců (.col), které jsou umístěny uvnitř kontejneru (.container nebo .container-fluid).

### Kontejnery
Kontejnery jsou základní stavební kameny rozvržení Bootstrapu. Existují dva typy kontejnerů:

* .container: Pevná šířka, která se přizpůsobuje různým velikostem obrazovky.
* .container-fluid: Má šířku 100% bez ohledu na velikost obrazovky.

### Řádky a sloupce
* .row: Používá se pro vytvoření řádků, do kterých umisťujeme sloupce.
* .col: Definuje sloupce uvnitř řádků. Každý řádek může mít až 12 sloupců.

### Rozdělení na různé velikosti sloupců
Každý sloupec zabírá určitou část 12-sloupcové mřížky. K tomu se používají třídy, jako například .col-6, které definují, kolik sloupců z celkových 12 bude prvek zabírat. Např. .col-6 znamená, že sloupec bude zabírat 6/12 šířky, což je polovina.

### Responzivní grid systém
Bootstrap umožňuje vytvářet responzivní design, který se přizpůsobuje různým velikostem obrazovek. Můžeme určit, jak se budou sloupce chovat na různých zařízeních (mobilní telefony, tablety, desktop). K tomu slouží následující třídy:

* .col-sm-: Pro malé obrazovky (≥ 576px)
* .col-md-: Pro střední obrazovky (≥ 768px)
* .col-lg-: Pro velké obrazovky (≥ 992px)
* .col-xl-: Pro extra velké obrazovky (≥ 1200px)

### Přístupnost
Kromě atributu aria-label existuje v HTML celá řada dalších atributů a vlastností, které pomáhají zlepšit přístupnost webu, zejména pro uživatele se zdravotním postižením. Mezi ně patří:

* alt (alternativní text pro obrázky)
Atribut alt se používá u značky <img>, aby poskytl popis obrázku pro uživatele, kteří si obrázky nemohou zobrazit (například kvůli technickým omezením nebo proto, že používají čtečky obrazovky).
Příklad:
html

``
<img src="obrazek.jpg" alt="Popis obrázku">
``
* aria-hidden="true" (skrytí prvků pro čtečky obrazovky)
Používá se pro skrytí prvků, které nemají být čteny čtečkami obrazovky, ale jsou vizuálně viditelné pro běžné uživatele.
Příklad:
html

   ``<div aria-hidden="true">Tento text nebude čten čtečkou obrazovky.</div>
   ``
* role (přidání role prvku)
Atribut role umožňuje definovat specifickou funkci prvku pro čtečky obrazovky. Například můžete definovat, že určitý prvek je tlačítko, navigace, dialogové okno atd.
Příklad:
html
    
    ``<div role="button">Tlačítko</div>
    ``
* tabindex (řízení pořadí při procházení klávesnicí)
Atribut tabindex určuje, v jakém pořadí se budou prvky zaměřovat při použití klávesy "Tab". Užitečné pro zajištění lepší klávesové navigace.
Příklad:
html

  ``
  <button tabindex="1">První tlačítko</button>
  <button tabindex="2">Druhé tlačítko</button>``

* aria-describedby (odkaz na popisný prvek)
Tento atribut propojuje prvek s jiným prvkem na stránce, který poskytuje popis daného prvku. Čtečka obrazovky přečte tento popis.
Příklad:
html

   ``
   <span id="popis">Popis tlačítka</span>
   <button aria-describedby="popis">Klikni</button>
   ``
* aria-label (alternativní popis pro prvek)
* aria-labelledby (odkaz na popisný prvek)
* aria-live (určení, zda se má prvek aktualizovat v reálném čase)
* aria-pressed (určení stavu tlačítka)
* aria-expanded (určení stavu rozbalovacího seznamu)
* aria-controls (odkaz na ovládaný prvek)
* aria-haspopup (určení, zda prvek otevírá submenu)
* aria-hidden (skrytí prvku pro čtečky obrazovky)
* aria-describedby (odkaz na popisný prvek)

## Jednotky v CSS
### Absolutní jednotky
Absolutní jednotky mají pevnou hodnotu a nezávisí na velikosti obrazovky nebo nastavení uživatele. Mezi absolutní jednotky patří:
* px: pixely (1 pixel na obrazovce)
* cm: centimetry
* mm: milimetry
* in: palce (1 palec = 2.54 cm)
* pt: body (1 bod = 1/72 palce)
* pc: pica (1 pica = 12 bodů)

### Relativní jednotky
Relativní jednotky jsou závislé na velikosti obrazovky nebo nastavení uživatele. Mezi relativní jednotky patří:
* em: relativní k jednotkové velikosti písma
* rem: relativní k velikosti písma kořenového prvku (<html>)
* vw: relativní k šířce viewportu (1vw = 1% šířky viewportu)
* vh: relativní k výšce viewportu (1vh = 1% výšky viewportu)
* %: relativní k rodičovskému prvku (např. šířka 50% znamená polovinu šířky rodičovského prvku)
* ch: relativní k šířce znaku "0" v aktuálním písmu
* ex: relativní k výšce písmene "x" v aktuálním písmu
* vmin: relativní k menší z hodnot vw nebo vh
* vmax: relativní k větší z hodnot vw nebo vh
* fr: relativní k zbytku volného prostoru v flexboxu