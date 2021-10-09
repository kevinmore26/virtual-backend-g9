import express, { json } from "express";
import { conexion } from "./sequelize";
import { tareasRoutes } from "../routes/tarea.routes";

export class Server {
    constructor() {
      this.app = express();
      this.puerto = process.env.PORT || 8000;
      this.bodyParser();
      this.rutas();
    }
    bodyParser() {
        this.app.use(json());
        
      }
    rutas(){
        this.app.get('/',(req,res)=>{
            res.json({
                message:"Bienvenido a mi API"
            })
        });
        this.app.use(tareasRoutes)
    }
    start(){
        this.app.listen(this.puerto,async()=>{
            console.log(
                `Servidor corriendo exitosamente en el puerto ${this.puerto}`
            )
        try{
            await conexion.sync();
            console.log('')
        }catch(error){
            console.log(error)

        }
        })
    }
    }