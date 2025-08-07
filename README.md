# You shall no password
Randalf is a CLI tool to provision or regenerate secrets in `.env` files based on a YAML configuration.  
Don’t leave default passwords in your `.env` files — generate them randomly.  


## ✨ Features

- Automatically generates secure passwords for missing or all `.env` keys
- Declarative configuration via `config.yml`
- Works well with Docker, CI/CD, and secret bootstrapping
- Lightweight and pipx-installable

## 📦 Prerequisites

- Python 3.7+
- `pipx` installed (recommended for CLI tools)  
  Install pipx if you don't have it:

  ```bash
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath


## 🚀 Installation

Install Randalf directly from the GitHub repository using pipx:

```bash
pipx install git+https://github.com/CoLorenzo/Randalf.git
```

## 🧾 Usage

```bash
randalf -i ./config.yml -f ./.env
```

This will:

* Read `config.yml` for instructions
* Edit the `.env` file in-place
* Generate or regenerate passwords depending on the config

You can omit the parameters and Randalf will default to:

```bash
randalf -i config.yml -f .env
```

## 🛠️ Configuration Format

Here is an example `config.yml`:

```yaml
general:
  password_length: 64

only_if_empty:
  - MARIADB_ROOT_PASSWORD
  - REDIS_PASSWORD

always_override:
  - JWT_SECRET
  - API_KEY
```

* `password_length`: how many characters to generate
* `only_if_empty`: only generate if the variable is missing or empty
* `always_override`: always replace the value, even if one already exists

## 📁 Docker (optional)

If you prefer Docker:

```bash
docker run --rm \
  -v "$(pwd)/config.yml:/Randalf/config.yml:ro" \
  -v "$(pwd)/.env:/Randalf/.env" \
  colorenzo/randalf:latest
```
