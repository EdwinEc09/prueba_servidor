function guardar(){
    const codigoinfra = document.getElementById('nombre');
    //const nombreinsti = document.getElementById('nombre_insti');
    //const distritos = document.getElementById('distritos');
    //const telefonos = document.getElementById('telefonos');
    //const años = document.getElementById('años');


    axios.post('guardarinstitution', {
        nombre: codigoinfra.value,
        //nombre_institucion: nombreinsti.value,
        //distrito: distritos.value,
        //telefono: telefonos.value,
        //año: años.value
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'
        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}