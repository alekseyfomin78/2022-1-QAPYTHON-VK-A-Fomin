#### Задача
 * Тестирование портала https://target.my.com
 * Настроить окружение для запуска API-тестов
 * API-тесты должны запускаться через марк -m API

     API ( 7 баллов):
     * Написать API клиент, который будет иметь возможность авторизовываться на портале (3 балла)
     * Написать тест на создание кампании любого типа через API, кампания после теста должна удалиться автоматически  (2 балла)
     * Написать тест на создание сегмента через API и проверку того, что сегмент создан (1 балл)
     * Написать тест на удаление сегмента через API (1 балл)

#### Необходимые требования: 
* Зафиксировать в requirements.txt конкретные версии библиотек по аналогии с [requirements.txt из репозитория](https://github.com/Starborn933/education-vk-python-2022/blob/main/requirements.txt). Версии должны быть выпущены до 24.02.2022, сверяйтесь по странице на pypi и проверяйте, что в requirements.txt отсутствуют неиспользуемые в рамках ваших домашек зависимости.
* Положить в корень репозитория (прямо в ветку main, без отдельного Pull Request) целиком папку .github/workflows из репозитория. Этот скрипт активирует для вас GitHub Actions - Continious Integration систему от GitHub. Этот механизм позволит вам видеть ошибки, которые возникают при запуске домашки не на локальной машине (напоминаем - домашки должны запускаться не только у вас), и крайне желательно эти ошибки исправлять до создания Pull Request'а.
Подробнее о GitHub actions вы можете прочесть в соответствующем посте в блоге на портале.
* Еще раз напоминаем, что ветка домашнего задания и папка домашнего задания должна называться как homeworkN, где N - номер домашки. Например, homework3. Это обязательное условие для работы  GitHub Actions

#### Самостоятельное задание, без обязательного добавления кода в дз и сдачи на проверку
 * Адаптировать UI-тесты из ДЗ №2 под использование  API-клиента в тех местах, где это возможно и необходимо:
    * Авторизация
    * Создание сегмента
    * etc


#### Советы
 * Тесты *НЕ* должны быть зависимыми
 * Все тесты *ДОЛЖНЫ* проходить
 * Тесты *ОБЯЗАТЕЛЬНО* должны что-то проверять. Например, если мы что-то создали, то необходимо проверять, что оно создалось.
 * Тесты *ДОЛЖНЫ* уметь запускаться параллельно и проходить в параллельном режиме (не конфликтовать)
 * Тесты *ДОЛЖНЫ* уметь запускаться несколько раз подряд
 
#### Срок сдачи ДЗ
 До 6 апреля (включительно)

    
     