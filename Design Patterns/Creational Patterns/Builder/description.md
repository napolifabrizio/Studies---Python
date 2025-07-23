# Builder

## O que é

    Esse design pattern foca na construção de objetos. Em vez da Factory, que foca em criar sunclasses dos tipos de objetos, o Builder foca em criar construtores como as subclasses, e o objeto é o resultado desses construtores.

## Analogia

Vamos supor que queremos construir um sistema que mexe com tipos de pizza. A Factory faria pra cada tipo de pizza, uma subclasse, enquanto o Builder faria um (ou mais) construtor, onde esse construtor tem métodos que criam o objeto da pizza parte por parte.

## Que problema ele resolve?

Nesse exemplo da pizza, eu teria várias subclasses, pois cada pizza precisaria de uma subclasse, o que pode ficar confuso uma hora. O Builder eu posso fazer construtores que montam a pizza, centralizando mais o codigo, ainda mais com o uso do Director.

Outro problema que ele resolve é o seguinte, vamos supor que chocolate é um dos parametros, mas faz sentido uma pizza salgada possuir um parametro chocolate? Com builder, eu não preciso colocar que todos objetos da pizza tenham os mesmos parametros, eu realmente estou criando uma pizza step by step, se eu não mencionei chocolate na pizza, então ela não irá possuir.

