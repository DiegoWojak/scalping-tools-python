# Protocolos de Auditoría — debt-auditor

Pasos para ejecutar una auditoría de sesión de negociación de deudas.

---

## Paso 1 — Identificar entidades involucradas

**Qué hacer:**
- Listar todas las entidades mencionadas en el documento auditado
- Clasificar cada entidad: banco, financiera, caja, entidad estatal, telefonía, cesionaria

**Preguntas clave:**
- ¿Se mencionan entidades del estado (Reactiva, Impulsa, Banco de la Nación)?
- ¿Hay deudas con telefonías (Claro, Movistar)?
- ¿Se distingue entre entidad original y cesionaria?

**Resultado esperado:** lista de entidades con su clasificación

---

## Paso 2 — Verificar si aplica el proceso de 4 pasos

**Qué hacer:**
- Buscar evidencia de cada paso en el documento:
  1. Roteo: ¿se identificó quién tiene la deuda actualmente?
  2. Negociación: ¿se contactó a la entidad correcta?
  3. Levantamiento: ¿se solicitó carta de no adeudo?
  4. Reinserción: ¿se planificó la reintegración al sistema financiero?

**Señales de proceso correcto:**
- Se hizo roteo antes de intentar negociar
- Se negoció con la entidad que tiene la deuda ahora (no el banco original si fue cedida)
- Se mencionó el proceso de levantamiento de castigo

**Señales de proceso incorrecto:**
- Intento de negociar sin roteo previo en deudas antiguas
- Ignorar el paso de levantamiento de castigo

---

## Paso 3 — Detectar tratamiento de deudas innegociables

**Qué hacer:**
- Verificar si aparecen entidades innegociables (Reactiva Perú, Impulsa Perú, Banco de la Nación)
- Verificar si se propusieron descuentos o negociaciones para estas deudas

**Señal de error crítico:**
- Proponer negociación con descuento en deudas estatales
- Ignorar la deuda de telefonías cuando aparece en el reporte Infocorp

**Acción esperada para telefonías:**
- No negociar descuento, sino gestionar carta de no adeudo

---

## Paso 4 — Evaluar uso de métricas

**Qué hacer:**
- Verificar si se usaron las 3 métricas clave para tomar decisiones:
  1. **Monto** de la deuda
  2. **Tiempo de mora** (antigüedad de la deuda)
  3. **Score Equifax/Infocorp** como diagnóstico inicial

**Señal de madurez:** las decisiones se justifican con datos concretos (montos, fechas, score)
**Señal de inmadurez:** decisiones sin respaldo en métricas, recomendaciones genéricas

---

## Paso 5 — Verificar roteo antes de negociar deudas antiguas

**Qué hacer:**
- Para deudas con > 2-3 años de mora, verificar si se realizó roteo
- Confirmar que no se intentó negociar directamente con el banco original sin verificar cesión

**Deuda antigua sin roteo previo:** error de proceso, reducir score en dimensión "Proceso"

---

## Formato del reporte de auditoría

```
## Resultado de Auditoría — debt-auditor
**Fecha:** YYYY-MM-DD
**Documento auditado:** <nombre o descripción>

### Hallazgos por paso
1. Entidades: <lista y clasificación>
2. Proceso 4 pasos: <sí/parcial/no — detalle>
3. Innegociables: <correcto/error — detalle>
4. Métricas: <usadas/ausentes — detalle>
5. Roteo: <aplicado/omitido — detalle>

### Score por dimensión
| Dimensión | Score (1-5) | Justificación |
|-----------|-------------|---------------|
| Proceso | X | |
| Conocimiento | X | |
| Métricas | X | |
| Manejo de errores | X | |
| Madurez | X | |
| **Total** | **XX/25** | |

### Diagnóstico
- 20-25: Maduro
- 13-19: En desarrollo
- < 13: Requiere revisión urgente
```
