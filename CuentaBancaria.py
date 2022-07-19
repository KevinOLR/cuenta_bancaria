class CuentaBancaria:
    def __init__(self, tasa_interes, balance_cuenta): 
        self.tasa_interes = tasa_interes
        self.balance_cuenta = balance_cuenta

    def deposito(self, balance_cuenta):
        self.balance_cuenta += balance_cuenta
        return self

    def retiro(self, balance_cuenta):
        if self.balance_cuenta>5:
            self.balance_cuenta -= balance_cuenta + 5
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
        return self

    def mostrar_info_cuenta(self):
        if self.balance_cuenta > 5:
            print(f"Balance: ${self.balance_cuenta}")
        else:
            None
        return self

    def generar_interes(self):
        self.balance_cuenta = self.balance_cuenta + (self.balance_cuenta*self.tasa_interes)/100
        return self

cuenta_1 = CuentaBancaria(1.2,100)
cuenta_2 = CuentaBancaria(1.5,1000)
cuenta_1.deposito(10).deposito(20).deposito(20).retiro(15).generar_interes().mostrar_info_cuenta()
cuenta_2.deposito(100).deposito(200).retiro(50).retiro(30).retiro(10).retiro(10).generar_interes().mostrar_info_cuenta()

