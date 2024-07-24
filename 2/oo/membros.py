class Contador:
    contador = 0 #atributo de classe

    def inst(self):
        return "Teste"

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod
    def mais_um(n):
        return n+1
    
c1 = Contador()
print(c1.inst())

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(999))