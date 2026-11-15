// Botão "Copiar código" da página de doação
function copiarPix() {
  var campo = document.getElementById("pix-codigo");
  navigator.clipboard.writeText(campo.value);
  document.getElementById("botao-copiar").textContent = "Copiado!";
}
