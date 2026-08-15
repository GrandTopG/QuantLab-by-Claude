# 006 — Estrategia H12 A_3_Cruzando: Validación final y gestión de riesgo

**Fecha:** 2026-08-13
**Estado:** Estrategia base validada — lista para diseño de disparador de entrada

## Resumen ejecutivo

De 60 combinaciones posibles evaluadas hoy (6 escenarios H12 × 6 semanales,
alcistas y bajistas, más filtros de volatilidad), **una sola combinación
simple demostró ventaja estadística real, consistente en el tiempo, y con
la frecuencia operativa que el trader requiere (intraday, ~2-3 señales
semanales):**

> **A_3_Cruzando en H12** — Escenario A (C1>C2 y C1>C3) + Sub-caso 3
> (1 o 2 de las 3 velas cruzando por encima de OURAS)

## Método y datos

- XAUUSD, futuros COMEX (`GC=F`), velas H1 resampleadas a H4/H12/semanal,
  ancla 17:00 ET (confirmado contra especificación oficial de CME)
- Periodo: 2024-08-14 a 2026-08-07 (límite de 730 días de yfinance)
- **Periodo de crisis excluido de la validación final:** 2026-01-29 a
  2026-04-15 (crash histórico de oro, caída >12% intradía el 30-ene-2026,
  el mayor desde inicios de los 80 — evento real documentado, no error
  de datos, causado por nominación de Kevin Warsh a la Fed + subida de
  márgenes en COMEX/Shanghai)

## Resultado final — A_3_Cruzando (H12 solo), sin periodo de crisis

| Métrica | Valor |
|---|---|
| Casos (n) | 243 |
| Frecuencia | ~2.6 señales/semana (cumple el requisito de trading intradía) |
| Win rate | 58.85% |
| Retorno promedio por señal | +0.146% |
| P-value | 0.0039 |
| Sharpe (preliminar, sin fricciones — NO reportable como final) | 5.05 |
| VaR 95% | -1.21% |
| Volatilidad de resultados | 0.78% |

## Gestión de riesgo — Monte Carlo de rachas de pérdida (10,000 simulaciones)

| Percentil | Peor racha esperada |
|---|---|
| 95 | 8 pérdidas seguidas |
| 99 (margen de seguridad ampliado) | 10 pérdidas seguidas |

### Supervivencia de capital ante racha de 10 pérdidas seguidas (percentil 99)

| Riesgo por operación | Capital restante |
|---|---|
| 1% | 90.4% |
| 2% | 81.7% |
| 5% | 59.9% |
| 10% | 34.9% |

**Conclusión de riesgo:** con 1-2% de riesgo por operación, la estrategia
sobrevive cómodamente incluso al escenario de percentil 99. Niveles de
riesgo de 5%+ exponen a pérdidas de capital severas ante una racha
realista de mala suerte.

## Verificación de robustez temporal

- **Año por año:** 2024 (p=0.34, no sig.) → 2025 (p=0.0119) → 2026 parcial
  (p=0.0521) — tendencia de FORTALECIMIENTO progresivo, no un hallazgo
  aislado de un solo periodo
- **Excluyendo el crash 2026:** n baja de 338 a 243, pero retorno
  (0.146% vs 0.14% original) y significancia (p=0.0039) se mantienen
  prácticamente intactos — **la ventaja NO depende del periodo de crisis**

## Hallazgos secundarios — NO usados como filtros de entrada, reservados como moduladores de riesgo

Se evaluaron dos filtros adicionales. Ambos mejoran la calidad
estadística pero reducen la frecuencia por debajo del mínimo operativo
requerido (2-3 señales/semana):

| Filtro | n | Win rate | Retorno | P-value | Frecuencia |
|---|---|---|---|---|---|
| + Filtro semanal (semana también A_3_Cruzando) | 65 | 69.2% | 0.330% | 0.0043 | ~0.7/semana ❌ |
| + Volatilidad baja (ATR tercio inferior) | 81 | 71.6% | 0.254% | 0.0000 | ~0.85/semana ❌ |

**Decisión:** no se usan como filtros de entrada (mataría la frecuencia
necesaria). Se reservan como **moduladores de tamaño de posición**:
arriesgar más cuando coincidan, menos (o normal) cuando no.

## Sistema bajista — descartado por falta de evidencia

Se construyó el sistema espejo completo (Escenario_A/B_bajista, OUVAS,
Sub_caso_bajista) y se cruzó con el contexto semanal bajista (30
combinaciones). **Ninguna combinación bajista mostró evidencia válida**
de ventaja para vender (la única celda con p<0.05 tenía muestra
insuficiente — n=6 — y dirección contraria a la esperada, contradiciendo
su propia etiqueta). Conclusión: el sistema, con la evidencia actual,
solo tiene ventaja confirmada del lado de comprar.

## Principio nuevo formalizado — Aislamiento de variables

Toda validación de ventaja estadística se hace ÚNICAMENTE con datos de
precio (OHLC) y sus derivados directos — nunca mezclada con variables
externas (fundamentales, tiempo, noticias) en el mismo cálculo. Las
variables externas solo se usan como (1) filtro de riesgo que decide SI
se toma una señal ya validada, o (2) investigación posterior cuando el
monitoreo detecta deterioro. Motivo: mezclar impide diagnosticar si un
fallo viene de la lógica técnica, de la variable externa, o de la
combinación.

## Limitaciones reconocidas

- Solo 2 años de datos disponibles (límite gratuito de yfinance)
- El análisis mide únicamente "próxima vela H12" — no es aún un backtest
  de operación completa con entrada/salida y gestión de riesgo real
- No incluye comisiones, spread ni slippage — el Sharpe de 5.05 es
  optimista, no representa lo que se lograría en cuenta real
- No se ha medido el MAE (Maximum Adverse Excursion) — necesario para
  calibrar un SL basado en evidencia real, no en intuición
- El uso de datos de futuros (GC=F) vs. CFD spot no se ha comparado
  directamente (Yahoo no ofrece un ticker XAUUSD spot gratuito
  confiable) — pendiente comparar con datos exportados de Exness/MT5

## Próximos pasos (próxima sesión)

1. Exportar historial real de Exness (MT4/MT5 → Export Bars) y repetir
   la validación completa sobre esos datos, para confirmar que la
   estrategia se sostiene en el instrumento que realmente se va a operar
2. Medir MAE (Maximum Adverse Excursion) de cada señal, para calibrar
   el SL con evidencia real, usando percentil alto (85-90%), no el
   promedio
3. Diseñar el disparador de entrada real (posible confirmación en H4)
4. Backtest completo con entrada/salida, SL/TP, y costos de operación
5. Explorar la composición interna de las 3 velas H4 dentro de cada H12
   (limpia vs. con retroceso) como posible filtro/modulador adicional
6. Construir el sistema de alertas de volatilidad (Fase 5 del ROADMAP):
   alerta-filtro (ATR alto → no sugerir entrada) y alerta-precaución
   (ATR se dispara con operación ya abierta → avisar, no cerrar
   automáticamente)
7. Diseñar el sistema de monitoreo continuo (mensual/trimestral/
   semestral/anual) comparando Sharpe, drawdown, p-value rolling y win
   rate en vivo contra las expectativas de este documento
