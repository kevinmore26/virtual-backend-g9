import { Router } from "express";
import * as tareaController from '../controllers/tareas.controller';
import { crearTarea } from "../controllers/tareas.controller";

export const tareasRoutes = Router()

tareasRoutes.route('/tareas').post(tareaController.crearTarea);