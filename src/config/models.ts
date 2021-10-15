import comprasModel from "../models/compras.models";
import detallesModel from "../models/detalles.models";
import productosModel from "../models/productos.models";
import usuariosModel from "../models/usuarios.models"

// RELACIONES
export const Compras = comprasModel();
export const Detalles = detallesModel();
export const Productos = productosModel();
export const Usuarios = usuariosModel();

// Producto tiene muchos Detalles
Productos.hasMany(Detalles, {
  foreignKey: { name: "productoId", allowNull: false, field: "producto_id" },
});
// Detalle pertenece a un Producto
Detalles.belongsTo(Productos, {
  foreignKey: { name: "productoId", allowNull: false, field: "producto_id" },
});

Compras.hasMany(Detalles, {
  foreignKey: { name: "compraId", allowNull: false, field: "compra_id" },
});
Detalles.belongsTo(Compras, {
  foreignKey: { name: "compraId", allowNull: false, field: "compra_id" },
});

Usuarios.hasMany(Compras, {
  foreignKey: { name: "usuarioId", allowNull: false, field: "usuario_id" },
});
Compras.belongsTo(Usuarios, {
  foreignKey: { name: "usuarioId", allowNull: false, field: "usuario_id" },
});
