const carrega_imagens = (divDestino, data) => {
    var imagens = data.attr('imagens').split(",");
    var html = "";
    for(i=0;i<imagens.length;i++){
      html = html + "<img src='" + imagens[0] + "'height=1000px'/>";
    }
  
    divDestino.html(html);
  }

const mudar_cor = () => {
    document.getElementById("btn_erro").
    addEventListener("click", function(){
        document.querySelector("*").
        setAttribute("class", "azul");
    })
}