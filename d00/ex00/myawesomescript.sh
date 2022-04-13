#!/bin/bash
curl -# --head $1  2>/dev/null | grep "Location: " | cut -c11-