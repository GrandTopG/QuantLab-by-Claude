# QuantLab — Roadmap del Proyecto

> "No busca decirte cuándo comprar o vender. Busca darte las herramientas para entender profundamente tus estrategias y decidir con evidencia."

---

## 🎯 Objetivo Final (Visión del proyecto terminado)

QuantLab es una **plataforma modular de investigación cuantitativa** donde cualquier idea de trading se convierte en una hipótesis medible. Al finalizar su desarrollo, el sistema permite:

- **Ingerir datos** históricos y en tiempo real de mercados (oro XAUUSD, acciones, índices, futuros).
- **Formular estrategias** como reglas explícitas y reproducibles (código, no intuición).
- **Backtestear** esas estrategias sobre datos históricos con métricas rigurosas (Sharpe, Sortino, drawdown máximo, win rate, expectancy, etc.).
- **Simular** el futuro con Monte Carlo (¿qué tan probable es sobrevivir a una mala racha?).
- **Analizar riesgo** de forma cuantitativa (VaR, volatilidad, correlaciones, exposición).
- **Optimizar parámetros** sin caer en overfitting (walk-forward analysis, validación cruzada).
- **Documentar cada experimento** como un investigador: hipótesis → método → resultado → conclusión.
- **Generar reportes profesionales** (equity curve, tear sheets) que sirvan como track record auditable para presentar a inversores.
- Evolucionar hacia **modelos estadísticos avanzados, ML e IA** aplicados a mercados.

**Criterio de éxito del proyecto completo:** poder tomar una idea de trading nueva, convertirla en código en menos de un día, backtestearla con rigor estadístico, y generar un reporte que un inversor profesional respetaría.

---

## 🧭 Cómo trabajar con este roadmap

- Cada **Fase** tiene su propio objetivo demostrable (algo que puedes *ver funcionando*).
- Cada Fase se divide en **Commits** (pasos pequeños, cada uno deja el proyecto funcional).
- Como no vienes de programación, cada Fase incluye una sección de **"Qué vas a aprender"** — el roadmap es también tu currículo.
- Cada commit relevante para tu track record se documenta en `research_log/` (carpeta de bitácora de investigación) — esto es tu evidencia para inversores futuros.

---

## FASE 0 — Fundación del Proyecto
**Objetivo de fase:** Tener el entorno de trabajo listo, el repositorio estructurado, y saber ejecutar tu primer script de Python.

**Qué vas a aprender:** instalar Python, usar terminal básica, qué es Git/GitHub, estructura de carpetas de un proyecto de datos.

Commits:
1. `chore: instalar Python, Git y VS Code`
2. `chore: crear repositorio QuantLab en GitHub`
3. `chore: estructura inicial de carpetas` (`/data`, `/notebooks`, `/src`, `/research_log`, `/reports`)
4. `docs: README.md con visión del proyecto`
5. `chore: configurar entorno virtual y requirements.txt`
6. `feat: script "hello_quantlab.py" — primer script ejecutado con éxito`

---

## FASE 1 — Datos: la materia prima
**Objetivo de fase:** Poder descargar, limpiar y visualizar datos históricos de XAUUSD (oro) y guardarlos localmente.

**Qué vas a aprender:** qué es una API, pandas básico, qué es OHLCV, limpieza de datos, gráficos de velas.

Commits:
1. `feat: función para descargar datos históricos (API gratuita, ej. yfinance)`
2. `feat: guardar datos en SQLite`
3. `feat: función de limpieza (nulos, duplicados, gaps)`
4. `feat: graficar velas japonesas con plotly`
5. `docs: notebook "01_exploracion_datos_XAUUSD.ipynb"`
6. `test: validar integridad de datos descargados`

---

## FASE 2 — Tu primera estrategia y motor de backtesting
**Objetivo de fase:** Formular una estrategia simple (ej. cruce de medias móviles) como código, correrla contra datos históricos y ver resultados numéricos.

**Qué vas a aprender:** qué es un backtest, señales de entrada/salida, métricas básicas de rendimiento, riesgo de "look-ahead bias".

