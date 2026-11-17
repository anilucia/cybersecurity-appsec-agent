# Fundamentos para análise defensiva

## Conceitos
- **Ativo:** componente ou informação que precisa de proteção.
- **Vulnerabilidade:** fraqueza explorável de código, configuração ou processo.
- **Ameaça:** agente, circunstância ou evento com potencial de explorar uma fraqueza.
- **Risco:** combinação de probabilidade de ocorrência e consequências sobre um ativo.
- **Exposição:** condição que permite atingir uma superfície de ataque.
- **Exploit:** técnica ou mecanismo que aproveita uma vulnerabilidade; existência da falha não demonstra exploração.

## Tríade CIA
- **Confidencialidade:** impedir acesso indevido à informação.
- **Integridade:** preservar correção e impedir alterações não autorizadas.
- **Disponibilidade:** manter serviço e dados acessíveis quando necessários.

## Classificações
- **CWE:** taxonomia de tipos de fraqueza, como CWE-89 (SQL Injection).
- **OWASP:** orientação de práticas de segurança em aplicações; não substitui provas sobre um caso específico.
- **MITRE ATT&CK:** descreve táticas e técnicas observadas em adversários; não equivale diretamente a CWE ou CVE. T1190, Exploit Public-Facing Application, só cabe quando a exploração de uma aplicação exposta for cenário relevante.
- **CVSS:** padrão de pontuação com métricas próprias; nunca chamar a matriz didática 5×5 de CVSS.

## Matriz didática de risco
Impacto e probabilidade de 1 a 5. Produto 1–4: baixo; 5–9: moderado; 10–16: alto; 17–25: crítico. Explicitar hipóteses e a incerteza.

## Boas práticas
- Consultas SQL parametrizadas em vez de concatenação de entradas.
- Senhas armazenadas com hash apropriado e sal, nunca em texto puro em sistemas reais.
- Privilégio mínimo, gestão de secrets, validação de entrada, logs sem dados sensíveis.
- Defesa em profundidade: revisão de código, testes, atualização, isolamento e monitoramento.
- Nunca executar testes de segurança fora de ativos sob autorização explícita.
- Antes/depois: preservar caso de teste, confirmar falha, corrigir, testar regressão e avaliar risco residual.

## Referências
- https://cwe.mitre.org/data/definitions/89.html
- https://attack.mitre.org/techniques/T1190/
- https://owasp.org/www-community/attacks/SQL_Injection
- https://owasp.org/www-project-top-ten/
