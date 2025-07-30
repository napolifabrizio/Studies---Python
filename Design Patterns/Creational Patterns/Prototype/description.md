# Prototype

## O que é

    Esse design pattern foca em criar um objeto original e partir dele, criar cópias. Essas cópias vão ser inicializadas com os mesmos valores, só sendo alterados se o programador quiser!

## Analogia

Vamos supor que queremos construir um sistema que mexe com tipos de pizza. A Factory faria pra cada tipo de pizza, uma subclasse, enquanto o Prototype cria uma classe, e partir dela, cópias que iremos modificar depois.

## Que problema ele resolve?

Eu não preciso criar a mesma classe várias vezes, escrevendo um monte de código que suja a tela do seu monitor. Eu inicializo apenas uma vez, crio cópias e altero seus valores, sem ter colisão de dados (se usar o deepcopy).

