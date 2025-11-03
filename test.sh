#!/bin/sh

curl --fail -H "Authorization: Bearer ${HA_TOKEN:-TEST_TOKEN}" http://homeassistant:8123/api/

