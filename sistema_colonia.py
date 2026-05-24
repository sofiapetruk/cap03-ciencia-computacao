def priorizar_sistemas(energia_disponivel):
    """
    Recebe a energia disponível e decide quais sistemas manter ligados.
    Retorna uma lista de ações com base em faixas de energia.
    """
    sistemas = {
        "suporte_a_vida": 50,
        "comunicacao": 20,
        "iluminacao": 15,
        "laboratorio": 25,
        "entretenimento": 10,
    }

    consumo_total = sum(sistemas.values())

    acoes = []
    acoes.append(f"Energia disponível: {energia_disponivel} kWh")
    acoes.append(f"Consumo total se tudo ligado: {consumo_total} kWh")

    if energia_disponivel >= consumo_total:
        acoes.append("STATUS: Todos os sistemas podem operar normalmente.")
    elif energia_disponivel >= 85:
        acoes.append("ALERTA: Desligar entretenimento para economizar energia.")
        acoes.append("Sistemas mantidos: suporte à vida, comunicação, iluminação, laboratório.")
    elif energia_disponivel >= 70:
        acoes.append("ALERTA: Desligar entretenimento e laboratório.")
        acoes.append("Sistemas mantidos: suporte à vida, comunicação, iluminação.")
    elif energia_disponivel >= 50:
        acoes.append("ALERTA GRAVE: Manter apenas suporte à vida e comunicação.")
        acoes.append("Sistemas desligados: laboratório, iluminação, entretenimento.")
    else:
        acoes.append("EMERGÊNCIA: Energia crítica! Manter apenas suporte à vida.")
        acoes.append("Todos os sistemas não essenciais DESLIGADOS.")

    return acoes


def analisar_energia(geracao, consumo, reserva=0):
    """
    Compara geração, consumo e reserva de energia.
    Gera uma decisão clara sobre a situação energética da colônia.
    """
    saldo = geracao - consumo
    
    acoes = []
    acoes.append(f"Geração: {geracao} kWh | Consumo: {consumo} kWh | Reserva: {reserva} kWh")

    if consumo > geracao:
        deficit = consumo - geracao
        acoes.append(f"ALERTA: consumo maior que geração (déficit de {deficit} kWh).")
        if reserva >= deficit:
            acoes.append(f"Reserva suficiente para cobrir o déficit. Reserva restante: {reserva - deficit} kWh.")
        else:
            acoes.append("CRÍTICO: Reserva insuficiente! Reduzir consumo imediatamente.")
    elif geracao > consumo:
        excedente = geracao - consumo
        acoes.append(f"SUGESTÃO: armazenar energia excedente ({excedente} kWh).")
    else:
        acoes.append("STATUS: Geração e consumo equilibrados.")

    return acoes

def calcular_regressao(x_lista, y_lista):
    """
    Ajusta uma reta Y = a + b*X usando mínimos quadrados.
    Retorna os coeficientes a (intercepto) e b (inclinação).
    """
    n = len(x_lista)
    soma_x  = sum(x_lista)
    soma_y  = sum(y_lista)
    soma_xy = sum(x_lista[i] * y_lista[i] for i in range(n))
    soma_x2 = sum(x ** 2 for x in x_lista)

    b = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    a = (soma_y - b * soma_x) / n
    return round(a, 4), round(b, 4)


def prever_energia_eolica(vento_historico, energia_historica, vento_novo):
    """
    Usa regressão linear para prever energia eólica gerada
    a partir de uma nova velocidade de vento.
    """
    a, b = calcular_regressao(vento_historico, energia_historica)
    previsao = a + b * vento_novo
    return round(previsao, 2), a, b


def prever_energia_solar(irradiancia_historica, energia_historica, irradiancia_nova):
    """
    Usa regressão linear para prever energia solar gerada
    a partir de um novo valor de irradiância.
    """
    a, b = calcular_regressao(irradiancia_historica, energia_historica)
    previsao = a + b * irradiancia_nova
    return round(previsao, 2), a, b


def executar_sistema():
    print("=" * 60)
    print("  SISTEMA DE GESTÃO DE ENERGIA - COLÔNIA ESPACIAL")
    print("=" * 60)

    # --- 3.1 Previsão eólica ---
    print("\n[1] PREVISÃO DE ENERGIA EÓLICA (Regressão Linear)")
    print("-" * 60)
    vento    = [8,  10,  12,  14,  16]
    energia_eolica = [20, 25, 30, 35, 40]
    vento_futuro = 11

    previsao_eolica, a_e, b_e = prever_energia_eolica(vento, energia_eolica, vento_futuro)
    print(f"Dados históricos -> Vento: {vento}")
    print(f"                 -> Energia: {energia_eolica}")
    print(f"Modelo ajustado: Y = {a_e} + {b_e} * X")
    print(f"Entrada : vento = {vento_futuro} km/h")
    print(f"Saída   : previsão de energia eólica ≈ {previsao_eolica} kWh")

    # --- 3.2 Previsão solar ---
    print("\n[2] PREVISÃO DE ENERGIA SOLAR (Regressão Linear)")
    print("-" * 60)
    irradiancia    = [400, 600, 800, 1000]
    energia_solar  = [10,  20,  30,  40]
    irradiancia_nova = 700

    previsao_solar, a_s, b_s = prever_energia_solar(irradiancia, energia_solar, irradiancia_nova)
    print(f"Dados históricos -> Irradiância: {irradiancia} W/m²")
    print(f"                 -> Energia:     {energia_solar} kWh")
    print(f"Modelo ajustado: Y = {a_s} + {b_s} * X")
    print(f"Entrada : irradiância = {irradiancia_nova} W/m²")
    print(f"Saída   : previsão de energia solar ≈ {previsao_solar} kWh")

    # --- 3.3 Análise de energia ---
    geracao_total = previsao_eolica + previsao_solar
    consumo_atual = 70
    reserva_atual = 15

    print("\n[3] ANÁLISE DE ENERGIA")
    print("-" * 60)
    resultados_analise = analisar_energia(geracao_total, consumo_atual, reserva_atual)
    for linha in resultados_analise:
        print(linha)

    # --- 3.4 Priorização de sistemas ---
    print("\n[4] PRIORIZAÇÃO DE SISTEMAS")
    print("-" * 60)
    energia_para_sistemas = geracao_total + reserva_atual
    resultados_prioridade = priorizar_sistemas(energia_para_sistemas)
    for linha in resultados_prioridade:
        print(linha)

    print("\n" + "=" * 60)
    print("  FIM DO RELATÓRIO DO SISTEMA")
    print("=" * 60)


if __name__ == "__main__":
    executar_sistema()
