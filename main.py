#! /usr/bin/env python3

import argparse
import yaml
import os
import secrets
import string


def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def load_env_file(env_path: str) -> dict:
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, _, value = line.strip().partition('=')
                    env_vars[key] = value
    return env_vars


def save_env_file(env_path: str, env_vars: dict):
    with open(env_path, 'w') as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")


def process_config(config_path: str, env_path: str):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    general = config.get('general_settings', {})
    default_length = general.get('password_lenght', 16)

    only_if_empty = config.get('only_if_empty', [])
    always_override = config.get('always_override', [])

    env_vars = load_env_file(env_path)

    for key in only_if_empty:
        if key in env_vars and not env_vars[key]:
            env_vars[key] = generate_password(default_length)

    for key in always_override:
        if key in env_vars:
            env_vars[key] = generate_password(default_length)


    save_env_file(env_path, env_vars)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Randalf: Gestione automatica password in .env")
    parser.add_argument("-i", "--input", required=True, help="Path al file di configurazione YAML")
    parser.add_argument("-f", "--envfile", required=True, help="Path al file .env da modificare")

    args = parser.parse_args()
    process_config(args.input, args.envfile)
