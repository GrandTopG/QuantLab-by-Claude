# 001 — Exploración inicial de datos XAUUSD

**Fecha:** 2026-08-03
**Estado:** Completado

## Objetivo
Establecer el pipeline básico de descarga, limpieza y visualización de datos
históricos del oro (XAUUSD / GC=F), como base para todo el trabajo de
investigación futuro en QuantLab.

## Método
- Fuente de datos: Yahoo Finance, vía librería `yfinance`
- Activo: GC=F (futuros de oro, proxy de XAUUSD)
- Periodo: 1 año, velas diarias (interval="1d")
- Herramientas: pandas (manejo de datos), plotly (visualización)

## Hallazgos
- yfinance devuelve las columnas en un MultiIndex (Price, Ticker), no en
  formato simple — hay que aplanarlo con `columns.get_level_values(0)`
  antes de usar los datos, o cualquier operación posterior falla o da
  resultados incorrectos.
- El orden de columnas por defecto de yfinance es alfabético
  (Close, High, Low, Open, Volume), no el orden tradicional OHLCV — hay
  que reordenar explícitamente por nombre, nunca asumir por posición.
- El precio del oro en el periodo analizado (últimos 12 meses) se movió
  desde ~3400 hasta un pico de ~5500, con una corrección posterior.

## Conclusión
El pipeline base de datos (descarga → limpieza → guardado en CSV →
visualización) queda funcionando y validado. Es la base sobre la que se
construirán los primeros backtests en la Fase 2.

## Próximos pasos
- Fase 2: implementar la primera estrategia (cruce de medias móviles) y
  el motor de backtesting.