#!/usr/bin/env python3

import base64
import bcrypt
import os
import re
import sys

def encode_secret(secret: str, rounds: int = 12) -> str:
    hashed = bcrypt.hashpw(secret.encode("utf-8"), bcrypt.gensalt(rounds))
    return base64.b64encode(hashed).decode("utf-8")

def replace_vars_in_template(template_path: str, output_path: str, replacements: dict):
	pattern = re.compile(r'\$\{(' + '|'.join(map(re.escape, replacements.keys())) + r')\}')
	with open(template_path, 'r', encoding='utf-8') as f:
		content = f.read()
		content = pattern.sub(lambda m: replacements[m.group(1)], content)
	with open(output_path, "w") as file:
		file.write(content)

DEFAULT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhOWRkNzY0NDkwMTA0NTg2ODVmMmZjNjFhZTRkNWY2NiIsImlhdCI6MTc2MjE3MTYzNSwiZXhwIjoyMDc3NTMxNjM1fQ.ud4A0VlTCDwE-Ir94AC4R9QOui3rqnGd4ib24AvokLY"

replacements = {
    "HA_USER": os.environ.get("HA_USER", "test_user"),
    "HA_PASSWORD": encode_secret(os.environ.get("HA_PASSWORD", "test_password")),
    "HA_USER_NAME": os.environ.get("HA_NAME", "Test User"),
    "HA_TOKEN": encode_secret(os.environ.get("HA_TOKEN", "DEFAULT_TOKEN")),
}

os.makedirs('/config/.storage', exist_ok=True)

replace_vars_in_template('./config-templates/onboarding', '/config/.storage/onboarding', replacements)
replace_vars_in_template('./config-templates/auth', '/config/.storage/auth', replacements)
replace_vars_in_template('./config-templates/auth_provider.homeassistant', '/config/.storage/auth_provider.homeassistant', replacements)