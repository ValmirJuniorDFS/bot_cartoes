import telebot

# === CONFIGURAÇÕES DO BOT ===
TOKEN = "8152732950:AAGiXy62zvTukR6bj-jNACqbFV_xoSALLa8"
bot = telebot.TeleBot(TOKEN)

# === MENSAGEM DE BOAS-VINDAS ===
@bot.message_handler(commands=['start'])
def boas_vindas(mensagem):
    texto = (
        "🎄 *Bem-vindo(a) ao Atendimento de Cartões de Natal Luxuosos!*\n\n"
        "Aqui você encontra cartões exclusivos com detalhes em prata, ouro e diamantes.\n\n"
        "💎 *Tabela de valores:*\n"
        "• Cartão Prata — R$ 400,00\n"
        "• Cartão Ouro — R$ 700,00\n"
        "• Cartão Diamante — R$ 1.000,00\n\n"
        "💰 Pagamento via *PIX* (chave aleatória).\n\n"
        "Após o pagamento, envie o *comprovante aqui mesmo* para que possamos confirmar sua compra.\n\n"
        "Digite *Quero comprar* para continuar. ✨"
    )
    bot.send_message(mensagem.chat.id, texto, parse_mode="Markdown")

# === TRATAMENTO DAS MENSAGENS ===
@bot.message_handler(func=lambda msg: True)
def respostas(mensagem):
    texto_usuario = mensagem.text.lower()

    if "quero comprar" in texto_usuario:
        resposta = (
            "Perfeito! 💫\n\n"
            "Escolha uma opção digitando o nome do cartão:\n"
            "- *Prata*\n"
            "- *Ouro*\n"
            "- *Diamante*"
        )
        bot.send_message(mensagem.chat.id, resposta, parse_mode="Markdown")

    elif "prata" in texto_usuario:
        bot.send_message(mensagem.chat.id, "🩶 Cartão *Prata* selecionado.\nValor: R$400,00\n\nEnvie o comprovante de pagamento via *PIX* para confirmar seu pedido.", parse_mode="Markdown")

    elif "ouro" in texto_usuario:
        bot.send_message(mensagem.chat.id, "🟡 Cartão *Ouro* selecionado.\nValor: R$700,00\n\nEnvie o comprovante de pagamento via *PIX* para confirmar seu pedido.", parse_mode="Markdown")

    elif "diamante" in texto_usuario:
        bot.send_message(mensagem.chat.id, "💎 Cartão *Diamante* selecionado.\nValor: R$1.000,00\n\nEnvie o comprovante de pagamento via *PIX* para confirmar seu pedido.", parse_mode="Markdown")

    elif "pix" in texto_usuario:
        bot.send_message(mensagem.chat.id, "🔑 Chave PIX (aleatória): [A SER DEFINIDA]\n\nApós o pagamento, envie o comprovante aqui mesmo.", parse_mode="Markdown")

    else:
        bot.send_message(mensagem.chat.id, "Não entendi 😅 — envie */start* para recomeçar ou *Quero comprar* para iniciar uma compra.", parse_mode="Markdown")


print("🤖 Bot está rodando...")
bot.polling()
