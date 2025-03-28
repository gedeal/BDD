#  Del 2 -----------------------------------------

Här kommer du behöva tänka till och forska på egen hand. Du skall vidareutveckla
uppgiften till att inkludera ytterligare funktionalitet samt några svårare testfall.
Extra krav som skall implementeras (du skall göra minst tre av dem):

- F002_1) Rabattfunktion. Om användaren köper fler än tre böcker skall hon få 10% rabatt
på hela kundkorgen. Testa flera olika fall, inklusive värden som är osannolika som
-1000 och 64000 böcker.


- F002_2) Lagerhantering. Varje bok skall ha en lagerstatus. Om användaren försöker köpa
fler exemplar än vad som finns i lagret, visas ett tydligt meddelande och antalet
begränsas till lagersaldot.


- F002_3) Login. Användaren måste logga in med giltiga användaruppgifter innan köpet kan
genomföras. Testa både lyckade och misslyckade inloggingar med Scenario
Outline.


- F002_4) Beställningshistorik. Användaren skall kunna se historiken över sina tidigare
beställningar. Testa att beställningar visas korrekt.


- F002_5) Kvitto. När en beställning är genomförd skickas ett kvitto automatiskt via e-post
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