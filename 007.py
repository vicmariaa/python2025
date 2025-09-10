<!DOCTYPE html>
<html lang="en">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogo da Palavra Secreta</title>
 </head>
 <body>
    <h1>Tente adivinhar a palavra secreta!</h1>
    <input type="text" id="palavraInput">
    <button onclick="vereficarPalavra()">Enviar</button>
    <p id="mensagem"></p>

    <script> const palavraSecreta = "abracadabra";
   function vereficarPalavra() {
    const palavraDigita = document.getElementById("palavraInput").
    value.toLowerCase();

    const mensagemElemento = document.getElementByld("mensagem")
    if(palavraDigitada === palavraSecreta){
        mensagemElemeto.textContent = "Parabéns! Você acertou!";}
    else{
        mensagemElemento.textContent = "Tente Novamente.";
        }
    </script>
    </body>
    </html>
