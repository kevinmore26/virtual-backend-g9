import express from "express";
export class Server{
    constructor(){
        this.app=express();
        this.puerto=8000
    }
    start(){
        this.app.listen(this.puerto,()=>{
            console.log(`Servidor corriendo en el puerto ${this.puerto}`)
        })
    }
}


