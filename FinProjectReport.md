# Report on the final project 

## API part

    1.Баг c некорректным логином и паролем.
        - Реализация:
            Выполнить API запрос на вход с незарегистрированного аккаунта.
        - Ожидание: Код ответа: 404
        - Реальность: Код ответа: 401
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/FIrstUI.png?raw=true)
    
    2.Баг c некорректным паролем.
        - Реализация:
            Выполнить API запрос на вход с валидного аккаунта,
        но с неправильным паролем.
        - Ожидание: Код ответа: 404
        - Реальность: Код ответа: 401
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/SecondUI.png?raw=true)

    3.Баг c пустым полем логина и пароля.
        - Реализация:
            Выполнить API запрос на вход с пустыми полями 
        пароля и логина.
        - Ожидание: Код ответа: 401
        - Реальность: Код ответа: 302, возвращает в хедерах 
        урл главной страницы и куки
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/ThirdUI.png?raw=true)

    4.Баг c добалвением пользователя.
        - Реализация:
            Выполнить API запрос на создание пользователя
        с вадидными значениями.
        - Ожидание: Код ответа: 201
        - Реальность: Код ответа: 210
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/FourthUI.png?raw=true)

    5.Баг c добалвением пользователя без отчества.
        - Реализация:
            Выполнить API запрос на создание пользователя
        с вадидными значениями, но без отчества.
        - Ожидание: Код ответа: 201
        - Реальность: Код ответа: 210
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/FifthUI.png?raw=true)

    6.Баг c добалвением пользователя с значениями полей больше отведенных. 
        - Реализация:
            Выполнить API запрос на создание пользователя
        с невадидными значениями, больше выделенного БД.
        - Ожидание: Код ответа: 400
        - Реальность: Код ответа: 500
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/SixthUI.png?raw=true)

    7.Баг смены пароля. 
        - Реализация:
            Выполнить API запрос на смену пароля.
        - Ожидание: Код ответа: 200
        - Реальность: Код ответа: 204
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/SeventhUI.png?raw=true)

    8.Баг смены пароля на пустоту. 
        - Реализация:
            Выполнить API запрос на смену пароля с пустым полем.
        - Ожидание: Код ответа: 200
        - Реальность: Код ответа: 204, можно поменять пароль на пустую строку.
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/EighthUI.png?raw=true)


## UI part

    1.Баг c отсутствием отчества в бд.
        - Реализация:
            Выполнить регистрацию с валидными данными.
        - Ожидание: Создание пользователя с корректными данным в БД.
        - Реальность: Отсутствие в БД отчества
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/FirstAPI.png?raw=true)

    2.Баг создание пользователя без отчества.
        - Реализация:
            Выполнить регистрацию с валидными данными, но без отчества.
        - Ожидание:Ошибка данных пользователя, отсутствие отчества.
        - Реальность: Создание пользователя без отчества
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/SecondAPI.png?raw=true)
    
    3.Баг количества символов у поля name.
        - Реализация:
            Выполнить регистрацию с максимальным значением поля name.
        - Ожидание: Успешная регистрация.
        - Реальность: Неуспешная регистрация, у поля name меньше 255 символов.

    4.Баг с большой фамилией.
        - Реализация:
            Выполнить регистрацию с максимальным значением поля surname, 
        после этого выполнить logout или переход по активным ссылка.
        - Ожидание: Успешная регистрация, logout и переход по ссылкам.
        - Реальность: Кнопки перехода и logout-а исчезают, их невозможно использовать.
![Image text](https://github.com/DmtrSuch/2022-1-QAPYTHON-VK-D-Suchkov/blob/finProject/ImageForReport/ThirdAPI.png?raw=true)