#!/usr/bin/env bash

# 1) FastAPI (main.py) 실행
#    main.py 가 프로젝트 루트에 있을 때는 "main:app" 으로 호출합니다.
uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 &

# 2) Streamlit (프론트엔드) 실행
streamlit run frontend/app.py \
  --server.port 10000
