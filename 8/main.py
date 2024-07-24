#O seguinte programa busca o produto solicitado pelo usuário na página de Ofertas do Dia, do site Mercado
#Livre. Em seguida, mostra algumas informações sobre os produtos encontrados, tais como nome do produto, vendedor, 
#preço, desconto e se o frete é grátis.

from bs4 import BeautifulSoup
import requests

def find_product():
    html_text = requests.get('https://www.mercadolivre.com.br/ofertas#nav-header').text
    soup = BeautifulSoup(html_text, 'lxml')
    items = soup.find_all('li', class_='promotion-item')

    for item in items:
        item_name = item.find('p', class_='promotion-item__title').text

        if product_name in item_name:
            seller_name = item.find('span', class_='promotion-item__seller')

            if seller_name == None:
                seller_name = 'Não Informado'
            else:
                seller_name = seller_name.text[3:]

            reais = item.find('span', class_='andes-money-amount__fraction').text
            cents = item.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-24')
            if cents == None:
                cents = '00';
            else:
                cents = cents.text

            discount = item.find('span', class_='promotion-item__discount-text').text[:3]

            delivery = item.find('span', class_='promotion-item__pill')
            if delivery == None:
                delivery = ''
            else:
                delivery = delivery.text

            print(f'''
            {item_name}
            Vendido por:{seller_name}
            Preço: R${reais},{cents}
            Desconto: {discount}
            {delivery}''')

if __name__ == '__main__':
    while True:
        print('Digite o nome do produto que deseja buscar (ou * pra encerrar): ')
        product_name = input('>')
        if product_name == '*':
            break;
        print('Buscando...')
        find_product()
