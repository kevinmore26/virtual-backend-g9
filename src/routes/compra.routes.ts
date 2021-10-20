import {Router} from "express";
import * as compraController from "../controllers/compra.controller";
import { authValidator } from "../middlewares/validator";
const compraRouter = Router();

compraRouter.post("/compra",authValidator, compraController.crearCompra);

compraRouter.post("/crear-preferencia",compraController.crearPreferencia);
// solo para producciones
compraRouter.post("/mp-notificaciones",compraController.mpNotificaciones)


export default compraRouter;