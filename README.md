# Universal Personal Tutor (UPT)

## Опис проекту
UPT (Universal Personal Tutor) — це Python-додаток, який генерує індивідуальні курси навчання, забезпечує теоретичні матеріали, практичні завдання, а також зберігає прогрес користувача. Основна мета програми — надавати користувачам інтерактивну платформу для навчання.

## Функціонал програми
- Генерація навчального курсу з 5 уроків (теорія і тести).
- Збереження прогресу виконання завдань.
- Відображення правильних та неправильних відповідей у кольорах (зелений/червоний).
- Можливість зберігати курси та прогрес у файловій системі.
- Реєстрація API-ключа для доступу до сервісу генерації матеріалів.

## Архітектура даних
1. **course** — зберігає курс у вигляді списку, де кожен елемент — це словник:
   ```json
   [
       {
           "theme": "Тема уроку",
           "theory": "Теоретичний матеріал",
           "practical": "Практичні завдання"
       }
   ]
   ```

2. **progress.json** — файл, що зберігає прогрес користувача:
   ```json
   [
       0,  // Чи почато курс (0 - ні, 1 - так)
       [1, "Відповідь 1"], // Завдання виконано правильно
       [0, "Відповідь 2"]  // Завдання виконано неправильно
   ]
   ```

3. **days.json** — json файл де зберігається теорія коженого дня.
   ```json
   [
       "Теорія першого дня",
       "Теорія другого дня",
       "Теорія третього дня"
   ]
   ```

4. **course.txt** — текстовий файл з описом курсу.

5. **key.json** — json файл де зберігається API-ключ.

6. **data/** — директорія, що створюється при першому запуску. У цій папці зберігаються всі дані, включаючи ключ API, прогрес, курс тощо.

### Особливості запуску
- Якщо при запуску програми відсутня папка `data`, це означає перший запуск програми. У цьому випадку користувачу буде запропоновано зареєструвати API-ключ. Після цього програма створить папку `data` і збереже ключ у ній.
- Якщо файл `course.txt` не існує, програма не запропонує продовжити курс, а тільки почати новий. Після початку курсу програма згенерує файли курсу та збереже їх у папці `data`.
- Якщо у файлі `progres.json` перша цифра буде 0 курс не вважається початим. Якщо всі вказівники на виконане завдання будуть 1 — з'явиться повідомлення про закінчення курсу.
- При відсутності з'єднання з Інтернетом з'явиться повідомлення про це.

## Модель даних
### Структура компонентів
```plaintext
+--------------------+            +--------------------+
|      UPT.py        |            |  ui_adaptive2.py   |
|--------------------|     - >    |--------------------|
| Основна логіка     |            | II Вікно           |
+--------------------+            +--------------------+
        |
        v
+--------------------+
|  ui_adaptive1.py   |
|--------------------|
| I Вікно            |
+--------------------+

```

### Модель даних
```plaintext
+-----------------------------------------+                                      +-----------------------------------------+                  +-----------------------------------------+
|                course                   |                                      |               progress.json             |                  |                 key.json                |
|-----------------------------------------|                                      |-----------------------------------------|                  |-----------------------------------------|  
| [                                       |                                      | [                                       |                  | Зберігання ключа API.                   |
|   {                                     |                                      |   0,                                    |                  +-----------------------------------------+
|     "theme": "Тема",                    |                                      |   [1, "Відповідь 1"],                   |                  
|     "theory": "Теорія",                 |                                      |   [0, "Відповідь 2"]                    |
|     "practical": "Практика"             |                                      | ]                                       |
|   },                                    |       / "theory"                     +-----------------------------------------+
|   ...                                   |    < - - - - - - - - - - - +                
| ]                                       |                            |
+-----------------------------------------+                         +-----------------------------------------+                 
        ^    /"theme", "practical"/                                 |                 days.json               |
        |                                                           |-----------------------------------------|             
+-----------------------------------------+     / План на день      | [                                       |                 
|               course.txt                |           - >           |   "Теорія першого дня",                 |                                     
|-----------------------------------------|                         |   "Теорія другого дня",                 |                
| Згенерований текст курсу                |                         | ]                                       |                  
+-----------------------------------------+                         +-----------------------------------------+                 


```

## Інструкція з встановлення та запуску
1. Встановіть необхідні бібліотеки:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустіть програму:
   ```bash
   python UPT.py
   ```
3. На першому запуску введіть API-ключ та почніть новий курс.


## Висновки
- Universal Personal Tutor (UPT) — це додаток для персоналізованого навчання.
- Ця програма є дуже актуальною в сучасних умовах, адже не потребує особливих умов для навчання, треба лише ноутбук і підключення до Інтернету.
- Для навчання не треба няких додаткових джерел інформації, все необхідне надається зразу.
- Програма навчання охоплює багато матеріалу і вміє підлаштовуватися під особисті потреби кожного користувача.
- Для навчання не потрібно багато часу, достатньо 20-30 хвилин на день.

## Контактна інформація

- Герасимчук Олександр Сергійович
- Група: ІО-25
- Телеграм: @alexgerasym4uk
- Пошта: <alexandrgerasym4uk@gmail.com>
