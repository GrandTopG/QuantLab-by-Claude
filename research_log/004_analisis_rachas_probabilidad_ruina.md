# 004 — Análisis de rachas de pérdidas y probabilidad de ruina

**Fecha:** 2026-08-10
**Estado:** Completado

## Objetivo
Determinar el riesgo real de rachas de pérdidas consecutivas en la
estrategia de cruce de medias, y calcular el tamaño de posición necesario
para sobrevivir esas rachas sin destruir la cuenta — en respuesta directa
a experiencia previa de pérdida total de cuentas de fondeo por
sobre-apalancamiento.

## Método
- Análisis de rachas reales sobre 49 operaciones (10 años de datos)
- Simulación Monte Carlo (10,000 iteraciones), remuestreando aleatoriamente
  los retornos reales de las operaciones, para estimar el rango de rachas
  posibles más allá de lo que la historia mostró
- Cálculo de capital restante tras distintas rachas, a distintos niveles
  de riesgo por operación (1%, 2%, 3%, 5%, 10%)

## Resultados

### Rachas de pérdidas
- Peor racha real observada (10 años): 6 operaciones
- Peor racha promedio en simulaciones: 6.7
- Percentil 95 (solo 5% de simulaciones peores que esto): 11
- Peor racha máxima simulada: 24

### Capital restante según riesgo por operación

| Riesgo/operación | Tras 6 pérdidas | Tras 11 pérdidas | Tras 24 pérdidas |
|---|---|---|---|
| 1% | 94.1% | 89.5% | 78.6% |
| 2% | 88.6% | 80.1% | 61.6% |
| 3% | 83.3% | 71.5% | 48.1% |
| 5% | 73.5% | 56.9% | 29.2% |
| 10% | 53.1% | 31.4% | 8.0% |

## Hallazgos
- La peor racha real observada (6) subestima el riesgo real — la
  simulación Monte Carlo muestra que rachas de 11+ ocurren en ~5% de los
  escenarios posibles, y rachas de 24 no son descartables.
- Las pérdidas y ganancias son asimétricas: recuperar una pérdida de X%
  requiere una ganancia de X/(1-X)%, que crece de forma no lineal. Una
  pérdida de 68.6% (riesgo 10%, racha de 11) requeriría un 218% de
  ganancia para recuperarse — prácticamente inviable en la práctica.
- Con riesgo de 1% por operación, incluso la peor racha simulada (24
  pérdidas) deja la cuenta en una posición fácilmente recuperable (78.6%
  del capital, requiere ~27% de ganancia para volver al original).

## Conclusión
La supervivencia a largo plazo no depende de encontrar una estrategia sin
rachas malas (matemáticamente no existe tal cosa) — depende de que el
tamaño de posición sea lo suficientemente conservador para que ninguna
racha realista destruya la cuenta. Estrategia (ventaja estadística) y
gestión de riesgo (tamaño de posición) resuelven problemas distintos y
ambos son necesarios.

## Próximos pasos
- Definir el % de riesgo por operación objetivo para cuentas de fondeo
  futuras, basado en este análisis (recomendación preliminar: 1-2%, no
  más, especialmente en cuentas con reglas estrictas de drawdown máximo)
- Aplicar este mismo análisis de rachas al sistema H1/M15 una vez
  cuantificado
- Revisar el "sistema de niveles" propio (dividir cuenta en 10) a la luz
  de este análisis — probablemente necesita ajustarse según estos números
  