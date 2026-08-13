# 005 — Estrategia H12/H4: Escenarios de tendencia y validación estadística

**Fecha:** 2026-08-12
**Estado:** En progreso — hallazgo preliminar prometedor

## Objetivo
Cuantificar el sistema de trading personal basado en análisis multi-timeframe
H12/H4, formalizando la lógica de "tendencia definida" e "intención de
continuación vs cambio" en reglas matemáticas exactas, y validar si alguna
combinación de reglas muestra ventaja estadística real.

## Método
- Datos: XAUUSD, velas H1 (2 años, límite de yfinance), resampleadas a H4
  y H12 con ancla en 17:00 EST (cierre de Nueva York / convención de
  futuros COMEX)
- Definición de variables: C1 (cierre última vela H12), C2 (penúltima),
  C3 (antepenúltima), OURAS (Open de la Última vela Roja Antes de la Subida)
- Escenario A: C1 > C2 y C1 > C3 (tendencia alcista fuerte)
- Escenario B: C1 < C2 pero C1 > C3 (tendencia alcista débil)
- Sub-caso 1 (Limpio): C1, C2, C3 todas > OURAS
- Sub-caso 2 (Sin cruzar): C1, C2, C3 todas < OURAS
- Sub-caso 3 (Cruzando): 1 o 2 de las 3 > OURAS
- Análisis exploratorio: retorno y dirección de la vela H12 inmediatamente
  siguiente a cada combinación detectada
- T-test de una muestra sobre cada combinación, y desglose año por año
  para verificar consistencia temporal

## Resultados — resumen de las 6 combinaciones

| Combinación | Casos | % Siguiente alcista | Retorno prom. siguiente | P-value |
|---|---|---|---|---|
| A_1_Limpio | 135 | 48.1% | -0.06% | 0.4288 |
| A_2_Sin_cruzar | 50 | 52.0% | +0.17% | 0.1398 |
| **A_3_Cruzando** | **338** | **58.3%** | **+0.14%** | **0.0012** |
| B_1_Limpio | 2 | — | — | (muestra insuficiente) |
| B_2_Sin_cruzar | 98 | 56.1% | +0.06% | 0.5176 |
| B_3_Cruzando | 65 | 41.5% | -0.14% | 0.3305 |

## Resultados — A_3_Cruzando, desglose por año

| Año | Casos | Retorno promedio | P-value |
|---|---|---|---|
| 2024 | 113 | +0.06% | 0.3414 |
| 2025 | 144 | +0.16% | 0.0119 |
| 2026 (parcial) | 81 | +0.23% | 0.0521 |

## Hallazgos
- De las 6 combinaciones posibles (Escenario A/B × Sub-caso 1/2/3), solo
  **A_3_Cruzando** muestra evidencia estadísticamente significativa de
  ventaja (p=0.0012 sobre el total de 338 casos).
- Contrario a la intuición inicial, la confirmación "limpia" (Sub-caso 1,
  ya superó la resistencia hace rato) NO mostró ventaja — el momento de
  mayor señal parece ser durante la ruptura activa de la resistencia
  (Sub-caso 3), no después de confirmada.
- El desglose año por año muestra una tendencia de FORTALECIMIENTO
  progresivo (retorno promedio y significancia mejorando de 2024 a 2026),
  no un resultado aislado de un solo periodo — reduce (sin eliminar) la
  preocupación de que sea un espejismo de un tramo específico.
- 2026 (datos parciales) está justo en el límite del umbral de
  significancia (p=0.0521) — pendiente de confirmar con más datos del año.
- El análisis solo mide la vela H12 INMEDIATAMENTE siguiente — no
  representa aún el resultado de una operación completa con entrada/salida.

## Limitaciones reconocidas
- Solo 2 años de historia disponible (límite de yfinance para datos H1)
- Este análisis es exploratorio (mira 1 vela hacia adelante), no un
  backtest de estrategia completa con entrada/salida y gestión de riesgo
- No se ha verificado si el resultado depende del contexto de mercado
  fuertemente alcista de 2025-2026 (pendiente: