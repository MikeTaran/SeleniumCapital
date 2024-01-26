"""
-*- coding: utf-8 -*-
@Time    : 2024/01/13 22:00
@Author  : Artem Dashkov
"""
import pytest


@pytest.fixture(
    scope="function",
    params=[
        # "Shares",
        # "Commodities",
        # "Forex",
        # "Cryptocurrency"
        "Indices"
    ],
)
def cur_type_fi(request):
    """Fixture"""
    print(f"\n\n\nCurrent type finance instrument - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        "most_traded",
        "top_risers",
        # "top_fallers",
        # "most_volatile"
    ],
)
def cur_tab(request):
    """Fixture"""
    print(f"\n\n\nCurrent tab - {request.param}")
    return request.param
