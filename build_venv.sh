echo "Removing env"
rm -r env

sleep 1s

echo "Creating env"
python3 -m venv env

sleep 3s

echo "Activate env"
source env/bin/activate

which python