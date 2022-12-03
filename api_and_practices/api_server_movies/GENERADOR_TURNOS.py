import calendar

# Crea un diccionario de citas, donde la clave es la fecha de la cita y el valor es la hora de la cita
citas = {
    "2022-12-01": "14:00",
    "2022-12-03": "15:00",
    "2022-12-05": "16:00"
}

# Usa la función calendar.monthcalendar para generar un calendario de diciembre de 2022
calendario = calendar.monthcalendar(2022, 12)

# Recorre cada semana del calendario
for semana in calendario:
    # Recorre cada día de la semana
    for dia in semana:
        # Si el día del calendario es un día válido (es decir, no es 0) y hay una cita programada para ese día, imprime la fecha y la hora de la cita
        if dia != 0 and dia in citas:
            print(f"Fecha de la cita: {dia:%Y-%m-%d}, Hora de la cita: {citas[dia]}")