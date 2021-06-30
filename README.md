# REST-API
REST API - kolekcja słów

W ramach zadania zostało stworzone REST API. Przeze mnie uruchamiane było przez POSTMAN. Projekt wykonany przy użyciu Flask i języka Python.
1.	Od początku jest utworzonych kilka początkowych słów. 
2.	Dodawanie odbywa się w następujący sposób 
{
    "word":{
        "id": 12,
        "word": "cake"
    }
}  

– nie można dodać dwóch słów o takim samym ID, przy metodzie POST dodajemy, przy metodzie PUT aktualizujemy słowo. Do obu metod jest ten sam URL -> http://127.0.0.1:5000/api/word
 
3.	Usuwanie -> podajemy po ukośniku id wyrazu, który chcemy usunąć. Przykładowy URL -> http://127.0.0.1:5000/api/word/1
4.	Pobieranie wszystkich unikalnych słów z kolekcji -> generuje się lista, która zawiera same słowa, bez numerów ID i jest wyświetlana URL -> http://127.0.0.1:5000/api/word/unic
5.	Sprawdzanie liczby wystąpień -> utworzony jest słownik z unikalnymi słowami i dodawane są do niego liczby wystąpień danych słów. URL -> http://127.0.0.1:5000/api/word/count 
