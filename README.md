# theWhyKingz
---
this repository was created for test task

structure:
```
|
|- data        -> folder with external data
|
|- notebooks   -> folder with notebooks
|
|- src         -> folder with necessary functions
|
 ```
 
to run jupyter notebook with necessary env run in terminal command

```
poetry update
poetry run jupyter notebook
```

Задачи:
1. Исследование данных, поиск зависимостей и скрытых переменных;
2. Выдвижение и проверка гипотез;
3. Разработка и презентация прогнозных моделей;
4. Поддержка, обновление и оптимизация разработанных моделей.


Тестовое задание.
Файл содержит данные по игровой активности, где:
user - уникальный идентификатор пользователя;
session - уникальный идентификатор игровой сессии;
start - начало сессии;
finish - соответсвенно, ее завершение;
score - сумма набранных за сессию очков. Согласно игровому процессу, очки начисляются за успешные действия игроком, и следовательно, снимаются за неуспешные.
	Положительный результат записывается пользователю на баланс и позволяет продолжить игру. Отрицательный - вынуждает пользователя ждать, либо платить, чтобы продолжать.
rounds - число действий, за которые начислялись либо снимались очки.

На основании предоставленных данных, постарайтесь, пожалуйста, ответить на следующие вопросы:
1. Какая в среднем длина жизни пользователя в игре;
2. Сколько пользователей можно ожидать в течение первого полугодия 2020 года. Отобразите в динамике по месяцам;
3. Какими свойствами обладает группа пользователей, чей показатель длины жизни ниже среднего;
4. Соответственно, какими свойствами обладает группа, чья длина жизни выше среднего;
Также, спрогнозируйте вероятность потери пользователя по итогам его сессии.

Держите, пожалуйста, во внимании:
 - данные преднамерено содержат ошибки;
 - статистика отображает лишь один год из жизни гипотетической игры;
 - оцениваться будут не только ответы, но и способы их получения, поэтому постарайтесь предоставить понятное и развернутое решение.

