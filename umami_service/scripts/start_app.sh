#!/bin/bash

uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8080 \
    --log-config logging_config.yaml \
    --log-level debug \
    --reload
