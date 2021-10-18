# Spis operacji, które kolejno przeprowadzaono na oryginalnych danych aby otrzymać dane wyjściowe:

I. Otrzymanie pliku music_details
- Usunięcie danych związanych z datą wejścia utworu na listę, oraz miejscami zajmowanymi w poszczególnych tygodniach
- Posortowanie utworów na podstawie nazwy wykonawcy
- Zmiana indeksów w posortowanej tabeli

II. Otrzymanie pliku music_top_list
- Podział otrzymanych danych tak, aby zajmowane miejsce w poszczególnych tygodniach było wierszem, co powoduje powstanie dwóch nowych kolumn: zmiennej, która została nazwana 'week',
ponieważ zawiera dane o tym, w którym tygodniu utwór jest notowany oraz wartości o nazwie 'place', która zawiera informację o zajętym miejscu. Dodatkowo pomijane są szczegółowe dane o piosenkach,
które zostały zamisane w pliku music_details (gatunek utworu, czas trwania), 
- Usunięcie pustych rekordów
- Posortowanie utworów na podstawie nazwy wykonawcy oraz ponowna indeksacja elementów
- Zamiana typu danych kolumnty 'date.entered' na DataFrame
- podmiana nieczytelnych wartości kolumny 'week'  na liczby całkowite (postaci x1st.week -> 1)
- Zmiana wartości w kolumnie 'date.entered' oraz 'week', aby każdy wiersz przedstawiał kalendarzowy tydzień i miejsce, które zajmuje utwór
- podmiana nazw kolumn na bardziej czytelne ('date.entered' -> 'week start'; 'week' -> 'week.end')