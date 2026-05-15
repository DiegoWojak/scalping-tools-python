---
name: debt-auditor
description: Audita procesos de negociación de deudas en el sistema financiero peruano. Evalúa si una sesión, transcripción o reporte sigue los patrones de madurez del dominio: proceso de 4 pasos (roteo → negociación → levantamiento de castigo → reinserción), distinción entre deudas negociables e innegociables (Reactiva Perú, Impulso Perú, Banco de la Nación, telefonías), uso correcto de métricas como monto, tiempo de mora y score Equifax/Infocorp. Usar cuando se quiera evaluar si un operador o sistema maneja correctamente casos de deuda castigada, deudas cedidas a terceros, y rangos reales de descuento documentados (60%-90%). Score 1-5 por dimensión: proceso, conocimiento, métricas, manejo de errores, madurez.
compatibility: Claude Code
metadata:
  version: "1.0"
  domain: deuda-financiera-peru
---

# debt-auditor

Auditor especializado en negociación de deudas en el sistema financiero peruano.

## Propósito

Evalúa si una sesión de negociación, transcripción de video o reporte de caso sigue los patrones documentados de madurez en el dominio de deuda castigada en Perú.

## Cómo usar este fork

1. Activar con `/load debt-auditor`
2. Proveer el archivo a auditar con `/audit <archivo>`
3. Recibir score por dimensión + hallazgos
4. Registrar resultado con `/feedback` o `python scripts/feedback.py "<resumen>"`

## Contexto del dominio

- **Sistema objetivo:** entidades financieras peruanas (bancos, financieras, cajas)
- **Tipo de deuda:** castigada (mora > 365 días en mayoría de entidades)
- **Actores:** operador de negociación, entidad original o cesionaria, cliente deudor
- **Herramienta clave:** score Equifax / Infocorp como diagnóstico inicial

## Archivos de referencia

| Archivo | Contenido |
|---------|-----------|
| `references/KNOWLEDGE.md` | Patrones detectados de casos reales |
| `references/PROTOCOLS.md` | Pasos para ejecutar la auditoría |
| `references/RUBRICS.md` | Criterios de scoring 1-5 por dimensión |

## Scripts

| Script | Uso |
|--------|-----|
| `scripts/feed.py <archivo>` | Ingesta nueva información a KNOWLEDGE.md |
| `scripts/feedback.py "<texto>"` | Registra resultado en assets/FEEDBACK.md |
