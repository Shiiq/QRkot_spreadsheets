# QRkot_w/_spreadsheets
### Учебный проект QRKot
Учебное приложение для гипотетического благотворительного фонда **QRKot**. Фонд собирает пожертвования на различные целевые проекты.  

В QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, 
которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. 
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.  
  
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: 
они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в 
первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в 
Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта 
все неинвестированные пожертвования автоматически вкладываются в новый проект.

Посредством GOOGLE_DRIVE_API и GOOGLE_SPREADSHEETS_API интегрирована возможность формирования отчёта в гугл-таблице. 
В таблице должны быть закрытые проекты, отсортированные по 
скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

Как установить проект:  
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Shiiq/QRkot_spreadsheets
```

```
cd app
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить приложение:

```
uvicorn main:app
```

#### Автор: Киряков Петр, 2022