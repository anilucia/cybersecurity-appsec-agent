# Validação prática da especialização AppSec no Hermes

## Objetivo e escopo

Validar a leitura da skill `vulnerability-analysis` e a análise defensiva de um login Python com SQLite `:memory:` e dados inteiramente fictícios. Todos os testes são locais e autorizados.

## Evidências observadas nas saídas compartilhadas (17/11/2026)

| Etapa | Evidência observada | Interpretação |
| --- | --- | --- |
| Descoberta | `hermes skills list` registrou `vulnerability-analysis` como `project / local / enabled` e `1 local` | Skill localizada e habilitada |
| Processo de análise | Hermes apresentou etapas de contexto, CIA, risco 5×5, CWE e revalidação | Comportamento declarativo alinhado à skill |
| Primeira análise | Detectou SQL Injection em `app.py`, mas afirmou erroneamente que `app_fixed.py` continha `password = ***` | Houve **falso positivo** sobre a correção |
| Validação Python local | `test_fixed_case_blocks_bypass` e `test_vulnerable_case_demonstrates_bypass` passaram (`Ran 2 tests ... OK`) | Testes demonstraram bypass no exemplo vulnerável e bloqueio no corrigido |
| Reavaliação | Hermes verificou bytes do arquivo e reconheceu `?` (ASCII 63), não `***` | Corrigiu a conclusão anterior a partir de evidência |
| Testes relatados pelo Hermes | Login legítimo `True` em ambos; injeção na senha `True` no vulnerável e `False` no corrigido; entrada com aspas causa erro no vulnerável e retorna `False` no corrigido | Comportamento reportado pelo agente; preservar prints/logs para auditoria |

Os resultados de Hermes acima foram **relatados a partir das saídas compartilhadas**, não reproduzidos por este pacote. As duas execuções de `unittest` foram realizadas pelo estudante e relatadas com `OK`. Não reivindicar avaliação independente de ambiente ou código em produção.

## Achado de segurança

- **CWE-89 — SQL Injection** na construção de SQL por interpolação em `examples/sql-injection/app.py`.
- A correção em `examples/sql-injection/app_fixed.py` usa `?` para ambos os parâmetros e `execute(query, (username, password))`.
- Matriz educacional da skill: laboratório `4 × 2 = 8` (moderado); cenário hipotético de produção `5 × 4 = 20` (crítico). **Não é CVSS**.
- MITRE ATT&CK T1190 não se aplica diretamente ao CLI local; apenas seria plausível se o padrão fosse exposto como aplicação pública.

## Aprendizados e riscos residuais

Uma skill não treina um modelo: fornece instruções e conhecimento para conduzir o raciocínio. O caso destacou o valor da **verificação de evidência e da autocorreção de um falso positivo**. A parametrização mitiga a CWE-89 nesta função; não transforma este exemplo em autenticação pronta para produção. No sistema real seriam necessários hash de senhas, controle de tentativas, gestão de sessões e configuração segura.

## Limites

- Não houve teste de infraestrutura real, scanner de produção ou análise de servidores externos.
- A captura da evidência deve preservar o texto do Hermes, sem apresentar inferências como testes executados.
- Os screenshots devem ser adicionados pelo autor nas pastas descritas em `GUIA-EVIDENCIAS.md`.
