# QuantLab — Estrategia recomendada: RCT-H12 (Ruptura Confirmada en Tendencia)

> Documento de referencia único: descripción completa de la estrategia
> recomendada, su fundamento lógico, y toda la evidencia estadística
> que la respalda, calculada hasta ahora.

---

## Nombre de la estrategia

**RCT-H12 — Ruptura Confirmada en Tendencia**
(nombre técnico interno de la señal: `A_3_Cruzando`)

## Descripción completa de la regla

Se opera sobre velas H12 (12 horas) de XAUUSD, ancladas al cierre de
futuros de COMEX (17:00 ET).

### Variables base

- **C1** = Close de la vela H12 más reciente ya cerrada
- **C2** = Close de la vela H12 anterior
- **C3** = Close de la vela H12 dos posiciones atrás
- **OURAS** = Open de la última vela roja (bajista) antes de que
  arrancara la tendencia alcista actual — funciona como nivel de
  resistencia de referencia. Se calcula marcando cada vela roja
  (`Close < Open`) y "arrastrando" (forward-fill) su Open a través de
  todas las velas verdes posteriores, hasta que aparezca una vela roja
  nueva que lo reemplace.

### Condición de Escenario (tendencia)

**Escenario A** (también llamado "Escenario 1"): `C1 > C2` Y `C1 > C3`
— la vela más reciente es más alta que las 2 anteriores: tendencia
alcista fuerte y sin ambigüedad.

*(Existe también el Escenario B / "Escenario 2": `C1 < C2` Y `C1 > C3`
— tendencia alcista débil. No forma parte de la estrategia
recomendada, no mostró ventaja estadística.)*

### Condición de Sub-caso (posición respecto a OURAS)

Se cuenta cuántas de las 3 velas (C1, C2, C3) están por encima de
OURAS:

- **Sub-caso 1 "Limpio"**: las 3 por encima — SIN ventaja (descartado)
- **Sub-caso 2 "Sin cruzar"**: las 3 por debajo — SIN ventaja (descartado)
- **Sub-caso 3 "Cruzando"**: 1 o 2 de las 3 por encima — **CON ventaja
  confirmada, es la señal de la estrategia**

### Regla de entrada (definición completa de la señal)

> **Comprar cuando: Escenario A (C1>C2 y C1>C3) Y Sub-caso 3
> (exactamente 1 o 2 de C1/C2/C3 están por encima de OURAS).**

---

## Fundamento lógico (Principio Institucional 6)

**¿Por qué debería existir ventaja aquí, más allá del dato estadístico?**

La señal captura el momento específico en que una tendencia alcista ya
confirmada (Escenario A) está **rompiendo activamente** una resistencia
técnica — ni ya la rompió hace tiempo (Sub-caso 1), ni todavía no la
toca (Sub-caso 2). Hipótesis de por qué esto tendría ventaja real:

1. Cuando el precio rompe una resistencia mientras la tendencia de
   fondo ya es fuerte, es consistente con compradores nuevos
   absorbiendo la oferta que antes frenaba el precio en ese nivel.
2. Traders en corto que apostaban a que la resistencia aguantaría
   probablemente se ven forzados a cerrar (comprar para cubrirse)
   cuando ven la ruptura — añade compras forzadas, no solo orgánicas.
3. Es coherente con el hallazgo de que el Sub-caso 1 (ya confirmado,
   sin ambigüedad) NO tiene ventaja: una vez que "todo el mundo ya lo
   ve", el movimiento de absorción de oferta y cobertura de cortos ya
   ocurrió — entrar ahí es llegar tarde.

**Honestidad metodológica:** esta lógica se articuló *después* de
encontrar el patrón estadísticamente (orden invertido respecto al
Principio 6 ideal). Los controles de robustez (p-value, consistencia
año por año, exclusión de periodo de crisis) mitigan el riesgo de que
sea casualidad, pero no lo eliminan del todo — el walk-forward
analysis (pendiente) sería la validación definitiva.

**Evidencia adicional pendiente de explorar:** correlación con volumen
real (¿hay más volumen durante A_3_Cruzando que en otros escenarios?
— variable distinta a volatilidad/ATR, no explorada aún).

