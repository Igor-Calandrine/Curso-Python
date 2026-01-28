"""
Introdução
    A programação orientada a objetos é uma das abordagens mais eficientes para escrever software. Na programação orientada a objetos, escrevemos classes que representam entidadaes e situações do mundo real, e criamos uma objetos com base nessas classes. Quando escrevemos uma classe, definimos o comportamento geral que toda uma categoria de objetos pode ser.
    Criar um objeto apartir de uma classe é uma operação conhecida como instanciação, e trabalhamos com instâncias de uma classe.
    Entender a programação orientada a objetos ajudará a ver o mundo como um programador vê. Ela ajudará você a realmente conhecer o seu código, não apenas o que acontece linha a linha, mas também os conceitos mais amplos por trás dele. Conhecer a lógica por trás das classes treinará você a penas de modo lógico a fim de poder escrever programas que tratem praticamente todo o problema encontrado de forma eficiente.

    Classes -> Representam Entidades (situações do mundo real)
    Classes -> Define o comportamento de objetos da entidade.
    Objeto -> Instâncias de uma classe
    
Problemas Comuns com Implementação Procedural

*   The uses of global data
    Any function that uses and/or changes global data, cannot easily be reused on a different progrma. A function that accesses global data is operating on data tha lives at a different level than the code of the function itself. That function will need a global statement to access this data. You can't just take a function that relies on global data and reuse it in another program, it can only be reused in a program with similar glabal data.

*   Variables scattered
    Many procedural programs tend to have large collections of global variables. By definition, a global variable can be used or changed by any piece of code. By definition, a global variable can be used or changed by any piece of code anywhere on the program. Assignments to global variables are often widely scattered throughout procedural programs, both in the mais code and inside function. Because variable values can change anywhere, ir can be extremely difficult to debug and maintain programs written this way.

*   Acess to much data 
    Function written to use global data often have acces to too much data When a function uses a global list, dictionary, or any other global data structure, it has acess to all the data in that data structure; However, typically the function should operate on only one piece (or just a small amount) of data. HAving the ability to read and modify any data in a large data structure can lead to erros, such accidentally using or overwriting data taht the function was not intended to touch.
    
    
    """

