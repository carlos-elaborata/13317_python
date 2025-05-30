# msg = "Abacate"
# print(f"-{msg}-")  # -Abacate-
# print(f"-{msg:<9}-")  # -Abacate  -
# print(f"-{msg:>9}-")  # -  Abacate-
# print(f"-{msg:^9}-")  # - Abacate -
# print(f"-{msg:=^15}-")  # -====Abacate====-


# Minha Tabela
# a -> 01001010
# b -> 01001011
# 5 -> 01011001
# 6 -> 01011010

# Sua Tabela
# a -> 01011001 -> Minha Tabela equivale ao 5
# b -> 01001011
# 5 -> 01011010 -> Minha Tabela equivale ao 6
# 6 -> 01011011

import os
import pathlib

# print(os.getcwd())
# print(os.listdir("exercicios"))

# for raiz, dirs, arqs in os.walk(os.getcwd()):
#     print(f"Raíz: {raiz}")
#     print(f"Diretórios: {dirs}")
#     print(f"Arquivos: {arqs}")
#     print("-" * 50)

# os.mkdir("arquivos")
# os.makedirs("arquivos/bin/2025/05")
# os.rmdir("exercicios")
# os.removedirs("arquivos/bin/2025/05")

# print(__file__)

# print(os.path.basename(__file__))
# print(pathlib.Path(__file__).name)


# print(os.path.dirname(__file__))
# print(pathlib.Path(__file__).parent)
# print(pathlib.Path(__file__).parents[0])

# print(os.path.abspath("exercicios"))
# print(pathlib.Path("exercicios").resolve())

# BASE_DIR = os.path.dirname(__file__)
# file_dir = os.path.join(BASE_DIR, "arquivos", "texto_09.txt")
# arquivo = open(file_dir, "r", encoding="utf8")
# conteudo = arquivo.read()
# arquivo.close()
# print(conteudo)

# BASE_DIR = pathlib.Path(__file__).parent
# file_dir = BASE_DIR / "arquivos" / "texto_09.txt"
# arquivo = open(file_dir, "r", encoding="utf8")
# conteudo = arquivo.read()
# arquivo.close()
# print(conteudo)

try:
    arquivo = open("batman.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    numero = int(conteudo)
    resultado = 1 / numero
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except ValueError:
    print("O conteúdo não pôde ser convertido para um inteiro.")
except ZeroDivisionError:
    print("Impossível dividir por zero.")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
else:
    print(f"1/{numero} = {resultado}")
finally:
    print("Fim do programa.")
