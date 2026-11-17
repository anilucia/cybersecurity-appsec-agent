"""Aplica os quatro registros no clone original, de forma idempotente.
Execute a partir da raiz do repositório após copiar os arquivos do kit.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def insert_once(path, anchor, addition, marker):
    file = ROOT / path
    if not file.exists():
        raise SystemExit(f"Arquivo ausente na base: {file}")
    text = file.read_text(encoding="utf-8")
    if marker in text:
        print(f"Ja aplicado: {path}")
        return
    if anchor not in text:
        raise SystemExit(f"Ancora nao encontrada: {path}: {anchor[:60]!r}; confira a versao do repositorio base")
    file.write_text(text.replace(anchor, addition + anchor, 1), encoding="utf-8")
    print(f"Atualizado: {path}")


insert_once("AGENTS.md", "Se nenhuma skill se aplicar,", "| Analise de vulnerabilidades (AppSec) | precisa revisar codigo ou infraestrutura autorizada, estimar risco e planejar mitigacao | `skills/vulnerability-analysis/SKILL.md` |\n\n", "`skills/vulnerability-analysis/SKILL.md`")
insert_once("AGENTS.md", "Leia o arquivo relevante sempre que a conversa envolver o conteúdo dele.", "- `agent/knowledge/security-basics.md`: fundamentos de vulnerabilidade, ameaca, risco, CIA e controles defensivos.\n\n", "`agent/knowledge/security-basics.md`")
insert_once("agent/persona.md", "## O que o DIO Agent não faz", "## Especializacao AppSec\n\nQuando o assunto for seguranca, atua como mentor defensivo: confirma autorizacao, investiga o contexto antes de recomendar comandos, distingue evidencia de hipotese, avalia CIA, probabilidade, impacto e severidade, orienta mitigacao e revalidacao. Evita afirmacoes de execucao nao comprovadas e utiliza `skills/vulnerability-analysis/SKILL.md`.\n\n", "## Especializacao AppSec")
insert_once("README.md", "A pesquisa na web usa a busca do seu harness.", "| [Analise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa riscos e orienta mitigacoes com contexto, evidencias e testes | \"Revise o app.py como mentor AppSec.\" |\n\n", "[Analise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md)")
