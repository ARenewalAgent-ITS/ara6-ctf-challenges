const secretariaMiddleware = (req, res, next) => {
    if (!req.user){
        return res.status(401).json({ message: "Gaada akses, kamu siapa slur?"});
    }
    if(req.user.role !== "Secretaria"){
        return res.status(401).json({ message: "Kamu bukan Secretaria >:("});
    }
    next();
}

module.exports = secretariaMiddleware;