const { resolve } = require("path");
const Note = require("../models/Note");
const User = require("../models/User");
const crypto = require("crypto");

const getNoteByUserUsuarioUUID = async (req, res) => {
    const owneruuid = req.user.id;
    try{
        const user = await User.findOne({
            where: {uuid: owneruuid},
            attributes: ['email', 'uuid']
        });
        if(!user){
            return res.status(404).json({message: "User not found"});
        }
        const note = await Note.getNoteByOwner(owneruuid);
        if(!note){
            return res.status(404).json({message: "No notes from user with that uuid"});
        }
        return res.render("notes", {notes: note, user: user});
    }catch(err){
        return res.status(400).json({message: err.message});
    }
};

const getNotesByUUID = async (req, res) => {
    const uuid = req.params.uuid;
    try{
        const note = await Note.getNoteByUUID(uuid);
        if(note){
            return res.status(200).json({message: "success", note: note});
        }
    }catch(err){
        return res.status(400).json({message: err.message});
    }
}

const getNotesByUserSecretariaUUID = async (req, res) => {
    const owneruuid = req.user.id;
    const bgcolor = req.query.bgcolor || "black";
    try{
        const note = await Note.getNoteByOwner(owneruuid);
        if(note){
            return res.status(200).json({message: "success", note: note, bgcolor: bgcolor});
        }
    }catch(err){
        return res.status(400).json({message: `No notes from user with that ${uuid}`});
    }
};

const createNotes = async (req, res) => {
    const { title, content } = req.body;
    const owneruuid = req.user.id;
    if (!title || !content) {
        return res.status(400).json({ message: "Ngapunten, info title dan content nya mas 🙏" });
    }

    try {
        const stat = await Note.createNote(title, content, owneruuid);

        if (!stat) {
            return res.status(400).json({ message: "Gagal Bikin Note" });
        }
        return res.status(200).json({ message: "Success Membuat Note" });
    } catch (err) {
        console.error("Error creating note:", err);
        return res.status(500).json({ message: `Error: ${err.message}` });
    }
};

const usuarioNoteIndex = async(req,res) => {
    const uuid = req.params.uuid;
    const nonce = crypto.randomBytes(16).toString('base64');
    console.log(`[+] Nonce: ${nonce}`);
    return res.set(
        'Content-Security-Policy',
        `script-src 'strict-dynamic' 'nonce-${nonce}'`
    ).render("usuarioNoteDetail", {uuid: uuid, nonce: nonce});
}

const usuarioCreateNote = async(req,res) => {
    res.render("usuarioCreateNote");
}

const usuarioNoteSuccessScript = async(req,res) => {
    const script = `
    function report(){
        alert("Data SuccessFully Spawned");
    }
    `;
    return res.status(200).set('Content-Type','text/javascript').send(script);
}

const visitUsuarioNote = async(req,res) => {
    const note = req.query;
    const bot_url = "http://bot:3000/visit_usuario";
    fetch(bot_url, {
        method: 'POST',
        body: JSON.stringify(note),
        headers: {'Content-Type': 'application/json'}
    }).then((response) => {
        if(response.status === 200){
            return res.status(200).json({message: "success"});
        }
    }).catch((err) => {
        console.log(err);
        return res.status(500).json({message: "error"});
    });
}

const visitSecretariaNote = async(req,res) => {
    const url = req.query;
    const bot_url = "http://bot:3000/visit_secretaria";
    fetch(bot_url, {
        method: 'POST',
        body: JSON.stringify(url),
        headers: {'Content-Type': 'application/json'}
    }).then((response) => {
        if(response.status === 200){
            return res.status(200).json({message: "success"});
        }
    }).catch((err) => {
        console.log(err);
        return res.status(500).json({message: "error"});
    });
}

const checkSecretariaNote = async(req, res) => {
    const title = req.query.title || "";
    try{
        const user = await User.getByRole("ELPresidente");
        const note = await Note.getPresidenteNote(title, user.uuid);
        if (!note) {
            return res.status(200).render("presidenteNote",{email: "Nobody@mail.com", content: "No Content Available"});
        }
            return res.status(200).render("presidenteNote",{email: user.email, content: note.content});
    }catch(err){
        console.log(err);
        return res.status(500).json({message: "error"});
    }

}

module.exports = {
    getNoteByUserUsuarioUUID,
    getNotesByUUID,
    getNotesByUserSecretariaUUID,
    usuarioNoteIndex,
    createNotes,
    usuarioNoteSuccessScript,
    usuarioCreateNote,
    checkSecretariaNote,
    visitUsuarioNote,
    visitSecretariaNote
}