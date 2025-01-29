const { DataTypes } = require("sequelize");
const sequelize = require("../database").sequelize;
const { v4: uuidv4 } = require('uuid');
const bcrypt = require("bcrypt");
const User = sequelize.define("user", {
    uuid: { 
        type: DataTypes.UUID, 
        defaultValue: DataTypes.UUIDV4, 
        primaryKey: true 
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false
    },
    role: {
        type: DataTypes.ENUM("ELPresidente","Secretaria", "Usuario")
    },
});
User.createUser = async function (email, password, role) {
    try{
        const uuid = uuidv4();
        const salt = await bcrypt.genSalt(10);
        const hashedPass = await bcrypt.hash(password, salt);
        const user = await this.create({uuid: uuid, email: email, password: hashedPass, role: role})
        return user;
    }catch(err){
        throw new Error("Problem on creating user");
    }
}

User.loginUser = async function (email, password){
    try{
        const user = await this.findOne({where: {email: email}});
        if(!user){
            return null;
        }
        const stat = await checkUser(password, user.password);
        if(!stat){
            return null;
        }
        return user;
    }catch(err){
        throw new Error("Problem on logging in");
    }
}

User.getByUUID = async function (uuid) {
    try{
        const user = await this.findByPk(uuid);
        return user;
    }catch(err){
        throw new Error("Problem on finding user based on uuid");
    }
}

User.getByEmail = async function (email){
    try{
        const user = await this.findOne({where: {email: email}});
    }catch(err){
        throw new Error("Problem On Creating");
    }
}

User.getByRole = async function (role){
    try{
        const user = await this.findOne({where: {role: role}});
        return user;
    }catch(err){
        throw new Error("Problem on finding user based on role");
    }
}
async function checkUser(password, target){
    const stat = await bcrypt.compare(password, target);
    return stat;
}


module.exports = User;