Commits:
1. `feat: implementar estrategia base (cruce de medias móviles)`
2. `feat: integrar motor de backtesting (backtesting.py)`
3. `feat: calcular métricas clave (retorno, Sharpe, drawdown máximo, win rate)`
4. `feat: graficar equity curve y drawdown`
5. `docs: research_log/001_cruce_medias_XAUUSD.md` (hipótesis → método → resultado)
6. `refactor: modularizar estrategias en /src/strategies`

---

## FASE 3 — Rigor estadístico y análisis de riesgo
**Objetivo de fase:** No solo saber si una estrategia "ganó", sino si esa ventaja es estadísticamente real y cuál es su riesgo real.

**Qué vas a aprender:** significancia estadística, distribución de retornos, VaR, Monte Carlo, "¿esto es suerte o ventaja real?".

Commits:
1. `feat: simulación Monte Carlo de curvas de equity`
2. `feat: cálculo de VaR y volatilidad histórica`
3. `feat: test de significancia estadística sobre resultados`
4. `feat: análisis de rachas de pérdidas (probabilidad de ruina)`
5. `docs: research_log/002_analisis_riesgo_estrategia_base.md`

---

## FASE 4 — Optimización sin hacer trampa (evitar overfitting)
**Objetivo de fase:** Poder ajustar parámetros de una estrategia de forma rigurosa, sin engañarte a ti mismo con resultados que no se replican en el futuro.

**Qué vas a aprender:** overfitting, walk-forward analysis, in-sample vs out-of-sample, validación cruzada aplicada a series de tiempo.

Commits:
1. `feat: framework de walk-forward analysis`
2. `feat: optimización de parámetros con validación out-of-sample`
3. `feat: comparación de robustez entre versiones de estrategia`
4. `docs: research_log/003_optimizacion_walk_forward.md`

---

## FASE 5 — Dashboard y reportes profesionales
**Objetivo de fase:** Tener una interfaz visual (no solo notebooks) donde puedas correr y comparar estrategias, y generar reportes tipo "tear sheet" presentables a inversores.

**Qué vas a aprender:** Streamlit básico, diseño de reportes financieros, storytelling con datos.

Commits:
1. `feat: dashboard Streamlit — selector de estrategia y activo`
2. `feat: visualización comparativa de múltiples estrategias`
3. `feat: generación automática de reporte PDF (tear sheet)`
4. `feat: página de "portafolio de estrategias" con métricas agregadas`
5. `docs: reporte de ejemplo en /reports`

---

## FASE 6 — Escalar: portafolio, más activos y ML
**Objetivo de fase:** Multi-activo, gestión de portafolio, y primeros modelos de machine learning como herramienta de investigación adicional.

**Qué vas a aprender:** correlación entre activos, optimización de portafolio (Markowitz), introducción a ML aplicado a features de mercado.

Commits:
1. `feat: soporte multi-activo (acciones, índices, futuros)`
2. `feat: matriz de correlaciones y optimización de portafolio`
3. `feat: pipeline de features para ML`
4. `feat: primer modelo predictivo experimental (clasificación de dirección)`
5. `docs: research_log/004_primer_experimento_ML.md`

---

## FASE 7 — Institucionalización (para atraer capital)
**Objetivo de fase:** QuantLab genera automáticamente el tipo de evidencia que un inversor institucional pediría.

Commits:
1. `feat: reporte de track record formal (estilo hedge fund tear sheet)`
2. `feat: sistema de logging de todas las decisiones/cambios de estrategia`
3. `docs: memorándum de estrategia (metodología documentada)`
4. `feat: exportar histórico completo auditable (CSV/PDF firmado con fecha)`

---

## 📌 Regla de oro para avanzar

No pases a la siguiente fase hasta que la actual tenga su **objetivo demostrable cumplido**. Prefiero que tardes una semana más en la Fase 1 a que construyas la Fase 3 sobre datos mal limpiados — en quant, un error silencioso en los datos invalida todo lo que viene después.

---

## Próximo paso inmediato

Empezar por **Fase 0, Commit 1**: instalar el entorno. Si quieres, en el siguiente mensaje te guío paso a paso para dejar tu máquina lista hoy mismo.