venv/bin/pip uninstall -y qwilib
venv/bin/pip uninstall -y $(venv/bin/pip freeze)

status=$?
if [ $status -eq 1 ]; then
  echo "Pip has no dependencies installed"
fi