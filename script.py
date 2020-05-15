import subprocess
import json

#Funciones auxiliares
granInforme = {}
granInforme['Valores']=[]
def appendRegistro(line, header):
    lineSplit = line.split()
    # print(lineSplit)

    if(header==False):
        miniInforme['lineas'].append({
        'language': lineSplit[0],
        'files': int(lineSplit[1]),
        'blank': int(lineSplit[2]),
        'code': int(lineSplit[3])
        })
    else:
        miniInforme['lineas'].append({
        'language': "C/C++ Header",
        'files': int(lineSplit[2]),
        'blank': int(lineSplit[3]),
        'code': int(lineSplit[4])
        })

#Download the repository
repositoryLink = "https://github.com/videolan/vlc-android"

process = subprocess.Popen(["git", "clone", repositoryLink], stdout=subprocess.PIPE, stderr=subprocess.PIPE)



#View releases and commits associated

process = subprocess.Popen(["git", "ls-remote", "--tags", repositoryLink], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
result = out.decode("utf-8")


# Get the commits and the releases

for line in result.split("\n"):
    splitLine = line.split("\t")
    if(len(splitLine)==2):
        # print(splitLine)
        commit = splitLine[0]
        release = splitLine[1]
        # print(commit)
        # print(release)
        process = subprocess.Popen(["git", "checkout", commit], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        #Count lines of code in a language code
        process = subprocess.Popen(["cloc", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        result = out.decode("utf-8")
        # print(result)


        informe= {}
        informe['Registro'] = []
        miniInforme = {}
        miniInforme['lineas'] = []


        lineas = result.split("\n")

        for line in lineas:
            lineSplit = ""

            if "Java" in line.split():
                appendRegistro(line, False)

            if "Kotlin" in line.split():
                appendRegistro(line, False)
            if "C/C++ Header" in line:
                appendRegistro(line,True)
            if "C" in line.split():
                appendRegistro(line, False)
            if "C++" in line.split():
                appendRegistro(line, False)

        miniInforme['commit'] = commit
        miniInforme['tag'] = release
        print(release)
        informe['Registro'].append(miniInforme)
        granInforme['Valores'].append(informe)



with open('data.json', 'w') as outfile:
    json.dump(granInforme, outfile, indent=3)
