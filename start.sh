#!/usr/bin/env bash
uvicorn blog.main:app --host 0.0.0.0 --port $PORT