# =========================================================
# Sistema de Registro de Notas - CUC
# Desarrollado por: David Lopez
# Correo: dlopezh@cuc.edu.co
# Descripción: Script en Python para la gestión y cálculo
# de calificaciones con ponderaciones institucionales.
# =========================================================

def calcular_promedio():
    print("==========================================")
    print("      SISTEMA DE CALIFICACIONES CUC       ")
    print("==========================================")
    
    try:
        # Solicitud de calificaciones con sus correspondientes porcentajes
        nota1 = float(input("Ingrese la nota del Primer Corte (30%): "))
        nota2 = float(input("Ingrese la nota del Segundo Corte (30%): "))
        nota3 = float(input("Ingrese la nota del Tercer Corte (40%): "))
        
        # Cálculo de la nota definitiva según ponderaciones
        definitiva = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)
        
        print("\n------------------------------------------")
        print(f"Nota Definitiva Calculada: {definitiva:.2f}")
        
        # Evaluación del estado académico del estudiante
        if definitiva >= 3.0:
            print("Estado Académico: APROBADO 🎉")
        else:
            print("Estado Académico: REPROBADO ❌")
        print("------------------------------------------")
        
    except ValueError:
        print("\n[Error]: Ingrese únicamente números válidos para las calificaciones.")

if __name__ == "__main__":
    calcular_promedio()