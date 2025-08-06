# Builder

## O que é

    Esse design pattern foca em adaptar objetos. Voce tem um objeto que faz X, mas o cliente espera Y. Então você cria um Adapter para fazer
    esse Y virar X, usando esse objeto e manipulando o que tiver que manipular.

## Analogia

Vamos supor que queremos construir um sistema que mexe com tipos de pizza. E seu sistema recebe os
ingredientes de um sistema A e precisa enviar pra sistema B. Porém, B espera receber diferente do que A manda, então criamos um Adapter para realmente adaptar isso!

## Que problema ele resolve?

Nesse exemplo da pizza, se eu não tivesse o Adapter, teria que mexer em algum código, podendo quebrar
o sistema se afetar algum acoplamento, com o Adapter, eu apenas crio uma classe intermediária, que
adapta o resultado de um código que ja existe, sem precisar mexer nele!
