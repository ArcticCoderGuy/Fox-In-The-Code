## 🔧 Tehtävän vaatimukset (Task 2: Bootstrap)
## 

Sivuston tulee sisältää seuraavat osiot ja toiminnallisuudet:

---

### 1. HTML5 + Bootstrap
- Sivusto rakennetaan käyttäen HTML5-rakennetta
- Bootstrap-komponentteja käytetään ulkoasuun ja responsiivisuuteen

---

### 2. Navigointi (Navbar)
- Yläpalkki, jossa on vähintään kolme linkkiä:
  - Etusivu
  - Tietoa meistä
  - Ota yhteyttä
  - Luotu oma nav.html-tiedosto juureen jonka ohjaa kaikkia sivuja eli "Lean"-hengessä muutokset tehdään vain yhteen paikkaan vakioidusti.

---

### 3. Hero-osio / Etusivun pääkuva
- Näyttävä isokuva (hero-image tai carousel) heti alussa
- Sisältää ison otsikon ja painikkeen (CTA = Call to Action)

---

### 4. Tietolaatikot / Kolumnit
- Kolme laatikkoa rinnakkain Bootstrapin `col`-tyylillä
- Esim. kolmen palvelun esittely (3 columns in a row)

---

### 5. Tietoa meistä -osio
- Bootstrapin card-komponentilla toteutettu osa
- Sisältää kuvia ja tekstiä
- Esim. tiimimme tai yritysesittely

---

### 6. Yhteydenottolomake
- Bootstrapin lomake-elementit:
  - input
  - textarea
  - button
- Ei tarvitse toiminnallisuutta, pelkkä ulkoasu riittää

---

### 7. Responsiivisuus
- Sivun tulee skaalautua eri laitteilla:
  - puhelin
  - tabletti
  - tietokone
- Bootstrapin grid-järjestelmä hoitaa suurimman osan

---

> ✅ Tämä pohja auttaa varmistamaan, että kaikki tehtävän vaatimukset täyttyvät.


-------------------------------------

# Fox-In-The-Code - verkkosivu

**Tervetuloa Fox-In-The-Code ensimmäiseen julkaisuun!**

Tämä projekti toteutettiin HTML5-, CSS- ja Bootstrap5 -teknologioilla.  
Sivuston tarkoituksena on esitellä yrityksen brändiä ja palveluita, korostaen "Define → Build → Finish" -periaatteita.

---

## 🔥 Projektin sisältö:

- Hero-sektio isolla kuvalla ja sloganilla
- Navigointipalkki kolmella linkillä (Etusivu, Tietoa Meistä, Ota Yhteyttä)
- Responsiivinen layout Bootstrapilla
- Moderni äänisoitin Wavesurfer.js-kirjastolla
- Favicon
- CSS-tyylitiedosto erillisenä
- Testattu Live Serverillä ja mobiilissa

---

## 🛠 Käytetyt teknologiat:

- HTML5
- CSS3
- Bootstrap 5.3
- Wavesurfer.js

---

## 📋 To-Do & jatkokehitysideoita:

- Yhteydenottolomakkeen lisääminen
- Tietoa Meistä -osio (Bootstrap card-komponentti)
- Footer-osio (esim. yhteystiedot ja some-linkit)

---

## 📱 Responsiivisuus:

Sivusto toimii mobiilissa, tabletilla ja desktopilla.  
Testattu Windows ja Android -laitteilla.

---

## 🎯 Valmis julkaisu:

Tämä versio täyttää peruskurssin vaatimukset ja palautuskriteerit:

✅ HTML5 + Bootstrap  
✅ Navigointi (3 linkkiä)  
✅ Hero-kuva ja CTA  
✅ Responsiivisuus  
✅ Favicon  
✅ Wavesurfer.js -äänisoitin  

---

Materiaalit: https://simpleicons.org/?q=PostGe


Lisälätinät: 

🚀 Fox-In-The-Code – verkkosivu
Ensimmäinen julkaisu – moderni ja vakioitu verkkosivusto arkkitehtonisella otteella.

Tämä sivusto on rakennettu HTML5-, CSS- ja Bootstrap 5 -teknologioilla, ja sen ylläpito tapahtuu tehokkaasti nav.html-moduulilla ja FileZilla FTP -siirrolla. Sivusto perustuu "Define → Build → Finish" -ajatteluun ja toimii kaikilla päätelaitteilla.

✅ Tehtävän vaatimukset (Task 2: Bootstrap)
Kohta	Toteutus
HTML5 + Bootstrap	Kyllä
Navigointipalkki 3+ linkillä	Kyllä
Hero-kuva + CTA	Kyllä
3 tietolaatikkoa (col)	Kyllä
"Tietoa meistä" -kortit	Kyllä
Yhteydenottolomake	Kyllä
Responsiivinen rakenne	Kyllä
Favicon	Kyllä

🔧 Teknologiat & Rakenteet
HTML5: Semanttinen ja selkeä rakenne

CSS3: Tyylit toteutettu erillisessä styles.css-tiedostossa

Bootstrap 5.3: Responsiivisuus ja grid-järjestelmä

JavaScript (Fetch): Dynaaminen nav.html-lataus joka sivulle

FileZilla FTP: Tiedostonsiirrot palvelimelle

Live-server testaus: VS Code Live Server ja mobiilitesti

📁 Rakenne ja modulaarisuus
index.html, about.html, contact.html, services.html – sivut

nav.html – vakioitu navigaatio, joka ladataan JavaScriptillä

styles.css – yksi yhteinen tyylitiedosto

/images – kuvakansio

/favicon.ico – selaimen välilehti-ikoni

script.js – valikkotoiminto ja navin dynaaminen lataus

📤 FTP-siirto (FileZilla)
Sivuston tiedostot siirrettiin julkaisupalvelimelle seuraavasti:

Asennettiin FileZilla

Yhdistettiin CPanelin tarjoamaan FTP-osoitteeseen

Luotiin uusi FTP-tili, jonka kansiopolku oli foxinthecode.fi/public_html

Siirrettiin *.html, styles.css, images/, favicon.ico yms.

Varmistettiin oikea juurikansio

Testattiin selaimessa (esim. https://foxinthecode.fi/index.html)

👉 Huom: nav.html:n muutokset päivittyvät automaattisesti kaikille sivuille, kun vain yksi tiedosto päivitetään palvelimelle.

📱 Responsiivisuus & Design
Bootstrapin grid takaa skaalautuvuuden

Testattu Android-puhelimella, Windows-laitteilla, eri selainmoottoreilla

Burger-valikko toimii <768px näkymässä

💡 Mahdollisia jatkokehityksiä
Lomakkeen backend (esim. PHP tai Google Forms)

SEO-metaanalyysi

Open Graph -kuvat some-jakoon

Tuki useammille kielille

Wavesurfer.js äänikortille (valinnainen lisä)

🧠 Oppimiskokemuksia
FTP:n kanssa sattui ja tapahtui: alku oli tervanjuontia (polut, oikeudet, timeoutit)

Lopulta kaikki saatiin kuntoon: testattiin manuaalisesti ja opittiin FileZilla kunnolla

Modulaarisuus = Lean-ajattelu: nav.html toi säästöä ylläpidossa

GitHubissa versiointi, FileZilla siirrossa

🔗 Linkit & julkaisu
Julkaistu osoitteessa:
🌐 https://foxinthecode.fi (tai vastaava CPanel-julkaisuosoite)

