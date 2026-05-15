---
name: gamedev-auditor
description: Audita proyectos de desarrollo de videojuegos. Evalúa si un proyecto cumple con los patrones de madurez del dominio: GDD (Game Design Document) presente y actualizado, separación de capas en arquitectura (lógica, render, input), control de versiones con commits descriptivos y frecuentes, build funcional en al menos una plataforma target, assets organizados con naming convention consistente, y sistema de escenas o estados del juego definido. Usar cuando se quiera evaluar el estado de un proyecto de videojuego, revisar su arquitectura, auditar la calidad del proceso de desarrollo, o diagnosticar deuda técnica y organizacional. Score 1-5 por dimensión: documentación, arquitectura, control de versiones, build, assets.
compatibility: Claude Code
metadata:
  version: "1.0"
  domain: desarrollo-videojuegos
---

# gamedev-auditor

Auditor especializado en proyectos de desarrollo de videojuegos.

## Propósito

Evalúa si un proyecto de videojuego sigue los patrones documentados de madurez en proceso, arquitectura y organización.

## Cómo usar este fork

1. Activar con `/load gamedev-auditor`
2. Proveer el archivo a auditar con `/audit <archivo>`
3. Recibir score por dimensión + hallazgos
4. Registrar resultado con `/feedback` o `python scripts/feedback.py "<resumen>"`

## Contexto del dominio

- **Engines comunes:** Unity, Godot, Unreal, Pygame, custom
- **Plataformas target:** PC, mobile, web, consola
- **Casos de uso:** proyectos indie, game jams, proyectos académicos, estudios pequeños
- **Riesgo principal:** deuda técnica acumulada, ausencia de documentación, builds rotas

## Archivos de referencia

| Archivo | Contenido |
|---------|-----------|
| `references/KNOWLEDGE.md` | Patrones detectados de proyectos reales |
| `references/PROTOCOLS.md` | Pasos para ejecutar la auditoría |
| `references/RUBRICS.md` | Criterios de scoring 1-5 por dimensión |

## Scripts

| Script | Uso |
|--------|-----|
| `scripts/feed.py <archivo>` | Ingesta nueva información a KNOWLEDGE.md |
| `scripts/feedback.py "<texto>"` | Registra resultado en assets/FEEDBACK.md |
