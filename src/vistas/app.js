//este es el js de istitution
function Guardarinstitution() {
    const codigoinfra = document.getElementById('name');
    const nombreinsti = document.getElementById('apelli');


    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarinstitution', {
        //en el fullname va el dato de la base de datos
        nombre: codigoinfra.value,
        apellido: nombreinsti.value,
      
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