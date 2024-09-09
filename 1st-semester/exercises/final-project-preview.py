from tkinter import *

# Matrix creation

matrix = [["" for _ in range(6)] for _ in range(14)]
matrix[0][0]= " "
matrix[0][1]= "DERMATOLOGIA"
matrix[0][2]= "UROLOGIA"
matrix[0][3]= "GINECOLOGIA"
matrix[0][4]= "TRAUMATOLOGIA"
matrix[0][5]= "ODONTOLOGIA"
matrix[1][0]= "10:00 AM"
matrix[2][0]= "10:30 AM"
matrix[3][0]= "11:00 AM"
matrix[4][0]= "11:30 AM"
matrix[5][0]= "1:00 PM"
matrix[6][0]= "1:30 PM"
matrix[7][0]= "2:00 PM"
matrix[8][0]= "2:30 PM"
matrix[9][0]= "3:00 PM"
matrix[10][0]= "3:30 PM"
matrix[11][0]= "4:00 PM"
matrix[12][0]= "4:30 PM"
matrix[13][0]= "5:00 PM"

# Filling the matrix

for i in range(1,14,1):
  for j in range(1,6,1):
    matrix[i][j]= "NR"

def userCodeValidation(user_code):
    while len(user_code) != 4:
      print("El codigo ingresado no es valido")
      user_code= input("Ingrese un codigo valido: ")

# Function to schedule an appointment

def book_appointment():
  flag = True
  while(flag):
    user_code= input("Digite su codigo de usuario: ")
    userCodeValidation(user_code)
    appointment_type= input("Ingrese el tipo de cita que necesita: ").upper()
    time = input("Ingrese el horario en el que desea agendar: ")
    for a in range(1,6,1):
      if matrix[0][a]== appointment_type:
        for b in range(1,14,1):
          if matrix[b][0]== time:
            if matrix[b][a] == "NR":
              matrix[b][a] = user_code + ", R"
              print("Su cita fue agendada con exito")
              see_appointments = input("Desea agendar una nueva cita (y/n): ").upper()
              if see_appointments == "N":
                flag= False
            else:
              print("Su cita no ha podida ser agendada")
              see_appointments = input("Desea agendar una nueva cita: ").upper()
              if (see_appointments == "N"):
                flag= False
  main()

# Function to search for an appointment

def search_appointment():
  flag= True
  while flag:
    appointments = 0
    appointments_list = []
    user_code= input("Digite su codigo de usuario: ")
    userCodeValidation(user_code)
    for i in range(1,14,1):
      for j in range(1,6,1):
        if matrix[i][j] == user_code + ", R":
          appointments+= 1
          appointments_list.append((matrix[i][0], matrix[0][j]))
    print("Usted tiene: ",appointments," citas agendadas")
    if (appointments != 0):
      see_appointments = input("Desea ver las citas agendadas a su nombre: ").upper()
      if (see_appointments == "Y"):
        for appointment in appointments_list:
          print(f"Horario: {appointment[0]}, Tipo de cita: {appointment[1]}")
    see_others_appointments = input("Desea ver otras citas: ").upper()
    if (see_others_appointments == "N"):
      flag = False
  main()



def menu():
  print("****** Menú ******")
  print("1. Agendar cita")
  print("2. Buscar cita")
  print("3. Salir")
  option = int(input("Digite la opción de su elección: "))
  return option

def main():
    while True:
        option = menu()
        if option == 1:
            book_appointment()
        elif option == 2:
            search_appointment()
        elif option == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
