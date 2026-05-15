# Protocolos de Auditoría — binance-auditor

Pasos para ejecutar una auditoría de bot de trading o estrategia automatizada en Binance.

---

## Paso 1 — Verificar existencia de gestión de riesgo

**Qué hacer:**
- Buscar definición explícita de stop-loss en el código o reporte
- Buscar definición de take-profit
- Verificar si el tamaño de posición está calculado en función del capital

**Señal de madurez:** stop-loss y take-profit con valores concretos, no "lo ajusto manualmente"
**Señal de alerta crítica:** ausencia total de stop-loss — marcar como error crítico en reporte

---

## Paso 2 — Revisar documentación de backtest

**Qué hacer:**
- Verificar cobertura temporal (mínimo 6 meses)
- Verificar que los datos sean reales de Binance, no sintéticos
- Verificar si se incluyeron comisiones (taker/maker fees)
- Verificar si se cubrieron distintas condiciones de mercado (bull, bear, lateral)

**Señal de alerta:**
- Backtest sobre solo 1-2 meses
- Win rate irreal (> 90%) que sugiere overfitting
- Sin comisiones incluidas — los resultados son irreales

---

## Paso 3 — Evaluar métricas de performance reportadas

**Qué hacer:**
- Verificar que el reporte incluya: PnL, drawdown máximo, win rate, Sharpe ratio
- Verificar número mínimo de trades para validez estadística (mínimo 30)
- Comparar métricas con benchmarks razonables

**Señal de inmadurez:** reporte con solo "ganó X%" sin desglose de métricas

---

## Paso 4 — Verificar manejo de errores y reconexión

**Qué hacer:**
- Buscar en el código manejo de errores de WebSocket
- Verificar manejo de rate limits de Binance (429, 418)
- Verificar manejo de fondos insuficientes
- Verificar si existe retry con backoff

**Señal de alerta:** ausencia de try/except alrededor de llamadas a API

---

## Paso 5 — Comparar paper trading vs live (si existen ambos)

**Qué hacer:**
- Verificar si existe separación explícita entre modos
- Si existen resultados de ambos modos, comparar métricas
- Diferencia > 30% entre paper y live = señal de overfitting o slippage no modelado

---

## Formato del reporte de auditoría

```
## Resultado de Auditoría — binance-auditor
**Fecha:** YYYY-MM-DD
**Bot/Estrategia auditada:** <nombre o descripción>

### Hallazgos por paso
1. Gestión de riesgo: <stop-loss/take-profit definidos — sí/no/parcial>
2. Backtest: <cobertura, calidad de datos, comisiones incluidas>
3. Métricas: <PnL, drawdown, win rate, Sharpe — presentes/ausentes>
4. Robustez: <manejo de errores — detalle>
5. Paper vs live: <comparación — N/A si no aplica>

### Score por dimensión
| Dimensión | Score (1-5) | Justificación |
|-----------|-------------|---------------|
| Gestión de riesgo | X | |
| Backtesting | X | |
| Métricas | X | |
| Robustez | X | |
| Madurez | X | |
| **Total** | **XX/25** | |

### Diagnóstico
- 20-25: Maduro
- 13-19: En desarrollo
- < 13: Requiere revisión urgente
```
