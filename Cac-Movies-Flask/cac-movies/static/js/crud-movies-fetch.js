const BASEURL = 'http://127.0.0.1:5000/'; //esta variable o constante tiene nuestra direccion de servidor
// con fetch es una api que permite traer info de una url
/**
 * Función para realizar una petición fetch con JSON.
 * @param {string} url - La URL a la que se realizará la petición.
 * @param {string} method - El método HTTP a usar (GET, POST, PUT, DELETE, etc.).
 * @param {Object} [data=null] - Los datos a enviar en el cuerpo de la petición.
 * @returns {Promise<Object>} - Una promesa que resuelve con la respuesta en formato JSON.
 */
//Usamos el async para que la aplicacion primero complete todas sus peticiones y luego muestre los resultados.
async function fetchData(url, method, data = null) { //method son los metodos http (delete, input, edit)
  const options = {
      method: method,
      headers: { //en header se indica que tipo de dato se espera
          'Content-Type': 'application/json',
      },
      body: data ? JSON.stringify(data) : null,  // Si hay datos, los convierte a JSON y los incluye en el cuerpo, convierte objetos javascript a JSON
  };
  try {
    const response = await fetch(url, options);  // Realiza la petición fetch
    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`); //si da error tira un error de estado
    }
    return await response.json();  // Devuelve la respuesta en formato JSON
  } catch (error) {
    console.error('Fetch error:', error); //si hay un error el catch tira un alert emitiendo que hay un error
    alert('An error occurred while fetching data. Please try again.');
  }
}

/**
 * Función para comunicarse con el servidor para poder Crear o Actualizar
 * un registro de pelicula
 * @returns 
 */
//el .value al final es para que devuelva cada valor de los campos en el html ya que nosotros queremos en el back sus datos.
async function saveMovie(){
  const idMovie = document.querySelector('#id-movie').value; //Modif campos por los del formulario
  const title = document.querySelector('#title').value;
  const director = document.querySelector('#director').value;
  const releaseDate = document.querySelector('#release-date').value;
  const banner = document.querySelector('#banner-form').value;

  //VALIDACION DE FORMULARIO (tira alertas mas notorias.)
  if (!title || !director || !releaseDate || !banner) {
    Swal.fire({
        title: 'Error!',
        text: 'Por favor completa todos los campos.',
        icon: 'error',
        confirmButtonText: 'Cerrar'
    });
    return;
  }
  // Crea un objeto con los datos de la película
  const movieData = { //igualamos las constantes del html a los objetos
      title: title,
      director: director,
      release_date: releaseDate,
      banner: banner,
  };

    
  let result = null;
  // Si hay un idMovie, realiza una petición PUT para actualizar la película existente
  if(idMovie!==""){
    result = await fetchData(`${BASEURL}/api/movies/${idMovie}`, 'PUT', movieData);
  }else{
    // Si no hay idMovie, realiza una petición POST para crear una nueva película
    result = await fetchData(`${BASEURL}/api/movies/`, 'POST', movieData);
  }
  
  const formMovie = document.querySelector('#form-movie');
  formMovie.reset();
  Swal.fire({ //Alerta para mostrar que esta todo correcto.
    title: 'Exito!',
    text: result.message,
    icon: 'success',
    confirmButtonText: 'Cerrar'
  })
  showMovies();
}


/**
 * Funcion que permite crear un elemento <tr> para la tabla de peliculas
 * por medio del uso de template string de JS.
 */
async function showMovies(){
  let movies =  await fetchData(BASEURL+'/api/movies/', 'GET');
  const tableMovies = document.querySelector('#list-table-movies tbody');
  tableMovies.innerHTML='';
  movies.forEach((movie,index) => {  //el foreach itera con todos los datos de nuestra pelicula.
    let tr = `<tr>
                  <td>${movie.title}</td>
                  <td>${movie.director}</td>
                  <td>${movie.release_date}</td>
                  <td>
                      <img src="${movie.banner}" width="30%">
                  </td>
                  <td>
                      <button class="btn-cac" onclick='updateMovie(${movie.id_movie})'><i class="fa fa-pencil" ></button></i> 
                      <button class="btn-cac" onclick='deleteMovie(${movie.id_movie})'><i class="fa fa-trash" ></button></i>
                  </td>
                </tr>`;
    tableMovies.insertAdjacentHTML("beforeend",tr);
  });
}
  
/**
 * Function que permite eliminar una pelicula del array del localstorage
 * de acuedo al indice del mismo
 * @param {number} id posición del array que se va a eliminar
 */
//Aca se encuentra el metodo delete con confirmacion.
function deleteMovie(id){
  Swal.fire({
      title: "Esta seguro de eliminar la pelicula?",
      showCancelButton: true,
      confirmButtonText: "Eliminar",
  }).then(async (result) => {
      if (result.isConfirmed) {
        let response = await fetchData(`${BASEURL}/api/movies/${id}`, 'DELETE');
        showMovies();
        Swal.fire(response.message, "", "success");
      }
  });
  
}


/**
 * Function que permite cargar el formulario con los datos de la pelicula 
 * para su edición
 * @param {number} id Id de la pelicula que se quiere editar
 */
async function updateMovie(id){
  //Buscamos en el servidor la pelicula de acuerdo al id
  let response = await fetchData(`${BASEURL}/api/movies/${id}`, 'GET');
  const idMovie = document.querySelector('#id-movie');
  const title = document.querySelector('#title');
  const director = document.querySelector('#director');
  const releaseDate = document.querySelector('#release-date');
  const banner = document.querySelector('#banner-form');
  
  idMovie.value = response.id_movie;
  title.value = response.title;
  director.value = response.director;
  releaseDate.value = response.release_date;
  banner.value = response.banner;
}
  
// Escuchar el evento 'DOMContentLoaded' que se dispara cuando el 
// contenido del DOM ha sido completamente cargado y parseado.
document.addEventListener('DOMContentLoaded',function(){
  const btnSaveMovie = document.querySelector('#btn-save-movie');
  //ASOCIAR UNA FUNCION AL EVENTO CLICK DEL BOTON
  btnSaveMovie.addEventListener('click',saveMovie); //llamamos al ejecutor de eventos que cuando se clikee el evento btn-save-movie ejecute su evento y guarde los datos.
  showMovies();
});