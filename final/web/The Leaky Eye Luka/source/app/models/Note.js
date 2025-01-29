const { DataTypes, Op } = require("sequelize");
const sequelize = require("../database").sequelize;
const { v4: uuidv4 } = require('uuid');
const User = require("./User");

const Note = sequelize.define("note", {
    uuid: { 
        type: DataTypes.UUID, 
        defaultValue: DataTypes.UUIDV4, 
        primaryKey: true 
    },
    title: {
        type: DataTypes.STRING,
        allowNull: false
    },
    content: {
        type: DataTypes.STRING,
        allowNull: false
    },
    owner: {
        type: DataTypes.UUID,
        allowNull: false,
    }
});

Note.createNote = async function (title, content, owner){
    try{
        const uuid = uuidv4();
        await this.create({uuid, title, content, owner});
        return true;
    }catch(err){
        throw new Error("Error on creating Note");
    }
}

Note.getNoteByUUID = async function (uuid){
    try{
        const note = await this.findByPk(uuid);
        return note;
    }catch(err){
        throw new Error("Problem on finding note based on uuid");
    }
}

Note.getNoteByOwner = async function (owner){
    try{
        const note = await this.findAll({where: {owner: owner}});
        return note;
    }catch(err){
        throw new Error("Problem on finding note based");
    }
}

Note.getPresidenteNote = async function (title, ownerUUID){
    try{
        const Note = await this.findOne({
            where: {
                title:{
                    [Op.startsWith]: title
                },
                owner: ownerUUID
            },
        });
        return Note
    }catch(err){
        throw err;
    }
}
module.exports = Note;