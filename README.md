# Hearty - онлайн-знакомства

## Техническое задание

### Введение

    Цель: Разработать полноценное веб-приложение "Сайт знакомств" с использованием фреймворка Django.
    Описание: Веб-приложение предоставляет платформу для знакомств и обмена сообщениями между пользователями. Приложение должно обладать множеством функциональностей, моделей и связей, а также включать использование сигналов, REST API и полнотекстовый поиск в базе данных.

#### Требования

##### Функциональные требования:

    1. Регистрация и аутентификация пользователей.
    2. Создание профиля пользователя с информацией о себе, фотографиями и предпочтениями.
    3. Поиск и просмотр профилей других пользователей.
    4. Возможность отправлять и получать сообщения между пользователями.
    5. Возможность оценивать и комментировать профили пользователей.
    6. Реализация алгоритма для подбора рекомендаций по совместимости между пользователями.
    7. Реализация полнотекстового поиска с использованием PostgreSQL для быстрого и точного поиска по базе данных.

##### Технические требования:

    1. Использование фреймворка Django версии 4.0.
    2. Использование Django ORM для работы с базой данных.
    3. Использование PostgreSQL в качестве базы данных.
    4. Реализация REST API для взаимодействия с клиентскими приложениями.
    5. Использование сигналов Django для обработки событий и выполнения определенных действий.
    6. Применение паттернов проектирования для обеспечения гибкости и масштабируемости приложения.
    7. Обеспечение безопасности приложения, включая защиту от CSRF-атак и реализацию авторизации и аутентификации пользователей.

#### Архитектура приложения

Приложение должно быть разделено на несколько модулей (приложений) для управления различными функциональными областями. Рекомендуется следующая структура приложения:

    1. account: Модуль для управления пользователями, регистрации и аутентификации.
    2. profiles: Модуль для создания и управления профилями пользователей.
    3. messaging: Модуль для обмена сообщениями между пользователями.
    4. recommendations: Модуль для реализации алгоритма подбора рекомендаций.
    5. search: Модуль для реализации полнотекстового поиска.
    6. api: Модуль для создания REST API.

#### Модели данных

    1. User: Модель пользователя с полями, такими как имя, электронная почта, пароль и другими необходимыми атрибутами.
    2. Profile: Модель профиля пользователя, содержащая информацию о себе, фотографии и предпочтениях.
    3. Message: Модель сообщения с полями отправителя, получателя, текстом и временем отправки.
    4. Comment: Модель комментария с полями автора, профиля пользователя, текстом и временем создания.

#### Сигналы Django

Используйте сигналы Django для выполнения следующих действий:

    1. Отправка уведомлений при получении нового сообщения.
    2. Обновление рейтинга профиля при получении нового комментария.

#### REST API

Реализуйте REST API для взаимодействия с клиентскими приложениями. Определите необходимые эндпоинты для регистрации, аутентификации, управления профилями, обмена сообщениями и получения рекомендаций.
Полнотекстовый поиск

Используйте PostgreSQL для реализации полнотекстового поиска по базе данных. Реализуйте функциональность поиска профилей пользователей на основе указанных критериев.

#### Заключение

    1. Разработайте веб-приложение "Сайт знакомств" на основе указанных требований и спецификаций.
    2. Обеспечьте качество и безопасность кода, учитывая современные стандарты разработки и защиты.
    3. Предоставьте документацию по API, описывающую доступные эндпоинты, параметры и форматы данных.
    4. Протестируйте приложение на различных сценариях использования, исправьте ошибки и оптимизируйте производительность при необходимости.