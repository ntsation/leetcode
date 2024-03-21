class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Valor do nó atual
        self.next = next  # Referência para o próximo nó

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Criar um nó dummy para simplificar a manipulação
        dummy_head = ListNode(0)
        # Iniciar o ponteiro atual no nó dummy
        current = dummy_head
        # Inicializar a variável de transporte
        carry = 0

        # Enquanto houver números em pelo menos uma das listas
        while l1 or l2:
            # Obter o valor do nó atual em ambas as listas, ou 0 se estiver vazio
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Somar os valores dos nós atuais e o valor de transporte
            total = val1 + val2 + carry
            # Atualizar o valor do transporte para o próximo cálculo
            carry = total // 10
            # Obter o dígito a ser armazenado no nó atual
            digit = total % 10

            # Criar um novo nó com o dígito atual e conectá-lo à lista resultante
            current.next = ListNode(digit)
            # Mover o ponteiro atual para o próximo nó
            current = current.next

            # Mover os ponteiros nas listas originais para os próximos nós
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Se houver transporte após o último cálculo, criar um novo nó para ele
        if carry > 0:
            current.next = ListNode(carry)
        
        # Retornar a lista resultante, excluindo o nó dummy inicial
        return dummy_head.next
