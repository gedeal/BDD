#  Del 1 -----------------------------------------
Du ska beskriva och testa ett enkelt system för en webbutik som säljer böcker. 
Systemet har följande enkla krav:

- F001 - Användaren kan lägga böcker i en varukorg
- F002 - Användaren kan ta bort böcker från varukorgen
- F003 - Varukorgen visar alltid aktuell summa och antal böcker
- F004 - Om användaren försöker lägga en bok som redan finns i varukorgen ska antalet
av just den boken öka istället för att skapa en ny rad
- F005 -Det skall gå att tömma varukorgen helt

### Uppgiften:
1. Skriv tydliga scenarier i Gherkin som beskriver ovanstående krav. Använd gärna
Scenario Outline där det passar.
2. Implementera step-filerna i Python med hjälp av Behave.
3. Din Python-kod behöver inte kopplas mot en riktig webbsida eller databas, det
räcker med att simulera funktionaliteten med hjälp av enklare Python-klasser
