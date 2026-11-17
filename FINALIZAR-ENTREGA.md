# Finalização da entrega DIO — AppSec com Hermes

Este pacote **complementa** o projeto em `C:\dev\ana\dio-agent`; não substitui a base da DIO nem publica automaticamente em seu GitHub.

## Passo 1 — Copiar somente o complemento

No PowerShell, dentro da pasta onde este ZIP foi extraído:

```powershell
Copy-Item .\finalizar_readme.py C:\dev\ana\dio-agent\ -Force
Copy-Item .\docs\VALIDACAO-HERMES.md C:\dev\ana\dio-agent\docs\ -Force
Copy-Item .\docs\GUIA-EVIDENCIAS.md C:\dev\ana\dio-agent\docs\ -Force
New-Item -ItemType Directory -Force C:\dev\ana\dio-agent\evidencias | Out-Null
Copy-Item .\evidencias\README.md C:\dev\ana\dio-agent\evidencias\ -Force
```

## Passo 2 — Integrar README, executar testes e verificar Git

```powershell
cd C:\dev\ana\dio-agent
python .\finalizar_readme.py
python -m unittest discover -s tests -v
git status --short
git diff --check
git diff -- README.md
```

A integração do README é idempotente. Não presume que o Hermes está funcionando: isso foi evidenciado nas respostas que você compartilhou, mas **não foi executado neste ambiente**. Revise o diff antes do commit.

## Passo 3 — Capturas do Hermes

Leia `docs/GUIA-EVIDENCIAS.md`, faça os prints no seu VS Code e salve os arquivos PNG em `evidencias/` com nomes indicados. Não publique capturas que mostrem chaves de API, tokens ou dados privados.

## Passo 4 — Commits sugeridos

```powershell
git add AGENTS.md agent/persona.md agent/knowledge/security-basics.md skills/vulnerability-analysis/README.md skills/vulnerability-analysis/SKILL.md .agents/skills/vulnerability-analysis examples/sql-injection/app.py examples/sql-injection/app_fixed.py tests/test_sql_injection.py .github/workflows/appsec-lab.yml apply_to_base.py docs/roteiro-hermes.md
 git commit -m "feat(appsec): specialize DIO Agent with vulnerability analysis"
```

Se o primeiro commit incluir arquivos já versionados ou nenhuma mudança, confira `git status` e ajuste o `git add`. Para o segundo:

```powershell
git add README.md docs/VALIDACAO-HERMES.md docs/GUIA-EVIDENCIAS.md evidencias/README.md finalizar_readme.py evidencias/*.png
git commit -m "docs: document Hermes validation and bootcamp evidence"
```

**Não crie commits vazios**. Se a pasta `evidencias` ainda não tiver prints, o `git add evidencias/*.png` pode não corresponder a arquivos; remova esse argumento até adicionar as capturas.

## Passo 5 — Publicar

1. Crie **na sua conta** um repositório público vazio chamado, por exemplo, `dio-agent-appsec-hermes` (sem gerar README/licença novos).
2. Confirme o remoto e a branch com `git remote -v` e `git branch --show-current`.
3. Se este clone ainda aponta para `digitalinnovationone/dio-agent`, **não dê push para o remoto original**. Use `git remote rename origin upstream` (somente se `origin` existir e for o original).
4. Adicione o seu remoto: `git remote add origin https://github.com/SEU-USUARIO/dio-agent-appsec-hermes.git`.
5. Use `git push -u origin main`, caso sua branch seja `main`.

Entregue à DIO a URL **do repositório público**, não um link para um arquivo.
