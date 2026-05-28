"""Homework scaffold — postgresql lesson `l4_n_plus_1_and_joins` (Vibe Learn).

Задача: убрать N+1: get_user_dashboard (≤2 запроса), get_category_tree (WITH RECURSIVE), LATERAL.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

Драйвер: psycopg (v3). DSN берётся из env DATABASE_URL.
"""

import os

import psycopg


def database_url() -> str:
    """DSN PostgreSQL из env. Дефолт совпадает с docker-compose.yml."""
    return os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/postgres",
    )


def connect() -> "psycopg.Connection":
    """Открыть соединение psycopg из DATABASE_URL."""
    return psycopg.connect(database_url())


# ----- TODO #1: get_user_dashboard -----
def get_user_dashboard(conn, user_id: int) -> dict:
    """собрать дашборд пользователя за ≤2 запроса (JOIN/агрегация вместо цикла)"""
    raise NotImplementedError("get_user_dashboard: реализуй меня")


# ----- TODO #2: get_category_tree -----
def get_category_tree(conn, root_id: int) -> dict:
    """WITH RECURSIVE — построить дерево категорий от root_id одним запросом"""
    raise NotImplementedError("get_category_tree: реализуй меня")


# ----- TODO #3: get_top_orders_per_user -----
def get_top_orders_per_user(conn, limit_per_user: int) -> list[dict]:
    """LATERAL join — топ-N заказов на каждого пользователя одним запросом"""
    raise NotImplementedError("get_top_orders_per_user: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — postgresql lesson scaffold up")
    print(f"DATABASE_URL: {database_url()}")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
