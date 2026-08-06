# 002 — Estrategia de cruce de medias móviles (XAUUSD)

**Fecha:** 2026-08-06
**Estado:** Completado (validación inicial)

## Objetivo
Construir y validar el motor de backtesting de QuantLab, usando como
primer caso de prueba una estrategia simple de cruce de medias móviles
(20/50 días) sobre XAUUSD. El objetivo no es encontrar una estrategia
"final", sino probar que el mecanismo de backtesting (señales, retornos,
métricas) funciona correctamente antes de aplicarlo a estrategias más
sofisticadas.

## Método
- Datos: XAUUSD diario, 1 año (mismo dataset de la Fase 1)
- Media rápida: SMA de 20 días sobre Close
- Media lenta: SMA de 50 días sobre Close
- Señal: 1 (compra) cuando rápida > lenta, -1 (venta) cuando rápida < lenta
- Se aplicó shift(1) a la señal para evitar look-ahead bias (operar solo
  con información disponible al cierre del día anterior)

## Resultados
- Retorno total acumulado: +11.1%
- Drawdown máximo: -26.20%
- Win rate: 100% (2 de 2 operaciones)
- Sharpe Ratio (anualizado): 0.53

## Hallazgos
- La estrategia solo generó 2 operaciones reales en todo el año — muestra
  estadísticamente insignificante para sacar conclusiones sobre si tiene
  ventaja real.
- El Sharpe Ratio bajo (0.53) indica que la relación retorno/riesgo fue
  débil — hubo mucha volatilidad en el camino (drawdown de -26%) en
  relación a la ganancia final obtenida.
- El motor de backtesting (cálculo de señales, retornos, tramos, métricas)
  quedó validado y funcionando — es reutilizable para cualquier estrategia
  futura, no solo esta.

## Conclusión
El resultado positivo (+11.1%) no es evidencia suficiente de que esta
estrategia tenga una ventaja real — se necesitan más años de datos y más
operaciones para una conclusión estadísticamente válida. El verdadero
logro de este experimento es tener el motor de backtesting construido y
probado.

## Próximos pasos
- Fase 3: ampliar el histórico de datos (más años), y empezar a introducir
  rigor estadístico real (significancia, Monte Carlo)
- Formalizar el sistema de trading discrecional propio (H1/M15) en reglas
  cuantificadas, usando este mismo motor