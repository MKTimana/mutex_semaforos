import threading
import time
import random
import argparse

class Banco:
    
    def __init__(self):
        self.acessos = 0
        self.saldo = 0.0
        self.lock = threading.Lock()
        
    def depositar(self, tid, valor):
        with self.lock:
            self.saldo += valor
            self.acessos += 1
            print(f"[T{tid}] depositou {valor:.2f} | saldo existente actualmente: {self.saldo:.2f}")
        

    def trabalhador(self, tid, loops, sleep_ms=(240,380)):
        from time import strftime
        print(f"{strftime('%H:%M:%S')}\n =================== [T{tid}] Inicio do trabalho ==============")
        
        for i in range(1, loops + 1):
            time.sleep(random.uniform(*sleep_ms) / 1000.0)
            valor = random.uniform(5,15)
            print(f" Operação {i}/{loops} da [T{tid}]")
            self.depositar(tid, valor)
            
        print(f"======================[T{tid}] Fim do trabalho ============= \n")



            
if __name__ == "__main__":
    banco = Banco()
    
    threads = []
    for tid in range(1,7):
        t = threading.Thread(target = banco.trabalhador, args = (tid, 5))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Acessos registrados: {banco.acessos}")
    print(f"Saldo final: {banco.saldo:.2f}")