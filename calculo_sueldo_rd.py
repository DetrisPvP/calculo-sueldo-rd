TASA_TSS = 0.0591        
TASA_BONIFICACION = 0.0833  
LIMITE_ISR_1 = 34685.00
LIMITE_ISR_2 = 52027.41
LIMITE_ISR_3 = 72260.00
TASA_ISR_1 = 0.15
TASA_ISR_2 = 0.20
TASA_ISR_3 = 0.25

def calcular_ISR(sueldo_mensual):
    """
    Calcula la retención del Impuesto Sobre la Renta (ISR)
    según los tramos establecidos en RD (simplificados para el ejercicio).
    """
    if sueldo_mensual <= LIMITE_ISR_1:
        return 0
    elif sueldo_mensual <= LIMITE_ISR_2:
        return sueldo_mensual * TASA_ISR_1
    elif sueldo_mensual <= LIMITE_ISR_3:
        return sueldo_mensual * TASA_ISR_2
    else:
        return sueldo_mensual * TASA_ISR_3

def solicitar_float_positivo(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def calcular_sueldo_neto():
    print("=== CÁLCULO DE SUELDO NETO - REPÚBLICA DOMINICANA ===")

    sueldo_bruto = solicitar_float_positivo("Ingrese el sueldo bruto mensual (RD$): ")
    otros_descuentos = solicitar_float_positivo("Ingrese otros descuentos aplicables (RD$): ")

    descuento_tss = sueldo_bruto * TASA_TSS
    retencion_isr = calcular_ISR(sueldo_bruto)
    bonificacion = sueldo_bruto * TASA_BONIFICACION

    sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion

    print("\n=== RESULTADOS ===")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:,.2f}")
    print(f"Descuento por Seguridad Social (5.91%): RD$ {descuento_tss:,.2f}")
    print(f"Retención por ISR: RD$ {retencion_isr:,.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:,.2f}")
    print(f"Bonificación (8.33%): RD$ {bonificacion:,.2f}")
    print(f"Sueldo Neto: RD$ {sueldo_neto:,.2f}")

calcular_sueldo_neto()