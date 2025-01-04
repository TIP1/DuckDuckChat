# Params
VENV = .venv
PYTHON = python3
PYTHON_DIR = /Applications/Python 3.11
PIP = $(VENV)/bin/pip

# Creating a virtual environment
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "📦 Creating a virtual environment..."; \
		$(PYTHON) -m venv $(VENV); \
		echo "✅ A virtual environment has been created."; \
	else \
		echo "⚠️The virtual environment already exists."; \
	fi

# Activating the virtual environment
activate:
	@echo "🔗 To activate the virtual environment, run the command:"
	@echo "source $(VENV)/bin/activate"

# Deactivating the virtual environment
deactivate:
	@echo "🔌 To deactivate the virtual environment, run the command:"
	@echo "deactivate"

# Installing dependencies
install: venv
	@echo "📥 Installing dependencies in a virtual environment..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@echo "✅ Dependencies are installed."

# Launching the app
run: install
	@echo "🚀 Launching the app..."
	@$(PYTHON) app/main.py

# Cleaning up the environment
clean:
	@echo "🧹 Deleting the virtual environment..."
	rm -rf $(VENV)
	@echo "✅ Cleaning is complete."

# Update certificates
certificate:
	@echo "🧹 Installing certificates..."
	@"$(PYTHON_DIR)/Install Certificates.command"
	@echo "✅ The installation is complete."