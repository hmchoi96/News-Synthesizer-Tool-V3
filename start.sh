#!/usr/bin/env bash
# File: start.sh

# 1) FastAPI (main.py) 실행
uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 &

# 2) Streamlit (프론트엔드) 실행
streamlit run frontend/app.py \
  --server.port 10000
