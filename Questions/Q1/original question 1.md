I denna uppgift ska vi ta oss från ett givet heltal till talet ett i så få steg som möjligt om det är möjligt. I varje steg får vi göra någon av följande operationer (om de är tillåtna):

* Om talet är delbart med 7 får vi subtrahera 20 (a)
* Om talet är delbart med 5 får vi subtrahera 16 (b)
* Om talet är delbart med 2 får vi halvera det (c)
* Vi kan alltid välja att subtrahera 7 (d)

Om vi börjar med talet 70 så kan man nå ett i 4 steg genom att välja c, d, d och sist a
(70/2=35, 35-7=28, 28-7=21, 21-20=1). Om vi istället börjar med 623 så krävs 9 steg:
dcccdcdda. I denna uppgift ska du skriva metoder som returnerar antal steg men inte
presenterar vilka steg som behöver göras. Enkla skal hittar du i P/HI1029/uppgift4.

a) Skriv en metod som tar ett heltal som in-parameter och returnerar antal steg som krävs
för att nå 1 enligt ovan. Om lösning saknas ska metoden returnera -1. Använd en rekursiv
djupet först lösning. (2p)