import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API
import { useNavigate } from "react-router-dom"; // Para redirigir al usuario
import { login } from "../services/authService";

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const [showModal, setShowModal] = useState(false); // Estado para mostrar/ocultar el modal
  const [currentUser, setCurrentUser] = useState(null); // Usuario actual para editar
  const currentUserId = localStorage.getItem("id"); // Cambia esto por el ID del usuario actual (puedes obtenerlo del contexto o token)
  const [token, setToken] = useState(localStorage.getItem("accessToken"));
  const [refreshToken, setRefreshToken] = useState(localStorage.getItem("refreshToken"));
  const navi = useNavigate();

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => handleEdit(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row.id)}
            disabled={row.id === currentUserId}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  const handleEdit = (user) => {
    setCurrentUser(user); // Establecer el usuario actual para editar
    setShowModal(true); // Mostrar el modal
  };

  const handleDelete = (id) => {
    if (id == currentUserId) {
      alert("No puedes eliminar tu propio usuario.");
      return;
    }
    if (window.confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
      axios
        .delete(`http://127.0.0.1:8000/users/api/${id}/`, {
          headers: {
            Authorization: `Bearer ${token}`, // Agregar el token en los encabezados
          },
        })
        .then(() => {
          setData(data.filter((user) => user.id !== id)); // Actualizar la tabla
          alert("Usuario eliminado con éxito.");
        })
        .catch((error) => {
          //Quiero que lo vuelva a intentar pero primero que refresque el token si es un 401
          if (error.response && error.response.status === 401) {
            // Si el token expira, intenta refrescarlo
            axios
              .post("http://127.0.0.1:8000/users/token/refresh/", {
                refresh: refreshToken, // Enviar el refresh token
              })
              .then((response) => {
                localStorage.setItem("accessToken", response.data.access);
                setToken(response.data.access);
                // Reintentar la solicitud DELETE con el nuevo token
                return axios.delete(`http://127.0.0.1:8000/users/api/${id}/`, {
                  headers: {
                    Authorization: `Bearer ${token}`,
                  },
                });
              })
              .then(() => {
                setData(data.filter((user) => user.id !== id)); // Actualizar la tabla
                alert("Usuario eliminado con éxito.");
              })
              .catch((refreshError) => {
                console.error("Error al refrescar el token:", refreshError);
                alert(
                  "No se pudo refrescar el token. Por favor, inicia sesión nuevamente."
                );
                navi("/login");
              });
          } else {
            console.error("Error al eliminar el usuario:", error);
            alert("Ocurrió un error al eliminar el usuario.");
          }
        });
    }
  };

  const handleSave = () => {
    console.log(currentUser);
    axios
      .put(`http://127.0.0.1:8000/users/api/${currentUser.id}/`, currentUser, {
        headers: {
          Authorization: `Bearer ${token}`, // Agregar el token en los encabezados
        },
      })
      .then((response) => {
        setData(
          data.map((user) =>
            user.id === currentUser.id ? response.data : user
          )
        ); // Actualizar la tabla con los datos editados
        setShowModal(false); // Cerrar el modal
        alert("Usuario actualizado con éxito.");
      })
      .catch((error) => {
        if (error.response && error.response.status === 401) {
          // Si el token expira, intenta refrescarlo
          axios
            .post("http://127.0.0.1:8000/users/token/refresh/", {
              refresh: refreshToken, // Enviar el refresh token
            })
            .then((response) => {
              localStorage.setItem("accessToken", response.data.access);
              setToken(response.data.access);

              // Reintentar la solicitud PUT con el nuevo token
              return axios.put(
                `http://127.0.0.1:8000/users/api/${currentUser.id}/`,
                currentUser,
                {
                  headers: {
                    Authorization: `Bearer ${token}`, // Usar el nuevo token
                  },
                }
              );
            })
            .catch((refreshError) => {
              console.error("Error al refrescar el token:", refreshError);
              alert(
                "La sesión ha expirado. Por favor, vuelve a iniciar sesión."
              );
              navi("/login"); // Redirigir al usuario a la página de inicio de sesión
            });
        } else {
          console.error("Error al actualizar el usuario:", error);
          alert("Ocurrió un error al actualizar el usuario.");
        }
      });
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCurrentUser({ ...currentUser, [name]: value });
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
      {showModal && (
        <div className="modal d-block" tabIndex="-1" role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Editar Usuario</h5>
                <button
                  type="button"
                  className="close"
                  onClick={() => setShowModal(false)}
                >
                  <span>&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <form>
                  <div className="form-group">
                    <label>Nombre</label>
                    <input
                      type="text"
                      className="form-control"
                      name="name"
                      value={currentUser.name || ""}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="form-group">
                    <label>Apellido</label>
                    <input type="text"
                    className="form-control"
                    value={currentUser.surname}
                    onChange={handleInputChange}
                     />
                  </div>
                  <div className="form-group">
                    <label>Email</label>
                    <input
                      type="email"
                      className="form-control"
                      name="email"
                      value={currentUser.email || ""}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="form-group">
                    <label>Teléfono</label>
                    <input
                      type="text"
                      className="form-control"
                      name="tel"
                      value={currentUser.tel || ""}
                      onChange={handleInputChange}
                    />
                  </div>
                </form>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={handleSave}
                >
                  Guardar
                </button>
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowModal(false)}
                >
                  Cancelar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserDataTable;
