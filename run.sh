#!/usr/bin/env bash
echo "[START] $(date +%Y%m%d_%H%M%S)"
echo "" > data.json
scrapy runspider myspider.py -o data.json --nolog
echo "[INFO] RUN"
echo "[COMPLETED] $(date +%Y%m%d_%H%M%S)"