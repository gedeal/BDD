# BDD
Python Test - BDD


#  Del 1 -----------------------------------------
Du ska beskriva och testa ett enkelt system för en webbutik som säljer böcker. Systemet
har följande enkla krav:

- Användaren kan lägga böcker i en varukorg
- Användaren kan ta bort böcker från varukorgen
- Varukorgen visar alltid aktuell summa och antal böcker
- Om användaren försöker lägga en bok som redan finns i varukorgen ska antalet
av just den boken öka istället för att skapa en ny rad
- Det skall gå att tömma varukorgen helt

### Uppgiften:
1. Skriv tydliga scenarier i Gherkin som beskriver ovanstående krav. Använd gärna
Scenario Outline där det passar.
2. Implementera step-filerna i Python med hjälp av Behave.
3. Din Python-kod behöver inte kopplas mot en riktig webbsida eller databas, det
räcker med att simulera funktionaliteten med hjälp av enklare Python-klasser

## Del 2 -----------------------------------------
Här kommer du behöva tänka till och forska på egen hand. Du skall vidareutveckla
uppgiften till att inkludera ytterligare funktionalitet samt några svårare testfall.
Extra krav som skall implementeras (du skall göra minst tre av dem):
- Rabattfunktion. Om användaren köper fler än tre böcker skall hon få 10% rabatt
på hela kundkorgen. Testa flera olika fall, inklusive värden som är osannolika som
-1000 och 64000 böcker.
- Lagerhantering. Varje bok skall ha en lagerstatus. Om användaren försöker köpa
fler exemplar än vad som finns i lagret, visas ett tydligt meddelande och antalet
begränsas till lagersaldot.
- Login. Användaren måste logga in med giltiga användaruppgifter innan köpet kan
genomföras. Testa både lyckade och misslyckade inloggingar med Scenario
Outline.
- Beställningshistorik. Användaren skall kunna se historiken över sina tidigare
beställningar. Testa att beställningar visas korrekt.
- Kvitto. När en beställning är genomförd skickas ett kvitto automatiskt via e-post
(detta simulerar du i Python, du behöver inte skicka mailet på riktigt). Testa att
kvittot skapas och skickas iväg.

### Uppgiften:
1. Gör research online för att hitta bra sätt att implementera funktionerna i Python,
utan att använda komplex webbteknik som ramverk och liknande.
2. Skriv tydliga och underhållbara scenarier i Gherkin som testar varje vald
extrafunktion.
3. Implementera steps-definitionerna i Behave och Python. Använd klasser,
funktioner och variabler för att simulera funktionerna.
4. Se till att testfallen fungerar och kör utan fel med kommandot behave.