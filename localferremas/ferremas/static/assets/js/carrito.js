// carrito.js

function agregarAlCarrito(productoId) {
    fetch('/agregar-al-carrito/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: `producto_id=${productoId}`
    })
    .then(response => {
        if (response.ok) {
            location.reload();
            window.location.href = '/carrito/';
            
        } else {
            throw new Error('Error al agregar el producto al carrito');
        }
    })
    .catch(error => console.error('Error:', error));
}

function decrementarCantidad(carritoId, cantidad) {
    if (cantidad > 0) {
        fetch(`/api/carrito/decrementar/${carritoId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            if (response.ok) {
                cargarCarritoUsuario();
                location.reload();
            } else {
                console.error('Error al decrementar la cantidad del carrito');
            }
        })
        .catch(error => console.error('Error al decrementar la cantidad del carrito:', error));
    }
}


function eliminarDelCarrito(carritoId) {
    // Lógica para eliminar un producto del carrito
    fetch(`/api/carrito/eliminar/${carritoId}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            // Actualizar la interfaz de usuario para reflejar el cambio en el carrito
            cargarCarritoUsuario();
            location.reload();

        } else {
            console.error('Error al eliminar el producto del carrito');
        }
    })
    .catch(error => console.error('Error:', error));
}

function actualizarCantidad(carritoId, nuevaCantidad) {
    // Lógica para actualizar la cantidad de un producto en el carrito
    fetch(`/api/carrito/actualizar/${carritoId}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ cantidad: nuevaCantidad })
    })
    .then(response => {
        if (response.ok) {
            // Actualizar la interfaz de usuario para reflejar el cambio en el carrito
            cargarCarritoUsuario();
        } else {
            console.error('Error al actualizar la cantidad del producto en el carrito');
        }
    })
    .catch(error => console.error('Error:', error));
}

function cargarCarritoUsuario() {
    fetch('/api/carrito/')
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error al cargar el carrito de compras');
        }
    })
    .then(data => {
        // Aquí puedes manejar la respuesta exitosa y actualizar la interfaz de usuario con los datos del carrito
    })
    .catch(error => console.error('Error:', error));
}

// Función auxiliar para obtener el valor del token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

