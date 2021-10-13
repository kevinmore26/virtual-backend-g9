import { Sequelize } from "sequelize";
require("dotenv").config();


export const conexion = new Sequelize(
  process.env.DATABASE_URL,
  { logging: false,
  dialectOptions : 
  process.env.NODE_ENV === "production"
  ?{
    ssl:{
      rejectUnauthorized: false,
    },
    
  }
: {},
} // logging => indica si que quiere mostrar o no las consultas a la bd,
);
