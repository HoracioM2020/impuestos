ipi={"Dtomin":556.02, "Indif":85528,"Basemax":14839.02, "%-min": 18, "%-max": 32}
print(ipi)
print(ipi["Basemax"])

def main():
  a=int(input("su ingreso anual: "))
  print()
  b=impuesto(a)
  print("El impuesto  es de "), 
  c=round(b,0)
  print(c)

def impuesto(a):
        if a<=ipi["Indif"]:
            impuesto=ipi["%-min"]/100 *a-ipi["Dtomin"]
        if impuesto<0:
            impuesto=0
            print("Usted es un afortunado")
        elif a>ipi["Indif"]:
            impuesto=ipi["Basemax"]+(a-ipi["Indif"]*ipi["%-max"]/100

        return(impuesto)