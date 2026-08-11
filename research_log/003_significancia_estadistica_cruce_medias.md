# 003 — Test de significancia estadística: cruce de medias (10 años)

**Fecha:** 2026-08-10
**Estado:** Completado — hipótesis descartada con evidencia

## Objetivo
Determinar si el resultado positivo de la estrategia de cruce de medias
(20/50) sobre XAUUSD, ampliado a 10 años de datos, representa una ventaja
estadística real, o si es explicable por pura casualidad/ruido de mercado.

## Método
- Datos: XAUUSD, 10 años (2016-2026), velas diarias
- Estrategia: cruce de medias 20/50 (misma lógica validada en Fase 2)
- Test aplicado: t-test de una muestra (scipy.stats.ttest_1samp), sobre
  la serie de retornos diarios de la estrategia, contra la hipótesis nula
  de que el retorno promedio verdadero es cero

## Resultados
- Retorno total (10 años): +37.5%
- Drawdown máximo: -34.3%
- Win rate: 38.8% (49 operaciones)
- Sharpe Ratio: 0.28
- Estadístico t: 0.8701
- P-value: 0.3843

## Hallazgos
- Con muestra ampliada (49 operaciones vs. 2 en el análisis inicial), las
  métricas se revelan mucho más débiles de lo que sugería la muestra
  pequeña original.
- El p-value (0.3843) está muy por encima del umbral convencional de 0.05
  — no hay evidencia estadística suficiente para rechazar la hipótesis de
  que el retorno promedio real de la estrategia es cero (es decir, no se
  puede descartar que el resultado positivo se deba al azar).
- El retorno positivo observado podría explicarse en gran parte por la
  tendencia alcista general del oro en el periodo (~2016-2026), más que
  por una ventaja específica de la lógica de cruce de medias.

## Conclusión
La estrategia de cruce de medias 20/50, en su forma actual, NO muestra
evidencia estadísticamente significativa de tener ventaja real sobre
XAUUSD. Se descarta como candidata principal del portafolio, sin
descartar variantes futuras si se prueban con una hipótesis lógica clara
(no exploración exhaustiva de parámetros, para evitar p-hacking).

## Próximos pasos
- Formalizar y cuantificar el sistema de trading propio (H1/M15), que
  parte de experiencia real de mercado en vez de una regla técnica
  genérica — mejor candidato para tener una lógica fundamental de ventaja
  más sólida (ver Principio 6 de PRINCIPIOS_INSTITUCIONALES.md)
- Si se retoma cruce de medias, hacerlo con hipótesis específica y
  validación out-of-sample (Fase 4), no exploración de parámetros

  ## Comparación contra Buy & Hold

- Retorno de la estrategia (10 años): +37.52%
- Retorno de comprar y mantener sin operar (10 años): +226.71%

La estrategia activa no solo carece de significancia estadística, sino
que además tuvo un desempeño muy inferior a simplemente comprar el activo
y no operar — confirma que el resultado positivo de la estrategia se
explica principalmente por la tendencia alcista general del oro en el
periodo, no por una ventaja específica de la lógica de cruce de medias.
Esto refuerza la conclusión: se descarta esta estrategia como candidata
del portafolio en su forma actual.