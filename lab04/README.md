# Lab 04 – Configurarea Jenkins cu Docker, SSH Agent și Pipeline CI/CD

## Descrierea proiectului

Scopul acestui laborator este configurarea unui mediu Jenkins utilizând containere Docker, crearea unui agent SSH pentru execuția joburilor și configurarea unei pipeline CI/CD pentru un proiect PHP care conține teste unitare. Soluția include un Jenkins Controller, un agent configurat manual prin SSH și un Jenkinsfile pentru automatizarea procesului de instalare a dependințelor și rulare a testelor.

## Structura Proiectului

![](./images/image1.png)

## Continutul Fisierelor

docker-compose.yml:

![](./images/image2.png)

Dockerfile pentru SSH Agent:

![](./images/image3.png)

## Generarea cheilor SSH

Generarea ssh in directorul secrets si salvam continutul in .env:

![](./images/generare_ssh.png)

![](./images/generare_ssh2.png)

![](./images/generare_ssh3.png)

## Pornirea Jenkins

Construirea imaginii pentru agent și pornirea Jenkins + agent în containere separate:

![](./images/jenkins1.png)

![](./images/jenkins2.png)

Pentru parola inițială:

![](./images/jenkins3.png)

Instalarea pluginurilor sugerate:

![](./images/jenkins4.png)

Crearea unui admin user:

![](./images/jenkins5.png)

![](./images/jenkins6.png)

![](./images/jenkins7.png)

## Configurare SSH Agent în Jenkins

Adaudam credentiale cu cheia privata:

![](./images/jenkins8.png)

![](./images/jenkins9.png)

Creem un nou nod pentru shh-agent

![](./images/jenkins10.png)

![](./images/jenkins11.png)

![](./images/jenkins12.png)

Fisierul Jenkinsfile pentru testare pipeline:

![](./images/image4.png)

Testare pipeline:

![](./images/jenkins13.png)

![](./images/jenkins14.png)

![](./images/jenkins15.png)

![](./images/jenkins16.png)

## Întrebări și răspunsuri

### Avantajele folosirii Jenkins pentru automatizarea DevOps

- Automatizează complet procesul CI/CD.

- Permite rularea testelor și verificări constante asupra codului.

- Extensibil prin plugin-uri.

- Poate lucra cu agenți multipli pe sisteme diferite.

- Suport excelent pentru Docker, GitHub și alte tool-uri DevOps.

### Tipuri de agenți Jenkins

- SSH Agents — folosiți în acest laborator.

- JNLP Agents — conectați din exterior prin protocolul JNLP.

- Docker Agents — fiecare build rulează într-un container.

- Kubernetes Agents — poduri dinamice create pe cerere.

- Static Agents — mașini fizice sau VM-uri cu agent instalat manual.

### Probleme întâlnite și soluții

- Agentul nu se conecta:	Verificare cheie SSH, host name, credentiale

- PHP nu era instalat pe agent:	Instalare php-cli prin Dockerfile

- Pipeline-ul eșua la Composer:	Am facut un repo php simplu si valid