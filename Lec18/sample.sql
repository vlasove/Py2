/* Первый запрос на создание таблицы для хранения информации про книги */
CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, pages INT, price REAL);

/* Несколько запросов по работе с данными в таблице books */
/* Допустим у меня есть книга ("LOTR:1", "J.J.Tolkin", 750, 14.99) */
INSERT INTO books (title, author, pages, price) VALUES("LOTR:1", "J.J.Tolkin", 750, 14.99);

/* Теперь хочу прочитать из таблицы */
SELECT *  FROM books;

/* Теперь я понял, что ошибься в цене товара, хочу поменять */
UPDATE books SET price = 149.99 WHERE title = "LORT:1";

/* Теперь удалим какую-нибудь книжку */
DELETE FROM books WHERE title = "LOTR:1";
