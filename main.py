import platform
import os
import subprocess
import psutil
import cpuinfo
import GPUtil

def info_geral():
    print("="*30, "INFORMAÇÕES DO SISTEMA", "="*30)
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Nome do Host: {platform.node()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Plataforma: {platform.platform()}")
    print("="*80, "\n")

def info_cpu():
    info = cpuinfo.get_cpu_info()
    print("CPU:")
    print(f"  Modelo: {info['brand_raw']}")
    print(f"  Núcleos Físicos: {psutil.cpu_count(logical=False)}")
    print(f"  Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
    print(f"  Frequência Máx: {info['hz_advertised_friendly']}")
    print("-"*50, "\n")

def info_ram():
    mem = psutil.virtual_memory()
    print("Memória RAM:")
    print(f"  Total: {mem.total / (1024**3):.2f} GB")
    print(f"  Usada: {mem.used / (1024**3):.2f} GB")
    print(f"  Livre: {mem.available / (1024**3):.2f} GB")
    print(f"  Uso: {mem.percent}%")
    print("-"*50, "\n")

def info_gpu():
    gpus = GPUtil.getGPUs()
    print("GPU(s):")
    if gpus:
        for gpu in gpus:
            print(f"  Nome: {gpu.name}")
            print(f"  Memória Total: {gpu.memoryTotal} MB")
            print(f"  Memória Usada: {gpu.memoryUsed} MB")
            print(f"  Memória Livre: {gpu.memoryFree} MB")
            print(f"  Uso: {gpu.memoryUtil*100:.1f}%")
            print(f"  Temperatura: {gpu.temperature} °C")
    else:
        print("  Nenhuma GPU detectada")
    print("-"*50, "\n")

def info_disco():
    print("Discos:")
    for part in psutil.disk_partitions():
        if 'cdrom' in part.opts or part.fstype == '':
            continue
        usage = psutil.disk_usage(part.mountpoint)
        print(f"  Dispositivo: {part.device}")
        print(f"  Ponto de Montagem: {part.mountpoint}")
        print(f"  Total: {usage.total / (1024**3):.2f} GB")
        print(f"  Usado: {usage.used / (1024**3):.2f} GB")
        print(f"  Livre: {usage.free / (1024**3):.2f} GB")
        print(f"  Uso: {usage.percent}%")
    print("-"*50, "\n")

def info_placa_mae():
    print("Placa-mãe:")
    sistema = platform.system()
    try:
        if sistema == "Windows":
            output = subprocess.check_output(["wmic", "baseboard", "get", "product,Manufacturer,version,serialnumber"], universal_newlines=True)
            print(output)
        elif sistema == "Linux":
            output = subprocess.check_output(["sudo", "dmidecode", "-t", "baseboard"], universal_newlines=True)
            print(output)
        else:
            print("  Sistema não suportado para placa-mãe")
    except Exception as e:
        print(f"  Não foi possível obter informações: {e}")
    print("-"*50, "\n")

def main():
    info_geral()
    info_cpu()
    info_ram()
    info_gpu()
    info_disco()
    info_placa_mae()

if __name__ == "__main__":
    main()

