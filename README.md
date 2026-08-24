# Mood & Performance Tracker

A backend CRUD API for tracking user-input mood and performance data over time.

## What it does

Exposes endpoints to create, read, update, and delete mood/performance
entries, with data persisted in SQLite. Started with JSON file storage
and migrated to SQLite for more reliable, structured persistence.

## Tech stack

- FastAPI (routing/API layer)
- SQLite (data persistence)
- Python

## Architecture

Clean separation between routing, storage, and data layers, making it
straightforward to extend or swap components (e.g. add a frontend, move
to a different database).

## Status

Backend/API is functional. Originally scoped as a full-stack app —
frontend not yet started. On hold, but a planned next step.
