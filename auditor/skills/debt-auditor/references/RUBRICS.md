# Rúbricas de Scoring — debt-auditor

Criterios de evaluación 1-5 por dimensión. Score total sobre 25 puntos.

---

## Dimensión 1: Proceso (1-5)

Evalúa si se siguió correctamente el proceso canónico de 4 pasos.

| Score | Criterio |
|-------|----------|
| 5 | Los 4 pasos están presentes y en orden correcto. Roteo antes de negociar en deudas antiguas. |
| 4 | 3 de 4 pasos presentes. Pequeña omisión sin impacto en resultado. |
| 3 | 2 de 4 pasos presentes. O proceso correcto pero sin roteo previo en deuda antigua. |
| 2 | Solo 1 paso presente, o proceso ejecutado en orden incorrecto. |
| 1 | Sin proceso reconocible, acciones aleatorias sin estructura. |

---

## Dimensión 2: Conocimiento (1-5)

Evalúa si se distingue correctamente entre deudas negociables e innegociables.

| Score | Criterio |
|-------|----------|
| 5 | Identifica correctamente todas las entidades innegociables. Sabe qué hacer con telefonías (carta de no adeudo). |
| 4 | Identifica la mayoría de innegociables. Pequeño error en un caso borde. |
| 3 | Identifica los casos más obvios (Reactiva, BN) pero falla en casos secundarios (telefonías). |
| 2 | Confunde negociable con innegociable en al menos un caso importante. |
| 1 | No distingue entre tipos de deuda. Propone negociar con entidades estatales. |

---

## Dimensión 3: Métricas (1-5)

Evalúa si se usaron monto, tiempo de mora y score Equifax/Infocorp para tomar decisiones.

| Score | Criterio |
|-------|----------|
| 5 | Las 3 métricas usadas explícitamente para fundamentar cada decisión. |
| 4 | 2 de 3 métricas usadas. La tercera ausente pero no afecta el resultado. |
| 3 | Solo 1 métrica usada consistentemente. |
| 2 | Métricas mencionadas pero no usadas para tomar decisiones concretas. |
| 1 | Decisiones sin respaldo en métricas. Recomendaciones genéricas. |

---

## Dimensión 4: Manejo de errores (1-5)

Evalúa si se detectaron y corrigieron desviaciones del proceso correcto.

| Score | Criterio |
|-------|----------|
| 5 | Detecta errores propios y de terceros. Corrige en el momento. Documenta la corrección. |
| 4 | Detecta la mayoría de errores. Corrige los críticos. |
| 3 | Detecta errores obvios. No detecta errores sutiles. |
| 2 | Detecta errores solo cuando el resultado ya falló. No anticipa. |
| 1 | No detecta errores. Continúa proceso incorrecto sin cuestionarlo. |

---

## Dimensión 5: Madurez (1-5)

Evalúa la consistencia global con los patrones documentados en KNOWLEDGE.md.

| Score | Criterio |
|-------|----------|
| 5 | Consistencia alta con todos los patrones documentados. Agrega valor más allá del proceso básico. |
| 4 | Consistencia alta. Alguna brecha menor en casos borde no documentados. |
| 3 | Consistencia media. Domina los patrones principales, falla en secundarios. |
| 2 | Consistencia baja. Aciertos puntuales pero sin coherencia de conjunto. |
| 1 | Sin consistencia reconocible con la base de conocimiento del dominio. |

---

## Escala de diagnóstico total

| Rango | Diagnóstico |
|-------|-------------|
| 20-25 | **Maduro** — proceso sólido, conocimiento del dominio demostrado |
| 13-19 | **En desarrollo** — bases correctas pero brechas identificables |
| < 13 | **Requiere revisión** — errores críticos o ausencia de estructura |
