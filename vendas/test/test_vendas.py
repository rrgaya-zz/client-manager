from django.test import TestCase
from vendas.models import Venda, ItemDoPedido
from produtos.models import Produto


class VendaTestCase(TestCase):
    def setUp(self):
        self.venda = Venda.objects.create(numero="010", desconto=10, status="AB")
        self.produto = Produto.objects.create(
            descricao="Produto Test", preco=1500)

    def test_verifica_num_vendas(self):
        assert Venda.objects.all().count() == 1

    def test_valor_total_venda(self):
        """Testando o VALOR TOTAL da VENDA"""

        ItemDoPedido.objects.create(
            venda=self.venda, produto=self.produto, quantidade=10, desconto=10)

        assert self.venda.valor == 14980

    def test_valor_desconto(self):
        """Testando o valor do DESCONTO"""

        assert self.venda.desconto == 10

    def test_item_incluido_lista_itens(self):
        """Testa se o ITEM esta no set.all() da VENDA"""
        item = ItemDoPedido.objects.create(
            venda=self.venda, produto=self.produto, quantidade=1, desconto=0)

        self.assertIn(item, self.venda.itemdopedido_set.all())

    def test_check_nfe(self):
        """Testando status Nf-e"""
        self.assertFalse(self.venda.nfe_emitida)

    def test_check_status(self):
        self.venda.status = "PC"
        self.venda.save()
        self.assertEquals(self.venda.status, "PC")