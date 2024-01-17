# Projekta darbs kursam "Lietojumprogrammatūras automatizēšanas rīki".
Daudziem cilvēkiem ir kāds hobijs, vai kāda aizraušanās pie kuras ir vēlme laik pa laikam atgriezties. Manā gadījumā aizraušanās ir datorspēles. Pēc ilgas dienas darbā, vai pēc mokošas nedēļas taisot kādu projektu, gribas atpūsties un paspēlēt kādu no vecajām bērnības spēlēm. Sākuma doma bija kāda no steam piedāvātajām, vai GOG spēlēm, taču sākot projektu nāca atklāsme, ka tādas spēles procesu taču nevarēs pārbaudīt, jo steam spēlēs bieži vien ir aizliegts izmantot jebkāda veida papildprogrammas, un tas var novest līdz konta bloķēšanai, līdz ar to nācās izdomāt bezmaksas spēles variantu, kurš joprojām būtu spējīgs parādīt, ka projekts darbojas.
  Par glābēju kļuva neliela flash spēle, kuru atradu vēl ejot 6. klasē, "Sinjid". Spēle ir vienkārša, taču lai nonāktu pie daļas, kur var sākt izmantot burvestības, ir nepieciešams iegūt trīs līmeņus. Šī programma domāta tieši tam, lai atnākot no darba un palaižot programmu, mēs varam uztaisīt kafiju un atnākt pie spēles kura jau ir gatava jautrībai.
## Plāns.
1. Atrodam spēli (Sinjid)
2. Izmantojam Selenium bibliotēku, lai lejupielādētu Y8 game launcher. Agrāk varējām spēlēt meklētājā, bet ar Flash atcelšanu, spēle ir pieejama tikai pēc lejupielādes.
    -Diemžēl šis process ievilkās, jo atjauninot urllib3 uz jaunāko versiju selenium pārstāja darboties, un tas sāka mest error katru reizi, kad tika mēģināts atvērt mājaslapu. Tika mēģināts izmantot dažādus meklētājus, beigās paliku pie ms Edge, sakarā ar to, ka tas nāk kopā ar Windows operētāj sistēmām, līdz ar to lielāka iespēja, ka uz citiem datoriem nav nepieciešams taisīt papildus izmaiņas.
3. Izmantojam pyautogui bibliotēku ar kuras palīdzību mēs varam automatizēt atvērto logu (šajā gadījumā lai netērētu pārāk daudz laiku, izmantojas os bilbiotēku lai atvērtu spēli automātiski pa virsu skriptam, līdz ar to mums tas nav jādara manuāli.
4. _Spēles procesa **Automatizēšana** ._
5. Apsvērt domu uztaisīt arī programmu, kas secīgi izpilda pārējās programmas. (edit: apsvērts, nav izdevīgi. iemeslu skatīt zemāk)
### SVARĪGA INFORMĀCIJA
1.  Sakarā ar to, ka skriptam tiek norādīti mana privātā datora folderi, kā arī skripts pielāgots darbam uz mana monitora, lai panāktu, ka skripts darbojas uz citām ierīcēm, būs nepieciešamas būtiskas koda izmaiņas. Kods izmanto attēlus kuri uzņemti noteiktā ekrāna izšķirtspējā, līdz ar to uz modernākiem monitoriem vajadzēs uzņemt jaunus attēlus lai tie darbotos, kā arī kodā ir 3 rindas, kur tiek izmantotas noteiktas koordinātes lai ieslēgtu kādu no pogām, uz citiem monitoriem poga atrodas citur! Jā, es pamanīju, ka video paskaidrojumā skatoties uz ciklu pateicu nepareizu ciparu. Tas notika nejauši.
2. video paskaidrojums https://drive.google.com/file/d/1YcyORI77rQFAra0iKf0DWnRwuk7esuci/view?usp=sharing
