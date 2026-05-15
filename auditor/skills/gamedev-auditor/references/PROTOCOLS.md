# Protocolos de Auditoría — gamedev-auditor

Pasos para ejecutar una auditoría de proyecto de desarrollo de videojuego.

---

## Paso 1 — Verificar existencia y calidad del GDD

**Qué hacer:**
- Buscar documento de diseño (GDD, design doc, game brief)
- Evaluar si cubre las secciones mínimas: concepto, mecánicas, plataformas, arte, sonido
- Verificar que esté actualizado respecto al estado actual del proyecto

**Señal de madurez:** GDD con secciones completas y actualizado
**Señal de alerta:** sin GDD, o GDD de una sola línea, o desactualizado > 1 versión

---

## Paso 2 — Evaluar separación de capas en arquitectura

**Qué hacer:**
- Revisar estructura de archivos o descripción de arquitectura
- Verificar si la lógica de juego está separada del código de render
- Verificar si el manejo de input está en su propia capa

**Señal de madurez:** carpetas o módulos claramente separados por responsabilidad
**Señal de alerta:** un solo archivo con todo mezclado, o funciones de render con lógica de negocio

---

## Paso 3 — Revisar historial de commits y control de versiones

**Qué hacer:**
- Revisar mensajes de commit (si hay acceso al repo)
- Verificar frecuencia de commits
- Verificar si existe `.gitignore` apropiado
- Verificar si hay archivos binarios grandes en el historial

**Señal de madurez:** commits descriptivos, frecuentes, con convención clara
**Señal de alerta:** commits genéricos (`cambios`, `update`, `fix`), largos períodos sin commits

---

## Paso 4 — Verificar si existe build funcional

**Qué hacer:**
- Verificar si hay instrucciones de build en el README o documentación
- Verificar si hay scripts de build automatizados
- Verificar en qué plataforma se puede ejecutar el build actual

**Señal de madurez:** build funcional documentado, instrucciones claras para reproducirlo
**Señal de alerta:** sin build, build rota sin issue registrado, instrucciones de build ausentes

---

## Paso 5 — Evaluar organización de assets

**Qué hacer:**
- Revisar estructura de carpetas de assets
- Verificar si existe naming convention y si es consistente
- Verificar si hay assets sin usar en el repo (deuda de tamaño)

**Señal de madurez:** assets organizados por tipo, naming convention consistente en todo el proyecto
**Señal de alerta:** assets en la raíz del proyecto, nombres como `img1.png`, `sound_final_v2_DEFINITIVO.mp3`

---

## Formato del reporte de auditoría

```
## Resultado de Auditoría — gamedev-auditor
**Fecha:** YYYY-MM-DD
**Proyecto auditado:** <nombre o descripción>

### Hallazgos por paso
1. GDD: <presente/ausente — calidad>
2. Arquitectura: <capas separadas/mezcladas — detalle>
3. Control de versiones: <commits descriptivos/genéricos — frecuencia>
4. Build: <funcional/rota/ausente — plataforma>
5. Assets: <organizados/desorganizados — naming convention>

### Score por dimensión
| Dimensión | Score (1-5) | Justificación |
|-----------|-------------|---------------|
| Documentación | X | |
| Arquitectura | X | |
| Control de versiones | X | |
| Build | X | |
| Assets | X | |
| **Total** | **XX/25** | |

### Diagnóstico
- 20-25: Maduro
- 13-19: En desarrollo
- < 13: Requiere revisión urgente
```
