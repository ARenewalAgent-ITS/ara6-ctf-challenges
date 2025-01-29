const presidenteMiddleware = (req, res, next) => {
    if (!req.user){
        return res.status(401).json({ message: "Gaada akses, kamu siapa slur?"});
    }
    if(req.user.role !== "ELPresidente"){
        return res.status(401).json({ message: "Kamu bukan Secretaria >:("});
    }
    next();
}

module.exports = presidenteMiddleware;