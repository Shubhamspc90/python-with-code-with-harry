# # ==========================================
# # PYTHON VIRTUAL ENVIRONMENT (VENV) COMMANDS
# # ==========================================

# # Step 1: Create a Virtual Environment
# python -m venv venv1

# # Creates a virtual environment named "venv1"


# # Step 2: Activate Virtual Environment (PowerShell)
# .\venv1\Scripts\Activate.ps1

# # After activation, prompt will look like:
# # (venv1) PS D:\your_project>


# # Step 3: Check Installed Packages
# pip list

# # Shows all installed packages in the virtual environment


# # Step 4: Install a Package
# pip install pandas

# # Installs pandas and its dependencies


# # Step 5: Install Another Package
# pip install requests

# # Installs the requests library for HTTP requests


# # Step 6: Verify Installed Packages
# pip list

# # Example Output:
# # numpy
# # pandas
# # requests
# # python-dateutil
# # tzdata


# # Step 7: View Details of a Package
# pip show pandas

# # Displays package information


# # Step 8: Save All Dependencies
# pip freeze > requirements.txt

# # Creates requirements.txt containing all installed packages


# # Step 9: View Requirements File
# type requirements.txt

# # Displays contents of requirements.txt


# # Step 10: Install Packages from Requirements File
# pip install -r requirements.txt

# # Installs all packages listed in requirements.txt


# # Step 11: Upgrade pip
# python -m pip install --upgrade pip

# # Updates pip to the latest version


# # Step 12: Uninstall a Package
# pip uninstall requests

# # Removes the requests package


# # Step 13: Deactivate Virtual Environment
# deactivate

# # Exits the virtual environment


# # ==========================================
# # COMMON MISTAKES
# # ==========================================

# # Wrong
# .\venv\Scripts\Activate.ps1

# # Correct
# .\venv1\Scripts\Activate.ps1


# # Wrong
# pip install request

# # Correct
# pip install requests


# # Wrong
# pip unistall requests

# # Correct
# pip uninstall requests


# # ==========================================
# # MOST COMMON WORKFLOW
# # ==========================================

# python -m venv venv1

# .\venv1\Scripts\Activate.ps1

# pip install pandas

# pip install requests

# pip freeze > requirements.txt

# pip list

# deactivate