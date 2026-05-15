# Base de Conocimiento — gamedev-auditor

Patrones documentados de proyectos de desarrollo de videojuegos.

---

## GDD (Game Design Document)

Documento vivo que define el juego antes y durante el desarrollo:

**Secciones mínimas esperadas:**
- Concepto central (género, mecánica principal, público objetivo)
- Mecánicas de juego detalladas
- Progresión y estructura de niveles o contenido
- Arte y estilo visual (referencias o mood board)
- Sonido y música (estilo, no necesariamente assets)
- Plataformas target y controles

**Señales de alerta:**
- GDD desactualizado respecto al juego implementado
- GDD ausente en proyectos > 1 semana de desarrollo
- GDD de una sola línea sin estructura

---

## Arquitectura — separación de capas

| Capa | Responsabilidad |
|------|----------------|
| Lógica (Model) | Estado del juego, reglas, física, IA |
| Render (View) | Dibujado en pantalla, animaciones, shaders |
| Input (Controller) | Lectura de teclado, mouse, gamepad, touch |

**Señal de alerta:** lógica de juego mezclada con código de render (ej: `if player.x > 100: draw_enemy()`)

---

## Control de versiones — patrones maduros

- Commits descriptivos: `fix: collision detection in level 2` no `cambios`
- Frecuencia mínima: un commit por sesión de trabajo
- `.gitignore` configurado: sin binarios grandes, sin carpetas de build en repo
- Ramas separadas para features experimentales
- Assets grandes: Git LFS o almacenamiento externo

---

## Build funcional

- **Mínimo:** el juego arranca sin errores en una plataforma target
- **Recomendado:** build automatizado (script o CI)
- **Señal de alerta:** build rota por más de 2 días sin fix
- Plataformas comunes: PC (Windows/Linux/Mac), Web (WebGL), Android, iOS

---

## Organización de assets

**Estructura recomendada:**
```
assets/
├── sprites/
│   ├── player/
│   └── enemies/
├── audio/
│   ├── sfx/
│   └── music/
├── fonts/
└── ui/
```

**Naming convention consistente:**
- `snake_case` o `PascalCase`, elegir uno y mantenerlo
- Nombres descriptivos: `player_idle_01.png` no `img1.png`
- Sin espacios en nombres de archivo

---

## Sistema de escenas / estados del juego

**Patrón recomendado (máquina de estados):**
- `MainMenu → Loading → Gameplay → Pause → GameOver → MainMenu`
- Transiciones explícitas y documentadas
- Sin escenas "huérfanas" sin transición de entrada o salida

---

## Señales de alerta críticas

- Sin GDD después de la primera semana
- Todo el código en un solo archivo > 1000 líneas
- Sin commits en > 1 semana (proyecto activo)
- Build rota sin issue registrado
- Assets sin organización ni naming convention

---

_Actualizar este archivo con `/feed <archivo>` al ingresar nuevos casos documentados._
