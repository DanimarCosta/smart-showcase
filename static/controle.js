const mudar_cor = (componente, elemento, classe_css) => {
    document.getElementById(elemento).
    addEventListener("click", function(){
    document.querySelector(componente).
    setAttribute("class", classe_css);
    })
}


// Mostra o que esta selecionado
const status_ensino = () => {
  mudar_cor("#tag_ensino", "tag_ensino", "tag_ensino");
  console.log("Mudança de estado no ensino");
}

const status_cursos = () => {
  mudar_cor("#tag_cursos", "tag_cursos", "tag_cursos");
  console.log("Mudança de estado no ensino");
}

const status_tour = () => {
  mudar_cor("#tag_tour", "tag_tour", "tag_tour");
  console.log("Mudança de estado no ensino");
}

const status_maps = () => {
  mudar_cor("#tag_maps", "tag_maps", "tag_maps");
  console.log("Mudança de estado no ensino");
}

// Redirecionamentos de paginas
const redirecionador = (pagina) => {
  window.location.href = "http://127.0.0.1:5000/" + pagina;
}