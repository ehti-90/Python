#  Quiz Brain

A terminal-based quiz application built in Python using Object-Oriented Programming principles.

## Overview

The app loads a question bank, presents each question one by one, checks your answer, and reports your final score at the end.

## How It Works

1. Question data is loaded from `data.py`
2. Each question is turned into a `QuestionsBank` object and stored in a list
3. The `brain` class takes that list and drives the quiz loop
4. Questions are presented one by one via `next_question()`
5. The loop runs as long as `still_has_question()` returns `True`
6. At the end, `score_report()` displays your final result

## OOP Design

| Class | Responsibility |
|---|---|
| `QuestionsBank` | Holds a single question's text and answer |
| `brain` | Manages quiz state, tracks score, checks answers |
