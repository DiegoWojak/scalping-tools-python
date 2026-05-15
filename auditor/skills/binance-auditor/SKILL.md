---
name: binance-auditor
description: Audita bots de trading y estrategias automatizadas en Binance. Evalúa si un bot o estrategia cumple con los patrones de madurez del dominio: gestión de riesgo documentada (stop-loss y take-profit definidos), backtest mínimo de 6 meses con datos reales, separación clara entre paper trading y live trading, métricas de performance registradas (PnL, drawdown máximo, win rate, Sharpe ratio), manejo de errores de API con lógica de reconexión, y logs de operaciones con timestamp y razón de entrada/salida. Usar cuando se quiera evaluar la solidez de un bot existente, revisar un reporte de backtesting, o auditar los resultados live de una estrategia automatizada. Score 1-5 por dimensión: gestión de riesgo, backtesting, métricas, robustez, madurez.
compatibility: Claude Code
metadata:
  version: "1.0"
  domain: trading-automatizado-binance
---

# binance-auditor

Auditor especializado en bots de trading y estrategias automatizadas en Binance.

## Propósito

Evalúa si un bot, estrategia o reporte de trading sigue los patrones documentados de madurez para sistemas de trading automatizado en Binance.

## Cómo usar este fork

1. Activar con `/load binance-auditor`
2. Proveer el archivo a auditar con `/audit <archivo>`
3. Recibir score por dimensión + hallazgos
4. Registrar resultado con `/feedback` o `python scripts/feedback.py "<resumen>"`

## Contexto del dominio

- **Exchange objetivo:** Binance (spot y futuros)
- **Tipo de activo:** criptomonedas
- **Casos de uso:** bots algorítmicos, estrategias de scalping, grid trading, arbitraje
- **Riesgo principal:** pérdidas por ausencia de gestión de riesgo o backtesting insuficiente

## Archivos de referencia

| Archivo | Contenido |
|---------|-----------|
| `references/KNOWLEDGE.md` | Patrones detectados de bots y estrategias reales |
| `references/PROTOCOLS.md` | Pasos para ejecutar la auditoría |
| `references/RUBRICS.md` | Criterios de scoring 1-5 por dimensión |

## Scripts

| Script | Uso |
|--------|-----|
| `scripts/feed.py <archivo>` | Ingesta nueva información a KNOWLEDGE.md |
| `scripts/feedback.py "<texto>"` | Registra resultado en assets/FEEDBACK.md |
