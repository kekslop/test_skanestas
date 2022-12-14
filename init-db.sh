#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE docker;
    CREATE TABLE docker.docker (col String, dt Date ) engine MergeTree()PARTITION BY toYYYYMM(dt) ORDER BY col;
EOSQL