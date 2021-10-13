import express, { json } from "express";
import { tareasRouter } from "../routes/tarea.routes";
import { conexion } from "./sequelize";
import swagger from "swagger-ui-express";
import documentacion from '../../swagger_tareas.json' 
import cors from 'cors'


export class Server {
  constructor() {
    this.app = express();
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
    // indicara si el contenido de la izquierda es Verdadero (tiene un valor) entonces usara ese, sino, usara el contenido de la derecha
    // diferencia con el nullish coalescing operator => NCO valida que no sea ni NULL ni UNDEFINED y el logical OR valida que no sea undefined
    this.puerto = process.env.PORT || 8000;
    this.app.use(cors({
      origin:'*',
      methods:'GET',
      allowedHeaders:['Content-Type']
    }));
    this.bodyParser();
    this.rutas();
  }
  bodyParser() {
    this.app.use(json());
  }
  rutas() {
    this.app.get("/", (req, res) => {
      res.json({
        message: "Bienvenido a mi API",
      }); 
    });
    if (process.env.NODE_ENV === "production") {
      documentacion.host = "tareas-express-kevin.herokuapp.com";
      documentacion.schemes = ["https"];
    } else {
      documentacion.host = `127.0.0.1:${this.puerto}`;
      documentacion.schemes = ["http"];
    }
    this.app.use(tareasRouter);
    this.app.use('/docs', swagger.serve, swagger.setup(documentacion));
  }
  start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );

      try {
        // sincronizara todos los modelos creados en el ORM con la bd
        await conexion.sync();
        console.log("Base de datos conectada exitosamente");
      } catch (error) {
        console.log(error);
      }
    });
  }
}
