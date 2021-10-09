import {Tarea} from "../config/models";

export const crearTarea = async(req,res)=>{
    const data = req.body
    await Tarea.create(data)
    try{
        const nuevaTarea= await Tarea.create(data);
        return res.status(201).json({
            message:"Tarea creada exitosamente",
            content: nuevaTarea
        })
    }catch(error){
        return res.status(500).json({
            message:"Error al crear la tarea",
            content:error,
        })
    }
}