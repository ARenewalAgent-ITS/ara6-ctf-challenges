const { Sequelize } = require("sequelize");
const crypto = require("crypto");
const { v4: uuidv4 } = require("uuid");

class Database {
    constructor() {
      this.sequelize = new Sequelize({
        dialect: "sqlite",
        storage: "./database.sqlite",
        logging: false,
      });
    }
    
    async connect() {
      try {
        await this.sequelize.authenticate();
        console.log("Connected to the SQLite database using Sequelize");
      } catch (error) {
        console.error("Unable to connect to the database:", error);
      }
    }

    async dropall(){
      try{
        await this.sequelize.drop();
        console.log("All tables dropped successfully");
      }catch(err){
          console.error("Problem on dropping all tables", err);
      }
    }

    async migrate(){
        try{
            const User = require("./models/User");
            const Note = require("./models/Note");
            const presidenteUUID = uuidv4();
            const secretariaUUID = uuidv4();
            const flag = process.env['FLAG'] || "fake_flag";
            await User.sync();
            await Note.sync();
            await User.bulkCreate([{
                    "uuid": presidenteUUID,
                    "email": "lucaleakyeye@ELPresidente.com",
                    "password": crypto.randomBytes(32).toString("hex"),
                    "role": "ELPresidente"
                },
                {
                    "uuid": secretariaUUID,
                    "email": "mollyCemonk@Secretaria",
                    "password": crypto.randomBytes(32).toString("hex"),
                    "role": "Secretaria"
                }
            ]);
            await Note.bulkCreate([
                {
                    "uuid": uuidv4(),
                    "title": flag,
                    "content": "Luca decided to take a break from his usual shakedown routine and try his hand at stand-up comedy. Armed with a microphone and a surprisingly sharp wit, he strutted onto the stage of a local comedy club. His opening line?\"Why do they call me Leaky Eye Luca? Because when I cry, I flood the room!\"The crowd laughed nervously, unsure if they were allowed to laugh at a mobster. Luca mistook their fear for admiration and ended his set by pointing at random audience members, saying, \"You're next, funny guy!\" He left with thunderous applause (and a room full of terrified patrons).",
                    "owner": presidenteUUID
                }
            ]);
            console.log("Database migrated successfully");
        }catch(err){
            console.error("Problem on migrating database", err);
        }
    }

}

module.exports = new Database();

