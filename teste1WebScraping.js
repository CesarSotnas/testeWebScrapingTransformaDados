/* Acessar o site: http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar;
   Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
   Baixar o componente organizacional;
*/

//Importando os módulos http e file system
const http = require("http");
const fs = require("fs");

//colocando o endereço da url em uma variável
const url =
  "http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf";

//criando arquivo PDF
const file = fs.createWriteStream("Componente Organizacional.pdf");
const request = http.get(url, function (response) {
  response.pipe(file);
});


//Comando para rodar o código no terminal: node teste1WebScraping.js