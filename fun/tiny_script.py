from datetime import datetime

def proof_of_existence():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{time}] Still alive. Still building. – Mahi"

if __name__ == "__main__":
    print(proof_of_existence())
