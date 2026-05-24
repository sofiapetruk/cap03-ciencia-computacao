# cap03-ciencia-computacao

# Sistema de Gestão de Energia — Colônia Espacial

Sistema em Python que simula a gestão inteligente de energia de uma colônia espacial. Integra **análise de dados**, **previsão por regressão linear** e **tomada de decisão automática** com base no consumo e geração de energia.

---

## Funcionalidades

| Módulo | O que faz |
|---|---|
| **Priorização de sistemas** | Decide quais sistemas manter ligados conforme a energia disponível |
| **Análise de energia** | Compara geração, consumo e reserva; gera alertas ou sugestões |
| **Previsão eólica** | Usa regressão linear para estimar energia gerada a partir do vento |
| **Previsão solar** | Usa regressão linear para estimar energia gerada a partir da irradiância |

---

## Como executar

Nenhuma biblioteca externa necessária. Basta ter Python 3 instalado.

```bash
python sistema_colonia.py
```

---

## Exemplo de entrada e saída

### Previsão Eólica
```
Entrada : vento = 11 km/h
Saída   : previsão de energia eólica ≈ 27.5 kWh
```

### Análise de Energia
```
Entrada : geração = 40 kWh, consumo = 70 kWh, reserva = 15 kWh
Saída   : ALERTA: consumo maior que geração (déficit de 30 kWh).
          CRÍTICO: Reserva insuficiente! Reduzir consumo imediatamente.
```

### Priorização de Sistemas
```
Entrada : energia_disponivel = 45 kWh
Saída   : EMERGÊNCIA: Energia crítica! Manter apenas suporte à vida.
          Todos os sistemas não essenciais DESLIGADOS.
```

---

## Estrutura do código

```
sistema_colonia.py
│
├── priorizar_sistemas(energia_disponivel)
│     └── Decide quais sistemas ligar/desligar por faixas de energia
│
├── analisar_energia(geracao, consumo, reserva)
│     └── Compara geração vs consumo e emite decisão
│
├── calcular_regressao(x_lista, y_lista)
│     └── Calcula coeficientes a e b pelo método dos mínimos quadrados
│
├── prever_energia_eolica(vento_hist, energia_hist, vento_novo)
│     └── Prevê geração eólica usando regressão linear
│
├── prever_energia_solar(irrad_hist, energia_hist, irrad_nova)
│     └── Prevê geração solar usando regressão linear
│
└── executar_sistema()
      └── Integra todos os módulos e exibe o relatório completo
```

---

## Conceitos aplicados

- Variáveis e listas (Python)
- Estruturas condicionais (`if / elif / else`)
- Funções com parâmetros e retorno
- Laços (`for`, `sum`)
- Regressão linear simples (mínimos quadrados, sem bibliotecas externas)
- Lógica booleana para tomada de decisão

---

## Autores

Projeto desenvolvido como entregável acadêmico da disciplina de Programação / Fundamentos de Computação.
