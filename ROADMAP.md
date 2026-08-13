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
6. `feat: sistema de notificaciones (correo/Telegram) cuando se detecta una señal — modo "solo aviso" para operar manual`

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

### Ampliación: Portafolio de Estrategias (no una sola estrategia final)

QuantLab no busca UNA estrategia perfecta — busca construir un portafolio
de varias estrategias validadas independientemente, con lógicas de
ventaja distintas entre sí (tendencia, reversión a la media, sistema
H1/M15 cuantificado, fundamentales/macro), cada una operando de forma
independiente con capital asignado, para lograr un resultado combinado
más estable y menos volátil que cualquier estrategia individual.

**Principio de diseño clave:** las estrategias técnicas y las
fundamentales se mantienen como entradas SEPARADAS del portafolio, no
mezcladas dentro de una sola estrategia híbrida — esto preserva su
independencia real y facilita el diagnóstico si alguna deja de
funcionar. Una variable fundamental puede usarse como *filtro de riesgo*
dentro de una estrategia técnica (ej. no operar en días de anuncio de la
Fed), pero eso es distinto a fusionar fuentes de ventaja dentro de una
misma señal.

Commits sugeridos:
1. `feat: framework para correr múltiples estrategias en paralelo`
2. `feat: cálculo de correlación entre estrategias del portafolio`
3. `feat: asignación de capital entre estrategias (equal weight → risk parity)`
4. `docs: research_log de cada estrategia individual antes de combinarla al portafolio`

### Ampliación: Estrategia basada en fundamentales cuantificados ("quantamental")

Como una entrada más del portafolio (separada de las estrategias
técnicas, ver principio de diseño arriba), incorporar una o más
estrategias que usen variables macro/fundamentales como input
cuantificado — dado que el oro está particularmente influenciado por
estos factores:

- Calendario de decisiones de tasas de la Fed como variable de evento
- DXY (índice del dólar) como filtro de contexto — correlación inversa
  histórica con el oro
- Datos de inflación (CPI) como variable macro
- Datos COT (Commitment of Traders) como filtro de posicionamiento
  institucional

Fuentes: yfinance (DXY), FRED (Reserva Federal, datos macro gratuitos),
CFTC (reportes COT semanales). Se integra al mismo motor de backtesting
ya construido en Fase 2 — solo cambia cómo se genera la columna "Señal"
y qué datos adicionales se usan como input.

Commits sugeridos:
1. `feat: pipeline de descarga de datos macro (DXY, CPI, tasas Fed)`
2. `feat: pipeline de descarga de datos COT`
3. `feat: estrategia fundamental independiente (no combinada con la técnica)`
4. `docs: research_log validando la lógica fundamental de esta estrategia`

---

## FASE 7 — Institucionalización (para atraer capital)
**Objetivo de fase:** QuantLab genera automáticamente el tipo de evidencia que un inversor institucional pediría.

Commits:
1. `feat: reporte de track record formal (estilo hedge fund tear sheet)`
2. `feat: sistema de logging de todas las decisiones/cambios de estrategia`
3. `docs: memorándum de estrategia (metodología documentada)`
4. `feat: exportar histórico completo auditable (CSV/PDF firmado con fecha)`

## Requisito de diseño: Modo Manual vs Automático

El sistema debe tener un interruptor claro entre dos modos de operación:
- **Modo Manual (notificación):** detecta la señal según las reglas de la
  estrategia, y notifica al usuario (correo/Telegram/app) con entrada, SL,
  TP sugeridos — la ejecución de la orden la hace la persona, a mano.
- **Modo Automático (ejecución):** además de detectar la señal, envía la
  orden directamente al broker vía su API, sin intervención manual.

La lógica de detección de señal es la MISMA para ambos modos — lo único
que cambia es el paso final (avisar vs ejecutar). El modo automático solo
se activa después de tener validación estadística sólida de la estrategia
(Fase 3-4 completas) y track record documentado — es la decisión de mayor
riesgo de todo el proyecto, se implementa al final, no al principio.

Commits sugeridos:
1. `feat: capa de ejecución con interruptor modo manual/automático`
2. `feat: integración API de broker para modo automático`
3. `docs: protocolo de decisión para activar modo automático (checklist de validación previa)`

---

## 📌 Regla de oro para avanzar

No pases a la siguiente fase hasta que la actual tenga su **objetivo demostrable cumplido**. Prefiero que tardes una semana más en la Fase 1 a que construyas la Fase 3 sobre datos mal limpiados — en quant, un error silencioso en los datos invalida todo lo que viene después.

---

## Próximo paso inmediato

Empezar por **Fase 0, Commit 1**: instalar el entorno. Si quieres, en el siguiente mensaje te guío paso a paso para dejar tu máquina lista hoy mismo.