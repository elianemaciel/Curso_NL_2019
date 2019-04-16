notas = [10,20,50,100]

def sacar(vlr_saque):

        while vlr_saque != 0:

            if vlr_saque >= 10:
                print("Notas de 10")
                vlr_saque = vlr_saque - 10
                continue

            if vlr_saque >= 20:
                print("Notas de 20")
                vlr_saque = vlr_saque - 20
                continue

            if vlr_saque >= 50:
                print("Notas de 50")
                vlr_saque = vlr_saque - 50
                continue

            if vlr_saque >= 100:
                print("Notas de 100")
                vlr_saque = vlr_saque - 100
                continue

sacar(60)