---

## ¿Comparte lógica con otras estrategias del portafolio?

No — es la única estrategia validada por ahora. Al evaluar futuras
estrategias (incluida la que el usuario tiene pendiente de describir),
verificar si comparten esta misma lógica de "ruptura + tendencia
confirmada" — de ser así, no aportarían tanta diversificación real
como parece a primera vista.

---

## Evidencia estadística completa (Categoría A — ¿existe ventaja real?)

| Métrica | Valor |
|---|---|
| Instrumento | XAUUSD, futuros COMEX (GC=F) |
| Periodo analizado | 2024-08-14 a 2026-08-07 |
| Periodo de crisis excluido de esta validación | 2026-01-29 a 2026-04-15 (crash histórico de oro) |
| n (casos) | 243 |
| Frecuencia | ~2.6 señales/semana |
| Win rate | 58.85% |
| Retorno promedio por señal | +0.146% |
| P-value (t-test) | 0.0039 |
| Volatilidad de resultados | 0.78% |
| Sharpe (preliminar — NO incluye costos, no reportable como final) | 5.05 |
| VaR 95% (percentil 5 de retornos) | -1.21% |

### Robustez temporal

| Año | n | Retorno promedio | P-value |
|---|---|---|---|
| 2024 | 113 | +0.06% | 0.3414 (no significativo solo) |
| 2025 | 144 | +0.16% | 0.0119 |
| 2026 (parcial) | 81 | +0.23% | 0.0521 (borderline) |

Tendencia de fortalecimiento progresivo — no depende de un año aislado.

### Robustez sin el periodo de crisis

Al excluir el crash de 2026, n baja de 338 a 243, pero el retorno
promedio (+0.146% vs +0.14% original) y el p-value (0.0039) se
mantienen prácticamente intactos — **la ventaja no depende del evento
excepcional**.

---

## Gestión de riesgo (Categoría B)

### Monte Carlo de rachas de pérdida (10,000 simulaciones)

| Percentil | Peor racha de pérdidas seguidas |
|---|---|
| 95 | 8 |
| 99 (margen de seguridad ampliado) | 10 |

### Supervivencia de capital ante racha de 10 pérdidas seguidas (percentil 99)

| Riesgo por operación | Capital restante |
|---|---|
| 1% | 90.4% |
| 2% | 81.7% |
| 5% | 59.9% |
| 10% | 34.9% |

**Recomendación de riesgo:** 1-2% por operación — sobrevive cómodamente
incluso al escenario de percentil 99.

---

## Alternativas evaluadas y descartadas como filtro de entrada (reservadas como moduladores de riesgo)

| Versión | n | Win rate | Retorno | P-value | Frecuencia |
|---|---|---|---|---|---|
| + Filtro semanal (semana también A_3_Cruzando) | 65 | 69.2% | 0.330% | 0.0043 | ~0.7/semana — insuficiente |
| + Volatilidad baja (ATR tercio inferior) | 81 | 71.6% | 0.254% | 0.0000 | ~0.85/semana — insuficiente |

Ambas mejoran la calidad pero no cumplen el mínimo de frecuencia
operativa requerido (2-3 señales/semana, trading intradía). Se
reservan como moduladores de tamaño de posición: arriesgar más cuando
coincidan con la señal base, menos cuando no.

## Sistema bajista — evaluado y descartado

Se construyó el sistema espejo completo (variables OUVAS, Escenarios
A/B bajistas). Ninguna de las 30 combinaciones bajistas cruzadas mostró
evidencia válida de ventaja para vender.

---

## Pendiente — para completar la validación (ver `CHECKLIST_VALIDACION_ESTRATEGIA.md`)

- MAE / MFE (en progreso al momento de este documento)
- Comparación vs Buy & Hold
- Backtest completo con entrada/salida real, SL/TP, costos
- Walk-forward / out-of-sample testing
- Sortino Ratio, Kelly Criterion, probabilidad de ruina formal
- Drawdown máximo real (solo aproximado por ahora)

---

*Documento generado como snapshot de la estrategia recomendada al
2026-08-13. Actualizar conforme avancen las métricas pendientes.*
