from playwright.sync_api import sync_playwright
import time

#Teste 1: Adicionar itens no carrinho
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#Quando eu pesquisar pelo item Tênis Adidas Coreracer Masculino
#E adicionar o item ao carrinho
#Então o item que foi escolhido deve aparecer no carrinho

def teste_add_carrinho():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica para o código ir até a página da netshoes
        pagina.goto("https://www.netshoes.com.br")

        #Pesquisa o item "Tênis Adidas Coreracer Masculino"
        pagina.fill('xpath=//*[@id="search-input"]', "Tênis Adidas Coreracer Masculino")
        pagina.click('xpath=//*[@id="header-content"]/header/div[1]/section[2]/section/form/div/button')

        #Clica no produto para ver mais detalhes
        pagina.click('xpath=//*[@id="item-list"]/div/a[1]/div/div[2]/div[1]/span')

        #Clica no tamanho 40 para adicionar no carrinho
        pagina.click('xpath=//*[@id="buy-box"]/section[2]/div/div/div/ul/li[4]/a')

        #Clica no botão "Comprar"
        pagina.click('xpath=//*[@id="buy-button-now"]')

        #Verifica se o item foi adicionado ao carrinho
        assert pagina.inner_text('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div/h3') == "Tênis Adidas Coreracer Masculino"
        time.sleep(3)

#Teste 2: Verifica se o limite de 4 itens para o item "Sunga Boxer Masculina Preta De Praia Lisa Surf Short Box".
#Dado que eu tenha um dispositivo com acesso ao site da netshoes.
#Quando eu pesquisar pela item 'Sunga Boxer Masculina Preta De Praia Lisa Surf Short Box'.
#E adicionar o item ao carrinho.
#E clicar 4 vezes para adicionar mais 4 itens.
#Então uma mensagem dizendo que o limite de itens é 4 deve aparecer.

def teste_add_carrinho():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica para o código ir até a página da netshoes
        pagina.goto("https://www.netshoes.com.br")

        #Pesquisa o item "Sunga Boxer Masculina Preta De Praia Lisa Surf Short Box"
        pagina.fill('xpath=//*[@id="search-input"]', 'Sunga Boxer Masculina Preta De Praia Lisa Surf Short Box')

        #Clica no ícone de pesquisar
        pagina.click('xpath=//*[@id="header-content"]/header/div[1]/section[2]/section/form/div/button')

        #Clica no item para ver mais detalhes
        pagina.click('xpath=//*[@id="item-list"]/div/a/div/div[2]/div[1]/span')

        #Clica no tamanho 'G' e clica no botão comprar
        pagina.click('xpath=//*[@id="buy-box"]/section[2]/div/div/div/ul/li[3]/a')
        pagina.click('xpath=//*[@id="buy-button-now"]')

        #Tenta adicionar mais 4 sungas, testando o limite de 4 itens
        pagina.click('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/button[2]')
        pagina.click('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/button[2]')
        pagina.click('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/button[2]')
        pagina.click('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/button[2]')

        #Verifica se o aviso do limite aparece
        assert pagina.inner_text('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div/span') == "Você já atingiu a quantidade máxima desse item no carrinho."
        time.sleep(3)

#Teste 3: Limpar o carrinho
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#Quando eu pesquisar pelo item Tênis Adidas Coreracer Masculino
#E adicionar o item ao carrinho
#E apertar o botão da lata de lixeira para limpar o carrinho
#Então o carrinho estará vazio e aparecerá a mensagem "Seu carrinho está vazio"

def teste_limpa_carrinho():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica para o código ir até a página da netshoes
        pagina.goto("https://www.netshoes.com.br")

        #Pesquisa o item "Tênis Adidas Coreracer Masculino"
        pagina.fill('xpath=//*[@id="search-input"]', "Tênis Adidas Coreracer Masculino")
        pagina.click('xpath=//*[@id="header-content"]/header/div[1]/section[2]/section/form/div/button')

        #Clica no produto para ver mais detalhes
        pagina.click('xpath=//*[@id="item-list"]/div/a[1]/div/div[2]/div[1]/span')

        #Clica no tamanho 40 para adicionar no carrinho
        pagina.click('xpath=//*[@id="buy-box"]/section[2]/div/div/div/ul/li[4]/a')

        #Clica no botão "Comprar"
        pagina.click('xpath=//*[@id="buy-button-now"]')

        #Limpa o carrinho
        pagina.click('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/i')

        #Verifica se o carrinho foi limpo
        assert pagina.inner_text('xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/h1') == "Seu carrinho está vazio"
        time.sleep(3)