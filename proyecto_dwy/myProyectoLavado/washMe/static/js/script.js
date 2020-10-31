function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("verifique el largo del rut");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
        alert("rut incorrecto");
        return false;
    } else {
        alert("Rut Correcto");
        return true;
    }
}


function validaFecha() {
    var fechaFormulario = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    //////////////////////////////////////////////////
    var anno = fechaFormulario.slice(0, 4);
    var mes = fechaFormulario.slice(5, 7);
    var dia = fechaFormulario.slice(8, 10);
    //////////////////////////////////////////////////
    var fechaMia = new Date(anno, (mes - 1), dia); //0-+
    //////////////////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("fecha incorrecta");
        return false;
    } else {
        alert("fecha de nacimiento correcta");
        return true;
    }

}


function validarNombre() {
    var nombre = document.getElementById("txtNombre").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 80) {
        return true;
    }
    if (nombre.trim().length < 3) {
        alert("El Nombre debe tener entre 3 y 80 caracteres");
        return false;
    }

}

function validarApellido() {
    var Apellido = document.getElementById("txtapellido").value;
    if (Apellido.trim().length >= 3 && Apellido.trim().length <= 80) {
        return true;
    }
    if (Apellido.trim().length < 3) {
        alert("El Apellido debe tener entre 3 y 80 caracteres");
        return false;

    }
}

function validarFormulario() {
    var resp;
    resp = true;
    if (validarNombre() == false) {
        resp = false;
    }
    if (validarApellido() == false) {
        resp = false;
    }

    return resp;
}