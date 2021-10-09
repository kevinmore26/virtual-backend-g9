import { Router } from "express";
import { crearActividad, listarActividades ,devolverActividad,eliminarActividad} from "../controllers/actividades";

export const actividades_router = Router();
actividades_router.post("/actividad", crearActividad);
actividades_router.get("/actividades", listarActividades);
// -------------------

// actividades_router.get("/actividad/:id", devolverActividad);
// actividades_router.put("/actividad/:id", devolverActividad);

// -------------------


actividades_router
    .route("/actividad/:id")
    .get(devolverActividad)
    .put(devolverActividad)
    .delete(eliminarActividad)




// DESTRUCTURACIÓN
// -----------
// const objeto={
//     nombre:'ediard',
//     apellido:'more'
// }

// const {nombre} = objeto
// // es igual a 
// const nombre = objeto.nombre
// -----------