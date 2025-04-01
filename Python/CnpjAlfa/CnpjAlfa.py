import re
import sys

class CNPJ:
    def __init__(self, input_cnpj):
        try:
            cnpj_valido = self.valida_formato(input_cnpj)
            if cnpj_valido:
                self.cnpj = self.remove_pontuacao(input_cnpj)
            else:
                raise Exception("CNPJ não está no padrão aa.aaa.aaa/aaaa-dd (Para validação) ou aa.aaa.aaa/aaaa (Para geração do DV)")
        except Exception as e:
            print(e)
            sys.exit(0)

    def remove_digitos_cnpj(self):
        if len(self.cnpj) == 14:
            self.cnpj_sem_dv = self.cnpj[:-2]
        elif len(self.cnpj) == 12:
            self.cnpj_sem_dv = self.cnpj
        else:
            raise Exception("CNPJ com tamanho inválido!")

    def remove_pontuacao(self, input):
        return ''.join(x for x in input if x not in {'.', '/', '-'})

    def valida(self):
        self.remove_digitos_cnpj()
        dv = self.gera_dv()
        return f"{self.cnpj_sem_dv}{dv}" == self.cnpj

    def gera_dv(self):
        self.remove_digitos_cnpj()
        dv1 = DigitoVerificador(self.cnpj_sem_dv)
        dv1char = str(dv1.calcula())

        dv2 = DigitoVerificador(self.cnpj_sem_dv + dv1char)
        dv2char = str(dv2.calcula())

        return f"{dv1char}{dv2char}"

    def valida_formato(self, cnpj):
        return re.match(r'^([A-Z]|\d){2}\.([A-Z]|\d){3}\.([A-Z]|\d){3}/([A-Z]|\d){4}(-\d{2})?$', cnpj) is not None

class DigitoVerificador:
    def __init__(self, input):
        self.cnpj = input.upper()
        self.pesos = []
        self.digito = 0

    def calcula_ascii(self, caracter):
        return ord(caracter) - ord('0')

    def calcula_soma(self):
        tamanho_range = len(self.cnpj)
        num_range = -(-tamanho_range // 8)  # Ceiling division
        self.pesos = list(range(2, 10)) * num_range
        self.pesos = self.pesos[:tamanho_range][::-1]
        sum_of_products = sum(self.calcula_ascii(c) * self.pesos[index] for index, c in enumerate(self.cnpj))
        return sum_of_products

    def calcula(self):
        mod_sum = self.calcula_soma() % 11
        return 0 if mod_sum < 2 else 11 - mod_sum

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            raise Exception("Formato inválido do CNPJ.")
        exec = sys.argv[1].upper()
        input = sys.argv[2]

        cnpj = CNPJ(input)
        if exec == "-V":
            print(cnpj.valida())
        elif exec == "-DV":
            print(cnpj.gera_dv())
        else:
            raise Exception("Opção inválida passada, as válidas são: -V para validar, -DV para gerar digito validador.")
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(0)