# Rúbricas de Scoring — gamedev-auditor

Criterios de evaluación 1-5 por dimensión. Score total sobre 25 puntos.

---

## Dimensión 1: Documentación (1-5)

Evalúa la presencia y calidad del GDD y documentación del proyecto.

| Score | Criterio |
|-------|----------|
| 5 | GDD completo con todas las secciones mínimas. Actualizado respecto al estado actual del juego. |
| 4 | GDD presente con la mayoría de secciones. Pequeñas brechas en secciones secundarias. |
| 3 | GDD presente pero incompleto (< 50% de secciones mínimas) o levemente desactualizado. |
| 2 | GDD existe pero es de una sola página sin estructura, o muy desactualizado. |
| 1 | Sin GDD, o solo un README de una línea. |

---

## Dimensión 2: Arquitectura (1-5)

Evalúa la separación de capas lógica / render / input.

| Score | Criterio |
|-------|----------|
| 5 | Separación clara de las 3 capas. Carpetas o módulos independientes. Sin acoplamiento entre capas. |
| 4 | 2 de 3 capas claramente separadas. Acoplamiento menor en la tercera. |
| 3 | Separación parcial. Lógica mezclada con render en algunos módulos. |
| 2 | Separación mínima reconocible. Mayoría del código mezclado. |
| 1 | Todo en un solo archivo o módulo. Sin separación reconocible. |

---

## Dimensión 3: Control de versiones (1-5)

Evalúa la calidad de commits, frecuencia y uso de git.

| Score | Criterio |
|-------|----------|
| 5 | Commits descriptivos con convención clara. Frecuencia ≥ 1 por sesión. `.gitignore` correcto. Sin binarios en historial. |
| 4 | Mayoría de commits descriptivos. Frecuencia correcta. Un issue menor en .gitignore. |
| 3 | Mix de commits buenos y genéricos. Frecuencia irregular pero presente. |
| 2 | Commits mayormente genéricos (`update`, `fix`, `cambios`). Largos períodos sin commits. |
| 1 | Sin historial de commits, o historial de 1-2 commits para todo el proyecto. |

---

## Dimensión 4: Build (1-5)

Evalúa la existencia y calidad del build funcional.

| Score | Criterio |
|-------|----------|
| 5 | Build funcional en plataforma target. Instrucciones documentadas. Script de build automatizado. |
| 4 | Build funcional. Instrucciones documentadas pero proceso manual. |
| 3 | Build funcional pero sin instrucciones claras para reproducirlo. |
| 2 | Build existente pero con errores conocidos no resueltos. |
| 1 | Sin build, o build rota sin issue registrado. |

---

## Dimensión 5: Assets (1-5)

Evalúa la organización y naming convention de los assets del proyecto.

| Score | Criterio |
|-------|----------|
| 5 | Assets organizados por tipo en subcarpetas. Naming convention consistente en todo el proyecto. Sin assets sin usar. |
| 4 | Assets organizados. Naming convention mayormente consistente con excepciones menores. |
| 3 | Estructura parcial. Mix de convenciones. Algunos assets fuera de lugar. |
| 2 | Assets agrupados sin estructura clara. Naming inconsistente. |
| 1 | Assets en raíz del proyecto, sin naming convention, mezcla de tipos. |

---

## Escala de diagnóstico total

| Rango | Diagnóstico |
|-------|-------------|
| 20-25 | **Maduro** — proyecto bien estructurado, listo para escalar |
| 13-19 | **En desarrollo** — fundamentos presentes, deuda técnica manejable |
| < 13 | **Requiere revisión** — deuda técnica alta, riesgo de no completar el proyecto |
