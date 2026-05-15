# Rúbricas de Scoring — binance-auditor

Criterios de evaluación 1-5 por dimensión. Score total sobre 25 puntos.

---

## Dimensión 1: Gestión de riesgo (1-5)

Evalúa si stop-loss y take-profit están definidos y aplicados correctamente.

| Score | Criterio |
|-------|----------|
| 5 | Stop-loss y take-profit definidos con valores concretos. Tamaño de posición calculado sobre capital total. |
| 4 | Stop-loss y take-profit presentes. Tamaño de posición fijo pero documentado. |
| 3 | Stop-loss presente, take-profit ausente o viceversa. |
| 2 | Stop-loss mencionado pero no implementado consistentemente. |
| 1 | Sin stop-loss. Riesgo ilimitado por operación. |

---

## Dimensión 2: Backtesting (1-5)

Evalúa la cobertura temporal y calidad del backtest.

| Score | Criterio |
|-------|----------|
| 5 | Backtest ≥ 6 meses, datos reales, comisiones incluidas, cubre bull/bear/lateral. |
| 4 | Backtest ≥ 6 meses, datos reales, comisiones incluidas. Condiciones de mercado parciales. |
| 3 | Backtest 3-6 meses, o datos reales sin comisiones. |
| 2 | Backtest < 3 meses, o datos sintéticos, o sin comisiones. |
| 1 | Sin backtest, o backtest con resultados claramente irreal (win rate > 95%). |

---

## Dimensión 3: Métricas (1-5)

Evalúa si PnL, drawdown, win rate y Sharpe ratio están documentados.

| Score | Criterio |
|-------|----------|
| 5 | Las 4 métricas documentadas con valores concretos. Número de trades ≥ 30. |
| 4 | 3 de 4 métricas documentadas. |
| 3 | 2 de 4 métricas documentadas. |
| 2 | Solo PnL reportado, sin desglose de riesgo. |
| 1 | Sin métricas documentadas, o solo "ganó X%" sin contexto. |

---

## Dimensión 4: Robustez (1-5)

Evalúa el manejo de errores de API y casos borde.

| Score | Criterio |
|-------|----------|
| 5 | Manejo de WebSocket, rate limits, fondos insuficientes. Retry con backoff. Logs completos. |
| 4 | Manejo de la mayoría de errores. Un caso borde no cubierto. |
| 3 | Manejo de errores básicos (try/except). Sin retry ni lógica avanzada. |
| 2 | Manejo de errores parcial. Algunos paths críticos sin cobertura. |
| 1 | Sin manejo de errores. El bot crasha ante cualquier error de API. |

---

## Dimensión 5: Madurez (1-5)

Evalúa la consistencia entre backtest y resultados live, y la coherencia global.

| Score | Criterio |
|-------|----------|
| 5 | Diferencia paper/live < 15%. Estrategia coherente con condiciones de mercado actuales. |
| 4 | Diferencia paper/live 15-30%. Explicación documentada de la diferencia. |
| 3 | Diferencia paper/live 30-50%, o sin datos live para comparar. |
| 2 | Diferencia paper/live > 50%. Sin explicación. |
| 1 | Sin separación paper/live, o resultados live contradicen backtest sin análisis. |

---

## Escala de diagnóstico total

| Rango | Diagnóstico |
|-------|-------------|
| 20-25 | **Maduro** — bot sólido con gestión de riesgo y métricas claras |
| 13-19 | **En desarrollo** — bases correctas pero brechas en robustez o backtesting |
| < 13 | **Requiere revisión** — riesgo operacional alto, no apto para live trading |
