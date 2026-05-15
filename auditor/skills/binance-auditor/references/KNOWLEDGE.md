# Base de Conocimiento — binance-auditor

Patrones documentados de bots de trading y estrategias automatizadas en Binance.

---

## Gestión de riesgo — patrones obligatorios

- **Stop-loss** definido por operación, no opcional
- **Take-profit** con ratio riesgo/beneficio documentado (mínimo 1:1.5 recomendado)
- **Tamaño de posición** calculado en función del capital total (ej: máximo 2% del capital por trade)
- Ausencia de stop-loss = señal de alerta crítica en auditoría

---

## Backtesting — estándares mínimos

| Criterio | Mínimo aceptable |
|----------|-----------------|
| Cobertura temporal | 6 meses de datos históricos |
| Calidad de datos | Datos OHLCV reales de Binance, no sintéticos |
| Condiciones de mercado cubiertas | Bull, bear y lateral |
| Comisiones incluidas | Sí, con taker/maker fees de Binance |
| Slippage modelado | Sí para estrategias de alto volumen |

---

## Separación paper trading vs live trading

- Código debe distinguir explícitamente entre modo simulación y modo real
- Variable de entorno o flag de configuración recomendado (ej: `TRADING_MODE=paper`)
- Errores comunes: compartir estado entre modos, usar saldo real en pruebas

---

## Métricas de performance documentadas

| Métrica | Descripción |
|---------|-------------|
| PnL (Profit and Loss) | Ganancia/pérdida total en USD o BTC |
| Drawdown máximo | Peor caída desde un pico antes de recuperación |
| Win rate | Porcentaje de operaciones ganadoras |
| Sharpe ratio | Retorno ajustado por riesgo (> 1.0 aceptable, > 2.0 bueno) |
| Número de trades | Validez estadística (mínimo 30-50 trades en backtest) |

---

## Manejo de errores de API

- Lógica de reconexión automática ante desconexión de WebSocket
- Manejo de rate limits de Binance (errores 429, 418)
- Manejo de errores de fondos insuficientes sin crash del bot
- Retry con backoff exponencial para errores temporales

---

## Logs de operaciones

Cada operación debe registrar:
- Timestamp de entrada y salida
- Par de trading
- Precio de entrada, precio de salida, stop-loss, take-profit
- Razón de la señal de entrada (indicador, condición)
- PnL de la operación
- ID de orden en Binance

---

## Señales de alerta en auditoría

- Bot sin stop-loss → riesgo de pérdida total
- Backtest < 3 meses → muestra insuficiente
- Win rate > 90% en backtest → posible overfitting
- Sin logs → imposible auditar post-mortem
- Sin separación paper/live → riesgo de operar con capital real en pruebas

---

_Actualizar este archivo con `/feed <archivo>` al ingresar nuevos casos documentados._
