#!/bin/bash

cd app || exit
su -m app -c "uvicorn app:app --host 0.0.0.0 --port 5057"