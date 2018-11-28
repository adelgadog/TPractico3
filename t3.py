from sys import argv
fuera=list()                        #esta lista es para poner los no admitidos
Ciudades=list()                     #contiene las ciudades
n=0                                 #un contador que se utilizara para que lea cada persona de cada ciudad
fe=open(argv[1],"r")
fr=open('resultado.txt','w')
line=fe.readline().strip()
campos=line.split(":")
print("___________________________________________________________")
fr.write("___________________________________________________________" + '\n')
while line:
    if int(campos[1]) >= 18:
        if campos[2] not in Ciudades:
            Ciudades.append(campos[2])
            if campos[2] == Ciudades[n]:
                print(campos[0] + ", tiene " + str(campos[1]) + " años")
                fr.write(campos[0] + ", tiene " + str(campos[1]) + " años" + '\n')
        else:
            if campos[2] == Ciudades[n]:
                print(campos[0] + ", tiene " + str(campos[1]) + " años")
                fr.write(campos[0] + ", tiene " + str(campos[1]) + " años" + '\n')
    if int(campos[1]) < 18:
        fuera.append(campos)
    line=fe.readline().strip()
    campos=line.split(":")
    if not line:
        print("")
        print("Son de " + Ciudades[n] + " ^")
        print("___________________________________________________________")
        fr.write("" + '\n')
        fr.write("Son de " + Ciudades[n] + " ^ " + '\n')
        fr.write("___________________________________________________________" + '\n')
        n=n+1
        fe=open(argv[1],"r")
        line=fe.readline().strip()
        campos=line.split(":")
        if n == len(Ciudades):
            break

print("No cumplen con los Requesitos: ")
print("")
fr.write("No cumplen con los Requesitos: " + '\n')
fr.write(""+'\n')
fe=open(argv[1],"r")
line=fe.readline().strip()
campos=line.split(":")
while line:
    r=18 - int(campos[1])
    if int(campos[1])<18:
        print(campos[0] + " tiene " + str(campos[1]) + " años, es de " + campos[2] + " te quedan " + str(r) + " años para poder participar")
        fr.write(campos[0] + " tiene " + str(campos[1]) + " años, es de " + campos[2] + " te quedan " + str(r) + " años para poder participar" + '\n')
    line=fe.readline().strip()
    campos=line.split(":")
fe.close()
fr.close()

