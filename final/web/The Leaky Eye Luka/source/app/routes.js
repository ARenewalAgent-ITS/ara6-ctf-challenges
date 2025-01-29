const express = require("express");
const router = express.Router();
const noteController = require("./controllers/noteController");
const userController = require("./controllers/userController");
const authMiddleware = require("./middlewares/authMiddleware");
const secretariaMiddleware = require("./middlewares/secretariaMiddleware");
const presidenteMiddleware = require("./middlewares/presidenteMiddleware");

router.get("/", (req,res)=>{res.redirect("https://villains.fandom.com/wiki/Leaky-Eye_Luca")});
router.get("/register", userController.registerPage);
router.get("/login", userController.loginPage);
router.get("/welcome", authMiddleware, userController.welcomePage);
router.post("/api/register", userController.register);
router.post("/api/login", userController.login);
router.get("/usuario/notes", authMiddleware, noteController.getNoteByUserUsuarioUUID);
router.get("/api/usuario/note/:uuid", authMiddleware, noteController.getNotesByUUID );
router.get("/usuario/note/getnote/:uuid", authMiddleware, noteController.usuarioNoteIndex);
router.get("/usuario/note/createnote", authMiddleware,noteController.usuarioCreateNote);
router.get("/usuario/note/js/success.js", authMiddleware, noteController.usuarioNoteSuccessScript);
router.post("/api/usuario/note", authMiddleware, noteController.createNotes);
router.get("/bot/visit/secretaria", authMiddleware, noteController.visitUsuarioNote);
router.get("/bot/visit/presidente", authMiddleware, secretariaMiddleware, noteController.visitSecretariaNote);
router.get("/presidente/note", authMiddleware,  presidenteMiddleware,noteController.checkSecretariaNote);

module.exports = router;