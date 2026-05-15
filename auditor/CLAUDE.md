# Auditor Agent System

Sistema de agentes auditores con forks especializados. Cada fork es un skill independiente.

## Arranque

Al abrir este proyecto, listar los skills disponibles:

```
Skills disponibles:
- debt-auditor    → skills/debt-auditor/SKILL.md
- binance-auditor → skills/binance-auditor/SKILL.md
- gamedev-auditor → skills/gamedev-auditor/SKILL.md

Usa /load <skill-name> para activar un fork.
```

## Comandos reconocidos

| Comando | Acción |
|---------|--------|
| `/load <skill-name>` | Activa el fork: carga SKILL.md + references/ |
| `/feed <archivo>` | Ejecuta `scripts/feed.py <archivo>` del fork activo |
| `/audit <archivo>` | Audita el archivo con el fork activo |
| `/feedback` | Muestra `assets/FEEDBACK.md` del fork activo |
| `/status` | Muestra qué fork está activo |

## Progressive Disclosure (respetar siempre)

1. **Discovery** — solo `name` + `description` de cada skill al arrancar
2. **Activation** — carga `SKILL.md` completo + todo `references/` al invocar `/load`
3. **Execution** — `scripts/` y `assets/` solo cuando la tarea los requiere

**Regla crítica:** no mezclar contexto entre forks. Un `/load` reemplaza el contexto del fork anterior.

## Comportamiento al ejecutar /load

1. Leer `skills/<skill-name>/SKILL.md`
2. Leer `skills/<skill-name>/references/KNOWLEDGE.md`
3. Leer `skills/<skill-name>/references/PROTOCOLS.md`
4. Leer `skills/<skill-name>/references/RUBRICS.md`
5. Confirmar: "Fork `<skill-name>` activado. Listo para auditar."

## Comportamiento al ejecutar /audit

1. Verificar fork activo (si ninguno, pedir `/load` primero)
2. Leer el archivo objetivo
3. Aplicar PROTOCOLS.md del fork activo paso a paso
4. Puntuar según RUBRICS.md del fork activo
5. Mostrar hallazgos + score total
6. Sugerir: `python scripts/feedback.py "<resumen>"` para registrar resultado

## Comportamiento al ejecutar /feed

1. Verificar fork activo
2. Ejecutar: `python skills/<fork>/scripts/feed.py <archivo>`
3. Confirmar qué se agregó a KNOWLEDGE.md

## Notas

- Sin dependencia de Anthropic SDK — todo corre dentro de Claude Code
- Scripts en Python puro
- Contenido en español, código en inglés
