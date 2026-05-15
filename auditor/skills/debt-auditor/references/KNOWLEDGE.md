# Base de Conocimiento — debt-auditor

Patrones documentados del sistema financiero peruano para negociación de deudas castigadas.

---

## Proceso canónico de 4 pasos

1. **Roteo** — Identificar quién tiene la deuda actualmente (entidad original o cesionaria). Para deudas antiguas (> 2-3 años), alta probabilidad de que hayan sido cedidas a un tercero.
2. **Negociación** — Contactar a la entidad correcta con oferta de pago. Deudas cedidas se negocian con el comprador, no con el banco original.
3. **Levantamiento de castigo** — Solicitar carta de no adeudo o constancia de cancelación para que el registro negativo se limpie en Equifax/Infocorp.
4. **Reinserción al sistema financiero** — Con score limpio, el cliente puede volver a acceder a productos financieros formales.

---

## Variables clave de decisión

| Variable | Impacto |
|----------|---------|
| Monto de deuda | Determina si vale la pena negociar vs ignorar |
| Tiempo de mora | > 5 años: muy probable cesión. < 1 año: aún en banco original |
| Score Equifax/Infocorp | Diagnóstico inicial del estado del cliente |
| Tipo de entidad | Define si es negociable o no |

---

## Entidades innegociables

Las siguientes deudas **no se negocian** por ser entidades del estado:

- **Reactiva Perú** — préstamo estatal COVID-19
- **Impulsa Perú** — programa estatal de empleo
- **Banco de la Nación** — entidad financiera del estado peruano

Intentar negociar estas deudas con descuentos refleja desconocimiento del dominio.

---

## Casos especiales: telefonías

- **Claro, Movistar, Entel, Bitel** — deudas no negociables en términos de descuento
- **Acción requerida:** solicitar **carta de no adeudo** para levantar el castigo en Infocorp
- Error común: ignorar estas deudas pensando que no afectan el score

---

## Rangos reales de descuento documentados

- Rango típico: **60% a 90%** sobre el monto total
- Factores que mejoran el descuento: deuda antigua, monto pequeño, deuda cedida a tercero
- Factores que reducen el descuento: deuda reciente, garantías reales (hipoteca, etc.)

---

## Deudas cedidas a terceros

- Bancos venden carteras de deudas castigadas a empresas recuperadoras
- El comprador típicamente acepta descuentos mayores que el banco original
- **Proceso obligatorio:** hacer roteo primero para identificar al cesionario actual
- No hacer roteo antes de negociar = error de proceso documentado

---

## Score Equifax / Infocorp

- Escala de riesgo: Normal → CPP → Deficiente → Dudoso → Pérdida
- Categoría "Pérdida": deuda castigada, el impacto más severo en el score
- Limpieza del score: solo posible con carta de no adeudo + tiempo de actualización del buró
- Tiempo de actualización típico: 30-90 días hábiles tras la cancelación

---

_Actualizar este archivo con `/feed <archivo>` al ingresar nuevos casos documentados._
