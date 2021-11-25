const mudar_cor = (componente, elemento, classe_css) => {
    document.getElementById(elemento).
    addEventListener("click", function(){
    document.querySelector(componente).
    setAttribute("class", classe_css);
    })
}

const status_ensino = () => {
  mudar_cor("#cor_status_ensino", "ensino", "cor_status");

  mudar_cor("#cor_status_cursos", "cursos",  "default_color");
  mudar_cor("#cor_status_tour", "tour",  "default_color");
  mudar_cor("#cor_status_maps", "maps", "default_color");
  console.log("Mudança de estado no ensino");
}

const status_cursos = () => {
  mudar_cor("#cor_status_cursos", "cursos",  "cor_status");
  console.log("Mudança de estado no cursos");
}

const status_tour = () => {
  mudar_cor("#cor_status_tour", "tour",  "cor_status");
  console.log("Mudança de estado no tour");
}

const status_maps = () => {
  mudar_cor("#cor_status_maps", "maps", "cor_status");
  console.log("Mudança de estado no maps");
}