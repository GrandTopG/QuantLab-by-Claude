def calcular_metricas(datos, resumen_tramos):
    retorno_total = datos["Retorno_acumulado"].iloc[-1] - 1

    maximo_historico = datos["Retorno_acumulado"].cummax()
    drawdown = (datos["Retorno_acumulado"] / maximo_historico) - 1
    drawdown_maximo = drawdown.min()

    retorno_promedio_diario = datos["Retorno_estrategia"].mean()
    volatilidad_diaria = datos["Retorno_estrategia"].std()
    sharpe_ratio = (retorno_promedio_diario / volatilidad_diaria) * (252 ** 0.5)

    operaciones = resumen_tramos[resumen_tramos["Señal"] != 0]
    ganadoras = operaciones[operaciones["Retorno_total"] > 0]
    win_rate = len(ganadoras) / len(operaciones)

    return {
        "retorno_total": retorno_total,
        "drawdown_maximo": drawdown_maximo,
        "sharpe_ratio": sharpe_ratio,
        "win_rate": win_rate,
        "total_operaciones": len(operaciones)
    }