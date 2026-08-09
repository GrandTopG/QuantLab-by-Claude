import pandas as pd

def cruce_medias(datos, ventana_rapida=20, ventana_lenta=50):
    datos = datos.copy()

    datos["MA_rapida"] = datos["Close"].rolling(window=ventana_rapida).mean()
    datos["MA_lenta"] = datos["Close"].rolling(window=ventana_lenta).mean()

    datos["Señal"] = 0
    datos.loc[datos["MA_rapida"] > datos["MA_lenta"], "Señal"] = 1
    datos.loc[datos["MA_rapida"] < datos["MA_lenta"], "Señal"] = -1

    datos["Retorno_diario"] = datos["Close"].pct_change()
    datos["Retorno_estrategia"] = datos["Señal"].shift(1) * datos["Retorno_diario"]
    datos["Retorno_acumulado"] = (1 + datos["Retorno_estrategia"]).cumprod()

    return datos