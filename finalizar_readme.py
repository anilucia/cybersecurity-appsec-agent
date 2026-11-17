"""Adiciona seção AppSec ao README.md do clone DIO Agent sem substituí-lo."""
from pathlib import Path

root = Path(__file__).resolve().parent
readme = root / "README.md"
if not (root / "AGENTS.md").exists() or not readme.is_file():
    raise SystemExit("Execute dentro do clone do DIO Agent (README.md e AGENTS.md obrigatórios).")
marker = "<!-- DIO-APPSEC-PORTFOLIO-START -->"
end = "<!-- DIO-APPSEC-PORTFOLIO-END -->"
if marker in readme.read_text(encoding="utf-8"):
    print("README AppSec já integrado. Nenhuma mudança.")
    raise SystemExit(0)
section = r"""
<!-- DIO-APPSEC-PORTFOLIO-START -->
## 🛡️ Especialização AppSec — desafio DIO + Hermes

Esta evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) transforma o agente em um **mentor de análise defensiva de vulnerabilidades**, usando arquivos de conhecimento, uma persona e a skill `vulnerability-analysis` — **sem treinar um novo modelo**.

### Motivação e comportamento

O agente pergunta sobre contexto e autorização, lê código antes de concluir, diferencia evidências de hipóteses, avalia confidencialidade/integridade/disponibilidade (CIA), estima impacto × probabilidade em matriz didática 5×5, propõe mitigação e orienta revalidação. Inclui classificação CWE e mapeamento responsável para OWASP/MITRE ATT&CK.

### Arquivos criados e modificados

| Caminho | Finalidade |
| --- | --- |
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | Roteiro de investigação AppSec |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | Explicação da habilidade |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | Conceitos e controles defensivos |
| [`agent/persona.md`](agent/persona.md) | Complemento de personalidade voltado a AppSec |
| [`AGENTS.md`](AGENTS.md) | Descoberta e instruções da skill |
| [`examples/sql-injection/app.py`](examples/sql-injection/app.py) | Login intencionalmente vulnerável, apenas em laboratório |
| [`examples/sql-injection/app_fixed.py`](examples/sql-injection/app_fixed.py) | Exemplo corrigido com SQL parametrizado |
| [`tests/test_sql_injection.py`](tests/test_sql_injection.py) | Regressão automatizada |
| [`.github/workflows/appsec-lab.yml`](.github/workflows/appsec-lab.yml) | CI de testes (não é scanner) |

### Execução no Hermes (Windows / VS Code)

A partir da raiz do clone:

```powershell
cd C:\dev\ana\dio-agent
hermes skills trust "C:\dev\ana\dio-agent"
hermes skills list
hermes
```

Para o Hermes reconhecer a habilidade como skill local, mantenha uma cópia de `skills/vulnerability-analysis/` em `.agents/skills/vulnerability-analysis/` (além da pasta exigida pela DIO). Use o Hermes **na raiz do projeto**. A instalação do harness segue a [documentação oficial](https://hermes-agent.nousresearch.com/docs).

Rode os testes locais com:

```powershell
python -m unittest discover -s tests -v
```

### Melhoria escolhida: DevSecOps e verificação de evidências

A skill propõe revisão de alterações com formato consistente (contexto, achado, CIA, risco, mitigação, testes e risco residual). O GitHub Actions executa testes de regressão. **Plus comprovado em laboratório:** o Hermes corrigiu um falso positivo da sua análise anterior após checar os bytes do arquivo corrigido. Consulte [validação do Hermes](docs/VALIDACAO-HERMES.md) e [guia de evidências](docs/GUIA-EVIDENCIAS.md).

### Evidências

Salve os prints reais em [`evidencias/`](evidencias/). Nenhuma captura é fabricada. A confirmação de funcionamento refere-se apenas ao laboratório didático com SQLite em memória, não a ambientes de produção.

<!-- DIO-APPSEC-PORTFOLIO-END -->
"""
text=readme.read_text(encoding="utf-8")
readme.write_text(text.rstrip()+"\n\n"+section+"\n", encoding="utf-8")
print("Seção AppSec adicionada ao README.md. Revise com git diff -- README.md")
