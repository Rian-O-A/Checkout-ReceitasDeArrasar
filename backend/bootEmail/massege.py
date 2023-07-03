
    
def corpo_email(parametro):
    
    if parametro == None:
        model =['📧🍳 Ebook "Receitas para Arrasar" do Grupo Alcarroz Entregue! 🍳📧', """
        <p>🎉 Parabéns! O seu ebook "<b>Receitas para Arrasar</b>" do Grupo Alcarroz já está em suas mãos! Agora você está pronto para se tornar um mestre na cozinha e surpreender seus amigos e familiares com pratos deliciosos.</p>

    <p>📖 O ebook "<b>Receitas para Arrasar</b>" é uma coleção abrangente de receitas cuidadosamente selecionadas pelo Grupo Alcarroz. Com ele, você terá acesso a uma variedade de pratos incríveis que irão despertar seu lado culinário e levar suas habilidades na cozinha a um novo patamar.</p>

    <p>🍽️ Prepare-se para explorar um universo gastronômico diversificado, repleto de receitas irresistíveis. De pratos principais a sobremesas tentadoras, o ebook "<b>Receitas para Arrasar</b>" oferece opções para todos os gostos e ocasiões. Não importa se você é um novato na cozinha ou um chef experiente, há algo especial para todos.</p>

    <p>📚 Para acessar seu ebook "<b>Receitas para Arrasar</b>", siga as instruções abaixo: </p>

    <p>1️⃣ Verifique seu email cadastrado durante o processo de compra, pois o ebook foi enviado para você como um anexo ou clique 👉 <a href="https://drive.google.com/file/d/1y7dDKPTvSj_idevrh4drjjVANYmfeUKG/view?usp=sharing" target="_blank">aqui</a>. Certifique-se de verificar sua caixa de entrada, incluindo a pasta de spam ou lixo eletrônico, caso não encontre o email principal.</p>

    <p>2️⃣ Faça o download do ebook "<b>Receitas para Arrasar</b>" anexado ao email. Certifique-se de ter um dispositivo compatível para leitura de ebooks, como um smartphone, tablet, e-reader ou computador.</p>

    <p>3️⃣ Abra o ebook em seu dispositivo de leitura ou use um aplicativo de leitura de ebooks para desfrutar das receitas e dicas incríveis fornecidas pelo Grupo Alcarroz.</p>

    <p>🔒 Lembre-se de que este ebook é protegido por direitos autorais, portanto, respeite as políticas de uso estabelecidas pelo Grupo Alcarroz. Evite compartilhar o arquivo com terceiros, pois isso pode violar os termos e condições de uso.</p>

    <p>🔍 Explore o mundo das receitas incríveis com o ebook "<b>Receitas para Arrasar</b>" do Grupo Alcarroz. Desperte seu talento culinário e crie pratos de dar água na boca!</p>

    <p>🎁 Agradecemos por escolher o Grupo Alcarroz como seu parceiro na jornada culinária. Se você tiver alguma dúvida ou precisar de suporte adicional, nossa equipe de atendimento ao cliente estará pronta para ajudar. Bom apetite e divirta-se cozinhando! 🍽️✨</p>
        """]
    else:
        model= ["🕗Pagamento Pendente🕗 - Receitas para Arrasar (Grupo Alcarroz)", f"""
        <p>👋 Prezado(a),</p>

        <p>Agradecemos por escolher o Grupo Alcarroz como seu fornecedor preferido para o Receitas para Arrasar. Gostaríamos de fornecer as informações necessárias para concluir o pagamento da sua compra.</p>

        <p>🔑 ID da Compra: {parametro['id']}</p>

        <p>Para efetuar o pagamento, por favor, utilize o link a seguir para acessar o checkout de pagamento:</p>

        <p>🔗 <a href="{parametro['url']}" target="_blank">{parametro['url']}</a></p>

        <p>Ao acessar o link, você será direcionado(a) para a página de pagamento, onde poderá inserir os detalhes necessários e concluir a transação com segurança.</p>

        <p>Após efetuar o pagamento, agradecemos se puder nos enviar um e-mail de confirmação para <b>grupoalcarroz@gmail.com</b>, informando o ID da compra e o comprovante de pagamento. Isso nos ajudará a processar o seu pedido de forma eficiente.</p>

        <p>Caso tenha alguma dúvida ou precise de suporte adicional durante o processo de pagamento, nossa equipe de atendimento ao cliente está pronta para ajudar. Você pode entrar em contato conosco pelos seguintes meios:</p>

        <p>✉️ E-mail: grupoalcarroz@gmail.com</p>

        <p>Agradecemos novamente pela sua compra e pela confiança depositada no Grupo Alcarroz. Estamos empenhados em fornecer um serviço de qualidade e garantir a sua satisfação.</p>

        <p>🌟 Atenciosamente,</p>
        <p>Grupo Alcarroz</p>
        """]
        
    
    return model