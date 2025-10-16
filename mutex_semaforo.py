import threading
import time
import random
import argparse

class Banco:
    
    def __init__(self, max_concurrent=3):
        self.acessos = 0
        self.saldo = 0.0
        self.lock = threading.Lock()
        self.porta = threading.Semaphore(max_concurrent)
        self.capacidade = max_concurrent
        
    def depositar(self, tid, valor):
        with self.lock:
            self.saldo += valor
            self.acessos += 1
            print(f"[T{tid}] depositou {valor:.2f} | saldo existente actualmente: {self.saldo:.2f}")
        

    def trabalhador(self, tid, loops, sleep_ms=(240,380)):
        from time import strftime
        print(f"{strftime('%H:%M:%S')}\n =================== [T{tid}] Inicio do trabalho ==============")
        
        for i in range(1, loops + 1):
            with self.porta:
                
                ocupacao = self.capacidade - self.porta._value
                print(f"\n[T{tid}] entrou no balcão (ocupação = {ocupacao}/{self.capacidade})")
                time.sleep(random.uniform(*sleep_ms) / 1000.0)
                
                valor = random.uniform(5,15)
                print(f" Operação {i}/{loops} da [T{tid}]")
                self.depositar(tid, valor)
                
            ocupacao = self.capacidade - self.porta._value
            print(f"[T{tid}] saiu do balcão (ocupação = {ocupacao}/{self.capacidade})\n")
            
        print(f"======================[T{tid}] Fim do trabalho ============= \n")



            
if __name__ == "__main__":
    
    ap = argparse.ArgumentParser(description="Demonstração: Mutex (Lock) + Semáforo com threads")
    ap.add_argument("--workers", type=int, default=6, help="N° de threads (trabalhadores)")
    ap.add_argument("--loops", type=int, default=5, help="N° de operações por thread")
    ap.add_argument("--sleep-ms", type=str, default="240,380", help="Intervalo (ms) entre operações, ex.: 240,380")
    ap.add_argument("--max-concurrent", type=int, default=3, help="Capacidade do semáforo (threads simultâneas)")
    args = ap.parse_args()
    lo, hi = map(int, args.sleep_ms.split(","))
    
    banco = Banco(max_concurrent=args.max_concurrent)
    threads = []
    for tid in range(1, args.workers + 1):
        t = threading.Thread(target=banco.trabalhador, args=(tid, args.loops, (lo, hi)))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Acessos registrados: {banco.acessos}")
    print(f"Saldo final: {banco.saldo:.2f}")