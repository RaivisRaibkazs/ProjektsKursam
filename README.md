# Projekta darbs kursam "Lietojumprogrammatūras automatizēšanas rīki".
Daudziem cilvēkiem ir kāds hobijs, vai kāda aizraušanās pie kuras ir vēlme laik pa laikam atgriezties. Manā gadījumā aizraušanās ir datorspēles. Pēc ilgas dienas darbā, vai pēc mokošas nedēļas taisot kādu projektu, gribas atpūsties un paspēlēt kādu no vecajām bērnības spēlēm. Sākuma doma bija kāda no steam piedāvātajām, vai GOG spēlēm, taču sākot projktu nāca atklāsme, ka tādas spēles procesu taču nevarēs pārbaudīt, līdz ar to nācās izdomāt bezmaksas spēles variantu, kurš joprojām būtu spējīgs parādīt, ka projekts darbojas, un ar minimālām koda izmaiņām, to varētu palaist uz vitiem datoriem bez spēles pirkšanas.
  Par glābēju kļuva neliela flash spēle, kuru atradu vēl ejot 6. klasē, "Sinjid". Spēle ir vienkārša, taču lai nonāktu pie daļas, kur var sākt izmantot burvestības, ir nepieciešams iegūt piecus līmeņus. Šī programma domāta tieši tam, lai atnākot no darba un palaižot programmu, mēs varam uztaisīt kafiju un atnākt pie spēles kura jau ir gatava jautrībai.
## Plāns.
1. Atrodam spēli (Sinjid)
2. Izmantojam Selenium bibliotēku, lai lejupielādētu Y8 game launcher. Agrāk varējām spēlēt meklētājā, bet ar Flash atcelšanu, spēle ir pieejama tikai pēc lejupielādes.
  1. Diemžēl šis process ievilkās, jo kāds izdomāja atjaunināt urllib3 uz jaunāko versiju, un tas sāka mest error katru reizi, kad tika mēģināts atvērt mājaslapu. Tika mēģināts izmantot dažādus meklētājus, beigās paliku pie ms Edge, sakarā ar to, ka tas nāk kopā ar Windows operētāj sistēmām, līdz ar to lielāka iespēja, ka uz citiem datoriem nav nepieciešams taisīt papildus izmaiņas.
3. Uztaisīt programmu, kas nolasa spēles saturu, lai varam saprast, kuras pogas vajag izmantot.
4. _Spēles procesa **Automatizēšana** ._
5. Apsvērt domu uztaisīt arī programmu, kas secīgi izpilda pārējās programmas.
### Turpinājums sekos...
