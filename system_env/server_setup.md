 **complete steps** to install and configure FastAPI, Uvicorn, Nginx, pyenv, and MariaDB on a single Ubuntu server, with separate production and development environments using different ports.

### Step 0: create directories for production and dev 
```
mkdir -p ~/projects/fastapi/production
mkdir -p ~/projects/fastapi/development
```

### Step 1: Update System Packages
First, ensure your system packages are up to date.

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Dependencies
You’ll need various dependencies for Python, MariaDB, Nginx, and pyenv.

```bash
sudo apt install -y build-essential curl libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
python3-openssl mariadb-server mariadb-client nginx
```

### Step 3: Install pyenv for Python Version Management
#### a. Install pyenv

```bash
curl https://pyenv.run | bash
```

Add pyenv to your shell configuration:
```bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

Reload your shell:
```bash
exec "$SHELL"
```

#### b. Install Python Version via pyenv

Install a Python version (e.g., 3.11.4) using pyenv:

```bash
pyenv install 3.11.4
```

#### c. Create Separate Environments for Production and Development

- **Production environment**:

```bash
pyenv virtualenv 3.11.4 fastapi-prod
```

- **Development environment**:

```bash
pyenv virtualenv 3.11.4 fastapi-dev
```

### Step 4: Install FastAPI and Uvicorn in Each Environment
#### a. Activate Production Environment and Install FastAPI & Uvicorn

```bash
cd /path/to/your/production/app
pyenv local fastapi-prod
pip install fastapi uvicorn python-dotenv
```

#### b. Activate Development Environment and Install FastAPI & Uvicorn

```bash
cd /path/to/your/development/app
pyenv local fastapi-dev
pip install fastapi uvicorn python-dotenv
```

### Step 5: Set Up MariaDB Databases
#### a. Secure MariaDB Installation

Run the following command and follow the prompts to set a root password, disable remote root login, etc.

```bash
sudo mysql_secure_installation
```

#### b. Create Production and Development Databases

Log into MariaDB and create databases for production and development:

```bash
sudo mysql -u root -p

CREATE DATABASE prod_db;
CREATE DATABASE dev_db;

CREATE USER 'prod_user'@'localhost' IDENTIFIED BY 'prod_password';
CREATE USER 'dev_user'@'localhost' IDENTIFIED BY 'dev_password';

GRANT ALL PRIVILEGES ON prod_db.* TO 'prod_user'@'localhost';
GRANT ALL PRIVILEGES ON dev_db.* TO 'dev_user'@'localhost';

FLUSH PRIVILEGES;
EXIT;
```

### Step 6: Nginx Configuration for Reverse Proxy
#### a. Create Nginx Configuration for FastAPI (Production & Development)

```bash
sudo nano /etc/nginx/sites-available/fastapi
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Forward all requests for production to Uvicorn (port 8000)
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Forward all requests for development to Uvicorn (port 8001)
    location /dev/ {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Serve static files
    location /static/ {
        alias /path/to/static/files;  # Adjust path to your static files
    }
}
```

#### b. Enable the Nginx Site and Restart Nginx

```bash
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

### Step 7: Set Up Systemd Services for Uvicorn (Optional but Recommended)
Create systemd service files for running Uvicorn as a background service for both production and development.

#### a. Create Production Service File

```bash
sudo nano /etc/systemd/system/fastapi-prod.service
```

Add the following:

```ini
[Unit]
Description=FastAPI Production Server
After=network.target

[Service]
User=your_user
WorkingDirectory=/path/to/production/app
ExecStart=/home/your_user/.pyenv/versions/fastapi-prod/bin/uvicorn app:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

#### b. Create Development Service File

```bash
sudo nano /etc/systemd/system/fastapi-dev.service
```

Add the following:

```ini
[Unit]
Description=FastAPI Development Server
After=network.target

[Service]
User=your_user
WorkingDirectory=/path/to/development/app
ExecStart=/home/your_user/.pyenv/versions/fastapi-dev/bin/uvicorn app:app --host 0.0.0.0 --port 8001
Restart=always

[Install]
WantedBy=multi-user.target
```

#### c. Reload systemd and Start Services

```bash
sudo systemctl daemon-reload
sudo systemctl start fastapi-prod.service
sudo systemctl start fastapi-dev.service
sudo systemctl enable fastapi-prod.service
sudo systemctl enable fastapi-dev.service
```

### Step 8: Running FastAPI Servers Manually (if you don’t use systemd)
You can also start both environments manually using `uvicorn` if you prefer not to use systemd.

#### a. Running Production FastAPI App

Activate the production environment and start the server:

```bash
cd /path/to/your/production/app
pyenv local fastapi-prod
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### b. Running Development FastAPI App

Activate the development environment and start the server:

```bash
cd /path/to/your/development/app
pyenv local fastapi-dev
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
```

### Final Step: Verify Everything is Working
- **Production**: Visit `http://yourdomain.com/` to access the production FastAPI app.
- **Development**: Visit `http://yourdomain.com/dev/` to access the development FastAPI app.

### Summary of Commands:
1. Install dependencies.
2. Install pyenv and Python versions.
3. Set up MariaDB for both environments.
4. Install FastAPI and Uvicorn in both production and development environments.
5. Configure Nginx as a reverse proxy.
6. Set up and run Uvicorn with systemd or manually.

This setup allows you to run both production and development environments on the same server with FastAPI, Uvicorn, and Nginx.