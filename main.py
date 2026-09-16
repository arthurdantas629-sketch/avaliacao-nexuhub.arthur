 # FASE 1 - Construção Autônoma da Estrutura Base

# Etapa 1: Cadastro da Startup e Projetos

startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("Startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])


# Etapa 2: Mapeamento das Bancadas de Trabalho

# 1 = Bancada Ocupada
# 0 = Bancada Livre

bancadas = [
    [1, 0],  # Linha 0 - Setor Norte: N1 ocupada, N2 livre
    [0, 1]   # Linha 1 - Setor Sul: S1 livre, S2 ocupada
]

print("\nStatus das bancadas:")
print("Bancada N1:", bancadas[0][0])
print("Bancada N2:", bancadas[0][1])
print("Bancada S1:", bancadas[1][0])
print("Bancada S2:", bancadas[1][1])

print("\nLegenda: 1 = Ocupado | 0 = Livre")

Startup: CyberPulse Tech
Segmento: Segurança da Informação
Primeiro produto: Firewall IA

Status das bancadas:
Bancada N1: 1
Bancada N2: 0
Bancada S1: 0
Bancada S2: 1

Legenda: 1 = Ocupado | 0 = Livre
