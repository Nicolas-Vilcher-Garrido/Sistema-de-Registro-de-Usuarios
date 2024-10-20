### DESCRIÇÃO DO PROJETO ###
 
 É um projeto que visa simplificar o registro de usuários através de uma aplicação desktop. Ele utiliza Java para criar uma interface gráfica amigável, permitindo que os usuários insiram suas informações, como nome e e-mail, de forma intuitiva.

As informações capturadas pela interface Java são enviadas para um backend em Python utilizando Flask, que atua como uma API RESTful. O Flask processa os dados e se conecta a um banco de dados AWS RDS para armazenamento seguro e escalável. Este banco de dados é configurado para ser acessível somente por meio de conexões autenticadas, garantindo a segurança das informações.

O projeto é estruturado de forma a separar claramente os componentes: a interface Java reside em uma pasta específica, enquanto o código Python e as configurações do banco de dados estão organizados em suas respectivas pastas. Essa organização facilita a manutenção e a escalabilidade do sistema, permitindo a adição de novas funcionalidades ou a integração com outros serviços no futuro.

Em resumo, é uma solução robusta e modular para o registro de usuários, unindo a eficiência do Java no frontend e a flexibilidade do Python no backend, aproveitando a infraestrutura confiável da AWS.
