        # postgresql — N+1 проблема, JOIN-ы, CTE и LATERAL

        Homework-шаблон для урока **l4_n_plus_1_and_joins** (N+1 проблема, JOIN-ы, CTE и LATERAL) на платформе Vibe Learn.

        ## Что делать

        Дано: testcontainers PG + начальная схема (users, orders, items, categories с иерархией)
+ плохой Python-код, который явно делает N+1. Тесты в template считают число SQL-запросов
через psycopg cursor hook. Твоя задача:
1) Реализовать функцию `get_user_dashboard(user_id)` за ≤ 2 запросов к БД.
2) Реализовать `get_category_tree(root_id)` через WITH RECURSIVE.
3) Реализовать `get_top_orders_per_user(limit_per_user)` через LATERAL.
Тесты проверят корректность результатов и упадут, если запросов больше N+EPS.

## Контекст (из transfer-задачи урока)

Тебе показывают API endpoint Django-проекта: `/api/sellers/dashboard`. Он возвращает
список из 50 продавцов, для каждого — данные:
- email, profile_completed;
- count активных listings;
- sum выручки за последние 30 дней;
- топ-3 последних заказа (id, date, total).

Текущий код:

## Recap из урока

- **N+1 — главный антипаттерн ORM.** Один запрос за списком + N запросов за деталями вместо одного JOIN-а. На сотне родителей это 101 round-trip вместо 1.
- **Eager loading лечит:** SQLAlchemy `joinedload/selectinload`, Django `select_related/prefetch_related`, GORM `Preload`. Не магия — JOIN или WHERE IN под капотом.
- **LEFT JOIN с условием на правую таблицу в WHERE — это INNER JOIN.** Сохраняй LEFT-семантику переводя условие в ON.
- **CTE в PG12+ инлайнятся.** WITH ... AS MATERIALIZED — барьер оптимизации; WITH RECURSIVE — обход деревьев и графов.
- **LATERAL JOIN — для top-N per group и параметризованных subqueries.** Альтернатива — window functions (ROW_NUMBER + фильтр).

        ## Как работать

        1. Платформа Vibe Learn создаёт копию этого репо в твоём GitHub-аккаунте по клику «Начать домашку» на странице урока (через GitHub `/generate`, codecrafters-pattern).
        2. Склонируй копию локально, реализуй TODO в `main.py`, прогони тесты, запушь.
        3. CI (`.github/workflows/ci.yml`) ставит зависимости и запускает `pytest` на каждый push. Платформа слушает результат через webhook от GitHub Actions и обновляет статус домашки на странице урока.

        ## Локальное окружение

        - Python 3.12+
        - Docker + docker-compose — `docker compose up -d` поднимает single-node PostgreSQL 16 на `localhost:5432` с healthcheck. DSN: `postgresql://postgres:postgres@localhost:5432/postgres`. Переопределяется через env `DATABASE_URL`.

        ## Запуск

        ```bash
        # Поднять локальный PostgreSQL
        docker compose up -d

        # Установить зависимости
        pip install -r requirements.txt

        # Прогнать тесты (интеграционный включается через PG_INTEGRATION=1)
        pytest
        PG_INTEGRATION=1 pytest

        # Запустить main (печатает marker; замени stub на реализацию)
        python main.py
        ```

        ## Заметка автора

        Это baseline-шаблон, сгенерированный платформой. Бизнес-сущность задачи (что конкретно реализовать в `main.py`, какие тесты сделать строгими) расширяется по ходу итераций — параллельно с углублением теории урока.
