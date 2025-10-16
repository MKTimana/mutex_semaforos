# 🧠 Sincronização com Mutexes e Semáforos

**Autores:** Milton Timana @MKTimana & Manuel Dinis Jr.
**Disciplina:** Sistemas Distribuídos e Paralelos 
**Linguagem:** Python (com `threading`)

## 🎯 Objetivo
Demonstrar o uso de **mutexes (locks)** e **semáforos** para sincronização entre **threads** que acedem a um recurso partilhado.

## 🧩 Descrição
Este programa simula um sistema bancário onde várias threads (“trabalhadores”) acedem ao mesmo recurso partilhado — o saldo de um banco.  
Para garantir a integridade dos dados e controlar o número de acessos simultâneos, são utilizados:

- **Mutex (`threading.Lock`)** – para garantir **acesso exclusivo** ao saldo.  
- **Semáforo (`threading.Semaphore`)** – para limitar **quantas threads podem trabalhar ao mesmo tempo**.

Cada thread realiza um número definido de operações de depósito com pausas aleatórias, simulando o comportamento assíncrono de processos reais ou do dia-a-dia.

## ⚙️ Execução

### 1️⃣ Requisitos
- Python 3.10 ou superior  
- Sem dependências externas (utiliza apenas a biblioteca padrão)

### 2️⃣ Executar o programa

No terminal (dentro da pasta do ficheiro `mutex_semaforo.py`):

```bash
python mutex_semaforo.py --workers 20 --loops 10 --sleep-ms 240,380 --max-concurrent 4
```

### 3️⃣ Parâmetros disponíveis

| Parâmetro | Descrição | Valor padrão |
|------------|------------|----------------|
| `--workers` | Número de threads (trabalhadores) | 6 |
| `--loops` | Número de operações (depósitos) por thread | 5 |
| `--sleep-ms` | Intervalo aleatório de pausa (em ms) entre operações | 240,380 |
| `--max-concurrent` | Capacidade máxima do semáforo (threads simultâneas) | 3 |


## 🧪 Exemplo de saída (resumo)

```
[T3] entrou no balcão (ocupação = 3/4)
 Operação 5/10 da [T3]
[T3] depositou 12.15 | saldo existente actualmente: 184.50
[T3] saiu do balcão (ocupação = 2/4)

Acessos registados: 200
Saldo final: 287.55
```

🟢 As threads entram e saem do “balcão” em grupos limitados pelo semáforo.  
🔒 O `Lock` garante que o saldo é atualizado correctamente.


## 🧱 Conceitos demonstrados

| Conceito | Explicação |
|-----------|------------|
| **Thread** | Unidade de execução paralela dentro de um processo |
| **Mutex (Lock)** | Garante exclusividade mútua — apenas uma thread modifica o recurso por vez |
| **Semáforo** | Controla quantas threads podem aceder simultaneamente |
| **Concorrência** | Execução intercalada e segura de várias tarefas em simultâneo |


## 🧠 Testes recomendados

### Cenário 1 – Execução sequencial
```bash
python mutex_semaforo.py --workers 6 --max-concurrent 1
```
➡ Uma thread por vez (sem paralelismo real)

### Cenário 2 – Paralelismo controlado
```bash
python mutex_semaforo.py --workers 6 --max-concurrent 3
```
➡ Três threads no “balcão” ao mesmo tempo

### Cenário 3 – Todas simultâneas
```bash
python mutex_semaforo.py --workers 6 --max-concurrent 6
```
➡ Todas as threads entram juntas (mesmo assim o saldo mantém consistência)

## 🧾 Conclusão
O programa comprova a importância de **mecanismos de sincronização** em ambientes multithreaded.  
Sem o uso de `Lock` e `Semaphore`, as operações concorrentes poderiam resultar em inconsistência de dados e comportamentos imprevisíveis.