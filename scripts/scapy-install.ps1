#ps1

# Use Cloudbase-Init's Python
$basePathPython = "C:\Program Files\Cloudbase Solutions\Cloudbase-Init\Python"
$env:Path += ";${basePathPython};${basePathPython}\Scripts\"


# Update pip and install scapy
python -m pip install pip --upgrade
pip install scapy
